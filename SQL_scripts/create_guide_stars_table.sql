CREATE TABLE IF NOT EXISTS guide_stars(
    ID TEXT,
    RA FLOAT,
    DEC FLOAT,
    r_mag FLOAT,
    type INTEGER,
    pmRA FLOAT,
    pmDEC FLOAT,
    priority INTEGER,
    Field TEXT,
    Region TEXT,
    FOREIGN KEY ([ID]) REFERENCES "targets" ([ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
    )