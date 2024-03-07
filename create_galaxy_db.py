import pandas as pd
import sqlite3
from pathlib import Path
import string
import numpy as np


# Important paths for this script!
# The main path to the Hector folder.
hector_folder = Path("/Users/samvaughan/Science/Hector/")

# This is the 'observing' folder, where the final tiles we make live
observing_folder = hector_folder / "Observing/results/"

# This is the folder where all our region catalogues catalogues live
base_catalogue_folder = (
    hector_folder / "Targets/HectorInputCatalogues/results/RegionCatalogues/"
)

# This is the place where the results of the "big tiling" live
base_tiles_folder = hector_folder / "Targets/Tiling/results/"


def get_spectrograph_from_hexabundle(row):
    if row.Hexabundle in (string.ascii_uppercase[:8]):
        return "AAOmega"
    elif row.Hexabundle in (string.ascii_uppercase[8:21]):
        return "Spector"
    elif row.Hexabundle.startswith("GS"):
        return "Guider"
    else:
        raise NameError(
            f"Don't know which spectrograph Hexabundle {row.Hexabundle} is in!"
        )


# First, clear the following tables that we may already have
con = sqlite3.connect("hector.db")
cur = con.cursor()
cur.executescript(
    """
    DROP TABLE IF EXISTS tiles;
    DROP TABLE IF EXISTS targets_tiles;
    DROP TABLE IF EXISTS galaxies;
    DROP TABLE IF EXISTS guide_stars;
    DROP TABLE IF EXISTS standard_stars;
    DROP TABLE IF EXISTS all_targets;
    DROP TABLE IF EXISTS configured_tiles;
    DROP VIEW IF EXISTS galaxies_observed;
    """
)

print("Making the tables...")
# Now make some empty tables with the correct schema
# Firstly for the galaxies
with open("SQL_scripts/create_galaxies_table.sql", "r") as sql_file:
    galaxies_script = sql_file.read()
cur.executescript(galaxies_script)

# Now for the standard stars
with open("SQL_scripts/create_standard_stars_table.sql", "r") as sql_file:
    standard_stars_script = sql_file.read()
cur.executescript(standard_stars_script)

# And the guide stars
with open("SQL_scripts/create_guide_stars_table.sql", "r") as sql_file:
    guide_stars_script = sql_file.read()
cur.executescript(guide_stars_script)

# And the overall targets table
with open("SQL_scripts/create_overall_targets_table.sql", "r") as sql_file:
    overall_sql = sql_file.read()
cur.executescript(overall_sql)

# The tiles table
with open("SQL_scripts/create_tiles_table.sql", "r") as sql_file:
    tiles_script = sql_file.read()
cur.executescript(tiles_script)

# # And the tiles/targets join table
# with open("create_object_tile_join_table.sql", "r") as sql_file:
#     join_script = sql_file.read()
# cur.executescript(join_script)

# And the configured tiles table
with open("SQL_scripts/create_configured_tiles_table.sql", "r") as sql_file:
    configured_tiles_script = sql_file.read()
cur.executescript(configured_tiles_script)


print("Done")

# Now loop through and fill these


for folder, field_name in zip(
    ["HectorClusters_including_fg", "WAVES_S", "WAVES_N"],
    ["Cluster", "WAVES_S", "WAVES_N"],
):
    standard_stars = base_catalogue_folder.glob(f"{folder}/*/*_standard_stars.csv")
    guide_stars = base_catalogue_folder.glob(f"{folder}/*/*_guide_stars.csv")
    if field_name.startswith("W"):
        galaxies = base_catalogue_folder.glob(f"{folder}/*/*_target_galaxies.csv")
    else:
        galaxies = base_catalogue_folder.glob(
            f"{folder}/*/*_target_galaxies_including_fg.csv"
        )

    for galaxy_cat_name in galaxies:
        region = galaxy_cat_name.parent.stem
        print(f"Adding the targets from {field_name} / {region}")

        df = pd.read_csv(galaxy_cat_name)
        df["Field"] = field_name
        df["Region"] = region
        # Now edit the IDs. If the field name starts with W then we're in the WAVES regions
        # Otherwise we're in the clusters.
        # WAVES galaxies have an ID which starts with W, cluster galaxies start with C
        # if field_name.startswith("W"):
        #     df["ID"] = df.ID.apply(lambda x: f"W{x}")
        # else:
        #     df["ID"] = df.ID.apply(lambda x: f"C{x}")
        df.to_sql("galaxies", con, if_exists="append", index=False)

    for standard_star_cat_name in standard_stars:
        print(f"Adding the standard stars from {field_name} / {region}")
        region = standard_star_cat_name.parent.stem
        df = pd.read_csv(standard_star_cat_name)
        df["Field"] = field_name
        df["Region"] = region
        df["ID"] = df.ID.apply(lambda x: f"S{x}")
        df.to_sql("standard_stars", con, if_exists="append", index=False)

    for guide_star_cat_name in guide_stars:
        print(f"Adding the guide stars from {field_name} / {region}")
        region = guide_star_cat_name.parent.stem
        df = pd.read_csv(guide_star_cat_name)
        df["Field"] = field_name
        df["Region"] = region
        df["ID"] = df.ID.apply(lambda x: f"G{x}")
        df.to_sql("guide_stars", con, if_exists="append", index=False)

