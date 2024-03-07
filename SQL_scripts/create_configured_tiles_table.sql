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