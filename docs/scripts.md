# Python Scripts

There are two scripts included in the repo to populate the tables. Running the scripts below will delete the tables in the database and repopulate them. Please have a backup copy, especially if you're making changes to the code!

### After an observing run

When an observing run is finished, you should update the CSV files in the `CSV_files_to_update` folder. These keep track of who went observing, the dates of the observing run, and most importantly which tiles were observed. Fill out the new information in the same format as previously, paying close attention to the tile ID. This must be of the format `A3376_00033`, `A3391_A3395_T046`, `H01_00116`, etc, **not** `H01_tile_016` (for example).

When you've updated these CSV files, run the script `create_and_update_observation_tables.py`. This will essentially translate the CSV files into database format. 

You can check that everything has gone to plan by viewing the `galaxies_observed` table, like so:

```python
import pandas as pd
import sqlite3

con = sqlite3.connect("path/to/hector.db")
df = pd.read_sql("select * from galaxies_observed", con)
print(df)
```

You can then check to see that the most recently observed galaxies have made it into that table, save that to a CSV file (or whatever format you like), etc.

### Totally rebuilding the database

The script `create_galaxy_db.py` will totally recreate the following tables:

- [`all_targets`](Tables/all_targets.md)
- [`configured_tiles`](Tables/configured_tiles.md)
- [`galaxies`](Tables/galaxies.md)
- [`guide_stars`](Tables/guide_stars.md)
- [`standard_stars`](Tables/standard_stars.md)
- [`tiles`](Tables/tiles.md)

You shouldn't need to run this very often- only in case things go wrong, there's some database error or you want to start again from scratch for some reason. During normal operation of the observing pipeline, new tiles from the big tiling and the tile/robot files are added to the database automatically.