# all_targets

This table contains all the possible objects we might place on a bundle during the Hector Galaxy Survey- galaxies, standard stars and guide stars.

## Columns

- __ID__: Hector Survey ID
- __RA__: Right Ascension coordinate
- __DEC__: Declination Coordinate
- __type__: An integer which is 1 for galaxies, 0 for standard stars and 2 for guide stars


## SQL code

```sql
CREATE TABLE IF NOT EXISTS all_targets(
    ID TEXT,
    RA FLOAT,
    DEC FLOAT,
    type INTEGER
    )
```

## Example rows

|    | ID               |      RA |       DEC |   type |
|---:|:-----------------|--------:|----------:|-------:|
|  0 | C901033186400641 | 14.0174 |  0.261004 |      1 |
|  1 | C901032178409951 | 14.241  | -1.55472  |      1 |
|  2 | C901032178603925 | 14.6039 | -1.40148  |      1 |
|  3 | C901033042501675 | 14.2998 |  0.11102  |      1 |
|  4 | C901031602506671 | 14.465  | -2.60234  |      1 |