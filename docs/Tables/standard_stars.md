# standard_stars

A table of each standard star across all Hector fields and regions.

## Columns

- __ID__: Standard star target ID.
- __RA__: Right Ascension coordinate.
- __DEC__: Declination coordinate.
- __g_mag__: $g$-band magnitude.
- __r_mag__: $r$-band magnitude.
- __i_mag__: $i$-band magnitude.
- __z_mag__: $z$-band magnitude.
- __y_mag__: $y$-band magnitude.
- __GAIA_g_mag__: Gaia $g$-band magnitude.
- __GAIA_bp_mag__: Gaia $bp$-band magnitude.
- __GAIA_rp_mag__: Gaia $rp$-band magnitude.
- __Mstar__: Ignored for Standard stars- always 0.
- __Re__: Ignored for Standard stars- always 0.
- __z__: Ignored for Standard stars- always 0.
- __GAL_MU_E_R__: Ignored for Standard stars- always 0.
- __pmRA__: Gaia Proper motion, in milli-arcseconds per year, in the RA direction
- __pmDEC__: Gaia Proper motion, in milli-arcseconds per year, in the Declination direction.
- __priority__: Tiling priority.
- __type__: Integer type of the target. Will always be 0 in this case.
- __Field__: Name of the top level field the target is in. Will be one of "WAVES_N", "WAVES_S" or "Cluster"
- __Region__: The name of the region the target is from, e.g. "H01", "G12", "A0119", etc. 

## SQL

```sql
CREATE TABLE standard_stars(
    ID TEXT,
    RA FLOAT,
    DEC FLOAT,
    g_mag FLOAT,
    r_mag FLOAT,
    i_mag FLOAT,
    z_mag FLOAT,
    y_mag FLOAT,
    GAIA_g_mag FLOAT,
    GAIA_bp_mag FLOAT,
    GAIA_rp_mag FLOAT,
    Mstar FLOAT,
    Re FLOAT,
    z FLOAT,
    GAL_MU_E_R FLOAT,
    pmRA FLOAT,
    pmDEC FLOAT,
    priority INTEGER,
    type INTEGER,
    Field TEXT,
    Region TEXT,
    FOREIGN KEY ([ID]) REFERENCES "targets" ([ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
    )
```

## Example rows

|    | ID                  |      RA |      DEC |   g_mag |   r_mag |   i_mag |   z_mag |   y_mag |   GAIA_g_mag |   GAIA_bp_mag |   GAIA_rp_mag |   Mstar |   Re |   z |   GAL_MU_E_R |     pmRA |     pmDEC |   priority |   type | Field   | Region   |
|---:|:--------------------|--------:|---------:|--------:|--------:|--------:|--------:|--------:|-------------:|--------------:|--------------:|--------:|-----:|----:|-------------:|---------:|----------:|-----------:|-------:|:--------|:---------|
|  0 | S111920212349361391 | 21.235  |  3.26742 | 16.4208 | 16.0001 | 15.848  | 15.8144 |       0 |      16.0366 |       16.4018 |       15.5109 |       0 |    0 |   0 |            0 | -3.57862 |  -1.55154 |          5 |      0 | Cluster | A0119    |
|  1 | S110290123865229425 | 12.3865 |  1.91581 | 16.4656 | 16.0001 | 15.7831 | 15.71   |       0 |      16.0089 |       16.4114 |       15.4319 |       0 |    0 |   0 |            0 |  4.8397  |  -9.1822  |          5 |      0 | Cluster | A0119    |
|  2 | S111560193105725314 | 19.3106 |  2.97066 | 16.8265 | 16.0002 | 15.642  | 15.4922 |       0 |      16.0586 |       16.6462 |       15.2304 |       0 |    0 |   0 |            0 | -6.98664 |  -4.63984 |          2 |      0 | Cluster | A0119    |
|  3 | S104540224046751943 | 22.4047 | -2.88208 | 16.2984 | 16.0003 | 15.8841 | 15.8613 |       0 |      16.0096 |       16.3027 |       15.5402 |       0 |    0 |   0 |            0 | 14.4103  | -14.6194  |          8 |      0 | Cluster | A0119    |
|  4 | S105610222692972775 | 22.2693 | -1.98972 | 16.485  | 16.0004 | 15.8075 | 15.7281 |       0 |      16.0305 |       16.4468 |       15.4525 |       0 |    0 |   0 |            0 |  9.64197 |  -4.83663 |          5 |      0 | Cluster | A0119    |

