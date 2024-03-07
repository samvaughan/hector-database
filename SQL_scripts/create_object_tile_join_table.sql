CREATE TABLE IF NOT EXISTS targets_tiles(
    join_ID INTEGER PRIMARY KEY,
    tile_ID FLOAT,
    ID FLOAT,
    type INTEGER,
    FOREIGN KEY ([tile_ID]) REFERENCES "tiles" ([tile_ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([ID]) REFERENCES "all_targets" ([ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
    )