# Now combine everything together in one big targets tabel
df1 = pd.read_sql("SELECT * from galaxies", con)
df1["type"] = 1
df2 = pd.read_sql("SELECT * from standard_stars", con)
df2["type"] = 0
df3 = pd.read_sql("SELECT * from guide_stars", con)
df3["type"] = 2
all_targets = pd.concat(
    (
        df1.loc[:, ["ID", "RA", "DEC", "type"]],
        df2.loc[:, ["ID", "RA", "DEC", "type"]],
        df3.loc[:, ["ID", "RA", "DEC", "type"]],
    )
)
all_targets.to_sql("all_targets", con, if_exists="append", index=False)


# Finally, make a table of every tile which has been configured- the main thing we need here are the spectrogh and hexabundle each galaxy is in.
configured_tiles = pd.DataFrame()

configured_tiles_2023 = (observing_folder).glob("2*_2*/Upload/*/Files/Tile*.csv")
configured_tiles_commissioning = Path(
    "Tiles_Observed_pre_June2023/Commissioning/"
).glob("*.csv")

all_configured_tiles = list(configured_tiles_2023) + list(
    configured_tiles_commissioning
)

for tile_filename in all_configured_tiles:
    observing_run = tile_filename.parent.parent.parent.parent.stem
    if observing_run == "":
        observing_run = "commissioning"
    old_tile_ID = tile_filename.parent.parent.stem
    if old_tile_ID == "Tiles_Observed_pre_June2023":
        old_tile_ID = tile_filename.stem
    region = old_tile_ID.split("_")[0]
    # Treat the commissioning tiles separately
    if region == "Commissioning":
        region = "_".join(old_tile_ID.split("_")[:-1])
    # And the old tiles separately too
    if region == "Tile":
        region = "_".join(old_tile_ID.split("_")[1:-1])
    # Get the tile number. Almost always it's the last thing separated by '_'
    # Sometimes the last thing is 'SNAFU', so in that case we take the second last
    # Finally, a few tiles have funny names so we treat them at the end
    try:
        tile_number = int(old_tile_ID.split("_")[-1])
    except ValueError:
        if old_tile_ID.split("_")[-1].startswith("T"):
            tile_number = int(old_tile_ID.split("_")[-1].strip("T"))
        else:
            try:
                tile_number = int(old_tile_ID.split("_")[-2])
            except ValueError:
                tile_number = int(old_tile_ID.split("_")[2])
    new_tile_ID = f"{region}_{tile_number:05}"
    tmp_df = pd.read_csv(tile_filename, skiprows=11)
    tmp_df = tmp_df.loc[
        tmp_df["type"].isin([0, 1, 2]), ["ID", "Hexabundle", "type", "RA", "DEC"]
    ]
    tmp_df["tile_ID"] = new_tile_ID
    tmp_df["Spectrograph"] = tmp_df.apply(get_spectrograph_from_hexabundle, axis=1)
    tmp_df["observing_run"] = observing_run

    # Fix the IDs
    # FIXME: do this in a function
    if region in ["G12", "G15", "G23", "H01", "H03"]:
        prefix = "W"
    elif region.startswith("A"):
        prefix = "C"
    elif region.startswith("Commissioning"):
        if region.split("_")[1].startswith("A"):
            prefix = "C"
        else:
            prefix = "W"
    else:
        prefix = "G"

    # Check if we have to edit the IDs or not
    if not np.all(tmp_df.loc[tmp_df["type"] == 1, "ID"].str.startswith(prefix)):
        tmp_df.loc[tmp_df["type"] == 1, "ID"] = tmp_df.loc[tmp_df["type"] == 1].apply(
            lambda x: f"{prefix}{x.ID}", axis=1
        )
        tmp_df.loc[tmp_df["type"] == 2, "ID"] = tmp_df.loc[tmp_df["type"] == 2].apply(
            lambda x: f"G{x.ID}", axis=1
        )
        tmp_df.loc[tmp_df["type"] == 0, "ID"] = tmp_df.loc[tmp_df["type"] == 0].apply(
            lambda x: f"S{x.ID}", axis=1
        )

    tmp_df["row_ID"] = tmp_df.apply(
        lambda row: f"{row.ID}_{row.tile_ID}_{row.observing_run}", axis=1
    )

    configured_tiles = pd.concat(
        (
            configured_tiles,
            tmp_df.loc[
                :,
                [
                    "row_ID",
                    "ID",
                    "tile_ID",
                    "Hexabundle",
                    "Spectrograph",
                    "RA",
                    "DEC",
                    "type",
                ],
            ],
        )
    )

# Now make the table
configured_tiles = configured_tiles.sort_values("tile_ID").reset_index(drop=True)
configured_tiles.to_sql("configured_tiles", con, index=False, if_exists="append")


