# configured_tiles

This table contains a unique row for every object in every tile which has been configured and is ready to observe at the telescope. 

For example, each configured tile will contain 19 galaxies, 2 standards and 6 guides. Each of these objects will appear in this table, with a unique ID that is a combination of their target ID, the tile ID and the dates of the observing run that this tile was configured for. Using this table, we can reconstruct exactly which objects were observed in a given tile. 

## Columns

- __row_ID__: A unique ID for each row which is a combination of the target ID, the tile ID and the start and end dates of the observing run the tile was configured for.
- __ID__: The unique ID of the target.
- __tile_ID__: The unique ID of the tile.
- __Hexabundle__: The Hexabundle that a given target was assigned to. Will either be A through to U or GS1 through to GS6.
- __Spectrograph__: The spectrograph the Hexabundle corresponds to. Will either be "AAOmega", "Spector" or "Guider" for a guide bundle.
- __RA__: Right Ascension coordinate.
- __DEC__: Declination coordinate.
- __type__: An integer which is 1 for galaxies, 0 for standard stars and 2 for guide stars

## SQL code
```SQL
CREATE TABLE IF NOT EXISTS configured_tiles(
    row_ID ID PRIMARY KEY,
    ID TEXT,
    tile_ID TEXT,
    Hexabundle TEXT,
    Spectrograph TEXT,
    RA FLOAT,
    DEC FLOAT,
    type INTEGER
    )
```

## Example rows


|    | row_ID                                         | ID               | tile_ID     | Hexabundle   | Spectrograph   |      RA |      DEC |   type |
|---:|:-----------------------------------------------|:-----------------|:------------|:-------------|:---------------|--------:|---------:|-------:|
|  0 | 28683696_A3376_00017_20231108_20231119         | 28683696         | A3376_00017 | GS3          | Guider         | 90.3018 | -40.3431 |      2 |
|  1 | C901011946406290_A3376_00017_20231108_20231119 | C901011946406290 | A3376_00017 | M            | Spector        | 90.392  | -39.6452 |      1 |
|  2 | C901011725501113_A3376_00017_20231108_20231119 | C901011725501113 | A3376_00017 | F            | AAOmega        | 90.5162 | -40.1392 |      1 |
|  3 | C901011725207829_A3376_00017_20231108_20231119 | C901011725207829 | A3376_00017 | D            | AAOmega        | 89.7651 | -40.1934 |      1 |
|  4 | C901012057107868_A3376_00017_20231108_20231119 | C901012057107868 | A3376_00017 | S            | Spector        | 89.1799 | -39.5678 |      1 |

