# guide_stars

A table of all the guide stars across all the fields and regions of the Hector Survey.

- __ID__: Guide star target ID
- __RA__: Right Ascension coordinate
- __DEC__: Declination coordinate
- __r_mag__: $r$-band magnitude
- __type__: Integer type of the target. Will always be 2 in this case.
- __pmRA__: Gaia Proper motion, in milli-arcseconds per year, in the RA direction
- __pmDEC__: Gaia Proper motion, in milli-arcseconds per year, in the Declination direction.
- __priority__: Tiling priority.
- __Field__: Name of the top level field the target is in. Will be one of "WAVES_N", "WAVES_S" or "Cluster"
- __Region__: The name of the region the target is from, e.g. "H01", "G12", "A0119", etc. 

## SQL

```SQL
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
```

## Example rows

|    | ID                  |      RA |      DEC |   r_mag |   type |      pmRA |     pmDEC | priority   | Field   | Region   |
|---:|:--------------------|--------:|---------:|--------:|-------:|----------:|----------:|:-----------|:--------|:---------|
|  0 | G105710191187618252 | 19.1188 | -1.90181 | 12.3039 |      2 | -27.9186  | -73.0794  |            | Cluster | A0119    |
|  1 | G103710145572640594 | 14.5575 | -3.57503 | 12.3785 |      2 |   8.10336 | -40.4968  |            | Cluster | A0119    |
|  2 | G101600178827535100 | 17.8829 | -5.32945 | 12.4452 |      2 |   3.76461 | -58.9342  |            | Cluster | A0119    |
|  3 | G110600147776097558 | 14.7777 |  2.17267 | 12.4532 |      2 |  32.0362  | -81.3639  |            | Cluster | A0119    |
|  4 | G101480178474447685 | 17.8475 | -5.42725 | 12.484  |      2 | -44.4803  |   3.44717 |            | Cluster | A0119    |