# Make a view of the galaxies we've already observed
# This makes it easier to view these objects later without having to
# use this long SQL query
cur.executescript(
    """
    CREATE VIEW galaxies_observed
    AS
    SELECT
        configured_tiles.*,
        observed_tiles.run_ID
    FROM configured_tiles
    JOIN observed_tiles ON observed_tiles.tile_ID == configured_tiles.tile_ID
    WHERE configured_tiles.type == 1
    """
)

# Now make the tiles table
all_tiles_dfs = list(base_tiles_folder.glob("*/Tiling/*/*/Tiles/tiles_dataframe.csv"))
tiles_df = pd.DataFrame()
# Make the tile database
for fname in all_tiles_dfs:
    fname = Path(fname)
    region = fname.parent.parent.stem

    if region in (["G12", "G15"]):
        field = "WAVES_N"
        starting_ID_letter = "W"
    elif region in (["G23", "H01", "H03"]):
        field = "WAVES_S"
        starting_ID_letter = "W"
    else:
        field = "Cluster"
        starting_ID_letter = "C"

    tmp_df = pd.read_csv(fname)
    tmp_df.drop(list(tmp_df.filter(regex="Unnamed*")), axis=1, inplace=True)
    tmp_df["region"] = region
    tmp_df["field"] = field
    tmp_df.drop("Tile_number", inplace=True, axis=1)
    # Need to make the tileID 4/5 zeros long
    tmp_df["tile_ID"] = tmp_df.apply(lambda x: f"{x.region}_{x.tile_number:05}", axis=1)
    if tmp_df["ID"].dtype == np.int64:
        tmp_df["ID"] = tmp_df.apply(lambda x: f"{starting_ID_letter}{x.ID}", axis=1)
    tiles_df = pd.concat((tiles_df, tmp_df))

tiles_df.to_sql("tiles", con, if_exists="append", index=False)
# # Now group by the tile ID to make the table of just tiles
# tile_properties = (
#     tiles_df.loc[
#         :,
#         [
#             "tile_ID",
#             "tile_centre_RA",
#             "tile_centre_DEC",
#             "Filler_Galaxy",
#             "MW_analogue",
#             "EO_wind_galaxy",
#         ],
#     ]
#     .groupby("tile_ID")
#     .agg(
#         {
#             "tile_centre_RA": "mean",
#             "tile_centre_DEC": "mean",
#             "Filler_Galaxy": "sum",
#             "MW_analogue": "sum",
#             "EO_wind_galaxy": "sum",
#         }
#     )
#     .rename(
#         dict(
#             Filler_Galaxy="filler_galaxies",
#             MW_analogue="MW_analogues",
#             EO_wind_galaxy="EO_wind_galaxies",
#         )
#     )
# )

# tile_properties.to_sql(
#     "tiles", con, if_exists="append", index=True, index_label="tile_ID"
# )


# # Now finally make the join table, which has the galaxies and stars in each tile
# def replace_galaxy_star_ID(row, field_name):
#     letter = "C"
#     if field_name.startswith("W"):
#         letter = "W"
#     if row["type"] == 1:
#         return f"{letter}{int(row.ID)}"
#     else:
#         return f"S{int(row.ID)}"


# # tile_properties["completed"] = False
# # tile_properties.to_sql("tiles", con=con, if_exists="replace")
# glob1 = Path(
#     "/Users/samvaughan/Science/Hector/Targets/Tiling/results/20230515/Tiling/"
# ).glob("*/*/Tiles/*.fld")
# glob2 = Path(
#     "/Users/samvaughan/Science/Hector/Database/HectorDB_first_attempt/Tiles_Observed_pre_June2023"
# ).glob("*/*/Tiles/*.fld")
# all_tiles = list(glob1) + list(glob2)

# full_tiles_df = pd.DataFrame()
# for t in tqdm(all_tiles):
#     # Get the field, the region and the tile number from the tile filename
#     field = t.parent.parent.parent.stem
#     region = t.parent.parent.stem
#     tile_number = int(t.stem.split("_")[-1].lstrip("GT"))
#     # If we're looking at a guide file...
#     if "GT" in t.stem:
#         tmp_df = pd.read_csv(t, delim_whitespace=True, comment="#")
#         tmp_df["ID"] = tmp_df.ID.apply(lambda x: f"G{x}")
#     # else we're looking at a galaxy tile
#     else:
#         tmp_df = pd.read_csv(t, comment="#")
#         tmp_df["ID"] = tmp_df.apply(replace_galaxy_star_ID, field_name=field, axis=1)

#     tmp_df["tile_ID"] = f"{region}_{tile_number:05}"

#     full_tiles_df = pd.concat((full_tiles_df, tmp_df.loc[:, ["tile_ID", "ID", "type"]]))
# full_tiles_df = full_tiles_df.reset_index(drop=True)

# full_tiles_df.to_sql(
#     "targets_tiles", con, if_exists="append", index=True, index_label="join_ID"
# )
# # Now make the many-to-many table
# tiles_df.loc[:, ["ID", "tile_ID"]].to_sql(
#     "tiles_galaxies", con=con, if_exists="replace"
# )
