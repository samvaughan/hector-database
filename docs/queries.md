# Saved Queries 

There are a number of useful tables which have been saved as a "view" in the database, i.e. they're easy to access without having to type out the whole query again.

To access these tables, find the table below which you'd like to view (e.g. `galaxies_observed`) and do the following:

```python
import pandas as pd
import sqlite3

con = sqlite3.connect("path/to/hector.db")
df = pd.read_sql("select * from desired_table_name", con)
```

### All galaxies we've observed to date

This query selects all the galaxies which have been observed so far. The table is named "galaxies_observed" and it has the following columns:

- `row_ID`: a combination of tile ID, galaxy ID and run ID (will always be unique).
- `ID`: galaxy ID.
- `tile_ID`: The ID of the tile the galaxy was observed in.
- `Hexabundle`: The hexabundle the galaxy was observed in.
- `Spectrograph`: The spectrograph the galaxy was observed in.
- `RA`: Right Ascension.
- `DEC`: Declination.
- `type`: Object type- will always be 1 in this table.
- `run_ID`: The run ID when this tile was observed.

The query which creates this view is below:

```SQL
CREATE VIEW galaxies_observed
AS
SELECT
    configured_tiles.*,
    observed_tiles.run_ID
FROM configured_tiles
JOIN observed_tiles ON observed_tiles.tile_ID == configured_tiles.tile_ID
WHERE configured_tiles.type == 1
```

### Creating a new view

To create a new view, add your SQL query to one of the python scripts. For example, to create a view which calculates the number of tiles observed on each run, as well as the average tiles per night of each run, you could do the following:

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("/path/to/hector.db")
cur = conn.cursor()
cur.execute(
    """
    CREATE VIEW tiles_per_observing_run
    AS
    SELECT observing_runs.run_ID, start_date, end_date, COUNT(observing_runs.run_ID) as N_tiles_observed
    from observing_runs
    JOIN observed_tiles
        ON observing_runs.run_ID = observed_tiles.run_ID
    GROUP BY observing_runs.run_ID
    """
)
```

This would create a new view to a table which has columns 

- `run_ID`.
- `start_date`: the start date of the run.
- `end_date`: the last night of the run.
- `N_tiles_observed`: the total number of tiles observed during the run.