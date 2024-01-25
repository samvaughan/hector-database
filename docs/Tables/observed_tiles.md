# observed_tiles

A record of each tile we've observed during the Hector survey.

## Columns

- __id__: An SQL-generated index.
- __tile_ID__: ID of the tile observed.
- __run_ID__: ID of the observing run where that tile was observed.

## SQL 

```SQL
CREATE TABLE IF NOT EXISTS observed_tiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    [tile_ID] TEXT NOT NULL,
    [run_ID] TEXT NOT NULL,
    FOREIGN KEY ([run_id]) REFERENCES "observing_runs" ([run_ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
```

## Example rows

|    |   id | tile_ID                   | run_ID   |
|---:|-----:|:--------------------------|:---------|
|  0 |    0 | Commissioning_A2399_00001 | 2022B_2  |
|  1 |    1 | Commissioning_A2399_00002 | 2022B_2  |
|  2 |    2 | Commissioning_A2399_00003 | 2022B_2  |
|  3 |    3 | Commissioning_A2399_00004 | 2022B_2  |
|  4 |    4 | Commissioning_A2399_00005 | 2022B_2  |