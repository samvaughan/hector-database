# tiles

This table is the result of every "tiling" run we've completed on each of the Hector regions. It gives information about every target which is included in each tile _before_ that tile has been configured by the observation pipeline (and saved in the [configured_tiles](configured_tiles.md) table).

Note that because this table refers to tiles before they've been configured, a tile can have many more than two standard stars and six guide stars. A galaxy may also appear in more than one tile. 

## Columns

- __ID__: Target ID
- __RA__: Right Acension coordinate
- __DEC__: Declination coordinate
- __Re__: Half light radius ($r$-band)
- __z__: Redshift
- __Mstar__: Stellar mass, as $\log_{10}(M_* / M_{\odot})$ 
- __u_mag__: $u$-band magnitude
- __g_mag__: $g$-band magnitude
- __r_mag__: $r$-band magnitude
- __i_mag__: $i$-band magnitude,
- __z_mag__: $z$-band magnitude,
- __GAL_MU_E_R__: $r$-band surface brightness ($\mu$) averaged within $r_e$.
- __Ellipticity_r__: $r$-band ellipticity.
- __RS_member__: Whether the galaxy is a member of its cluster red-sequence. Only applies to targets in a cluster field.
- __r_on_rtwo__: Cluster-centric radius divided by the cluster $r_{200}$ value. Only applies to targets in a cluster field.
- __ClusterName__: Name of the galaxy's cluster. Only applies to targets in a cluster field.
- __ClusterMember__: Whether or not the galaxy is a member of its parent cluster, or a foreground target along the same line of sight. Only applies to targets in a cluster field.
- __GAL_MU_E_U:__ $u$-band surface brightness ($\mu$) averaged within $r_e$.
- __GAL_MU_0_U__: Central $u$-band surface brightness ($\mu$).
- __GAL_MU_E_G__: $g$-band surface brightness ($\mu$) averaged within $r_e$.
- __GAL_MU_0_G__: Central $g$-band surface brightness ($\mu$).
- __GAL_MU_0_R__: Central $r$-band surface brightness ($\mu$).
- __GAL_MU_E_I__: $i$-band surface brightness ($\mu$) averaged within $r_e$.
- __GAL_MU_0_I__: Central $i$-band surface brightness ($\mu$).
- __GAL_MU_E_Z__: $z$-band surface brightness ($\mu$) averaged within $r_e$.
- __GAL_MU_0_Z__: Central $z$-band surface brightness ($\mu$).
- __SersicIndex_r__: $r$-band Sersic index.
- __MassHIpred__: Predicted HI mass.
- __WALLABYflag__: Whether the target is also in the WALLABY survey.
- __Dingoflag__ INTEGER: Whether the target is also in the DINGO survey.
- __g_m_i__: $g - i$ colour.
- __IFU_diam_2Re__: Galaxy diameter divided by Hexabundle diameter at 2$r_e$.
- __GAL_MU_R_at_2Re__: $r$-band surface brightness at 2$r_e$.
- __GAL_MU_R_at_3Re__: $r$-band surface brightness at 3$r_e$
- __MW_analogue__: Whether the target passes the "Milky Way analague" selection critera.
- __EO_wind_galaxy__: Whether the target passes the "Edge-on Winde" selection critera.
- __priority__: Tiling priority.
- __type__: Integer type of the target. 0 for standard stars, 1 for galaxies, 2 for guide stars.
- __y_mag__: $y$-band magnitude.
- __GAIA_g_mag__: Gaia $g$-band magnitude.
- __GAIA_bp_mag__: Gaia $bp$-band magnitude.
- __GAIA_rp_mag__: Gaia $rp$-band magnitude.
- __pmRA__: Gaia Proper motion, in milli-arcseconds per year, in the RA direction
- __pmDEC__: Gaia Proper motion, in milli-arcseconds per year, in the Declination direction.
- __COMPLETED__: Column used and updated by the tiling code- best to ignore.
- __remaining_observations__: Column used and updated by the tiling code- best to ignore.
- __isel__: Column used and updated by the tiling code- best to ignore.
- __MagnetX_noDC__: A very simple (but wrong) attempt to convert RA and DEC to the robot X coordinate. Never use this value!
- __MagnetY_noDC__: A very simple (but wrong) attempt to convert RA and DEC to the robot Y coordinate. Never use this value!
- __tile_number__: Integer value assigned to the tile by the tiling code.
- __tile_centre_RA__: Right Ascension of the centre of the tile this galaxy is assigned to.
- __tile_centre_DEC__: Declination of the centre of the tile this galaxy is assigned to.
- __Filler_Galaxy__: Whether this galaxy is a "filler" for the given tile.
- __Region__: Name of the top level field the target is in. Will be one of "WAVES_N", "WAVES_S" or "Cluster"
- __Field__: The name of the region the target is from, e.g. "H01", "G12", "A0119", etc. 
- __tile_ID__: ID value of the tile. 
- __bad_class__: Whether this object falls into any of the SAMI "bad classes". 0 means a good target.




## SQL

``` sql
CREATE TABLE tiles(
    ID TEXT,
    RA FLOAT,
    DEC FLOAT,
    Re FLOAT,
    z FLOAT,
    Mstar FLOAT,
    u_mag FLOAT,
    g_mag FLOAT,
    r_mag FLOAT,
    i_mag FLOAT,
    z_mag FLOAT,
    GAL_MU_E_R FLOAT,
    Ellipticity_r FLOAT,
    RS_member INTEGER,
    r_on_rtwo FLOAT,
    ClusterName TEXT,
    ClusterMember INTEGER,
    GAL_MU_E_U FLOAT,
    GAL_MU_0_U FLOAT,
    GAL_MU_E_G FLOAT,
    GAL_MU_0_G FLOAT,
    GAL_MU_0_R FLOAT,
    GAL_MU_E_I FLOAT,
    GAL_MU_0_I FLOAT,
    GAL_MU_E_Z FLOAT,
    GAL_MU_0_Z FLOAT,
    SersicIndex_r FLOAT,
    MassHIpred FLOAT,
    WALLABYflag INTEGER,
    Dingoflag INTEGER,
    g_m_i FLOAT,
    IFU_diam_2Re FLOAT,
    GAL_MU_R_at_2Re FLOAT,
    GAL_MU_R_at_3Re FLOAT,
    MW_analogue INTEGER,
    EO_wind_galaxy INTEGER,
    priority INTEGER,
    N_observations_to_complete INTEGER,
    type INTEGER,
    y_mag FLOAT,
    GAIA_g_mag FLOAT,
    GAIA_bp_mag FLOAT,
    GAIA_rp_mag FLOAT,
    pmRA FLOAT,
    pmDEC FLOAT,
    COMPLETED INTEGER,
    remaining_observations INTEGER,
    isel INTEGER,
    MagnetX_noDC FLOAT,
    MagnetY_noDC FLOAT,
    tile_number FLOAT,
    tile_centre_RA FLOAT,
    tile_centre_DEC FLOAT,
    Filler_Galaxy INTEGER,
    region TEXT,
    field TEXT,
    tile_ID TEXT,
    bad_class TEXT
)
```

## Example rows

|    | ID               |      RA |       DEC |      Re |         z |   Mstar |   u_mag |   g_mag |   r_mag |   i_mag |   z_mag |   GAL_MU_E_R |   Ellipticity_r |   RS_member |   r_on_rtwo | ClusterName   |   ClusterMember | GAL_MU_E_U   | GAL_MU_0_U   | GAL_MU_E_G   | GAL_MU_0_G   | GAL_MU_0_R   | GAL_MU_E_I   | GAL_MU_0_I   | GAL_MU_E_Z   | GAL_MU_0_Z   | SersicIndex_r   | MassHIpred   | WALLABYflag   | Dingoflag   |    g_m_i |   IFU_diam_2Re | GAL_MU_R_at_2Re   | GAL_MU_R_at_3Re   |   MW_analogue |   EO_wind_galaxy |   priority |   N_observations_to_complete |   type |   y_mag |   GAIA_g_mag |   GAIA_bp_mag |   GAIA_rp_mag |   pmRA |   pmDEC |   COMPLETED |   remaining_observations |   isel |   MagnetX_noDC |   MagnetY_noDC |   tile_number |   tile_centre_RA |   tile_centre_DEC |   Filler_Galaxy | region   | field   | tile_ID     | bad_class   |
|---:|:-----------------|--------:|----------:|--------:|----------:|--------:|--------:|--------:|--------:|--------:|--------:|-------------:|----------------:|------------:|------------:|:--------------|----------------:|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:----------------|:-------------|:--------------|:------------|---------:|---------------:|:------------------|:------------------|--------------:|-----------------:|-----------:|-----------------------------:|-------:|--------:|-------------:|--------------:|--------------:|-------:|--------:|------------:|-------------------------:|-------:|---------------:|---------------:|--------------:|-----------------:|------------------:|----------------:|:---------|:--------|:------------|:------------|
|  0 | C901032178309088 | 13.9938 | -1.39983  | 3.5271  | 0.0432676 | 8.90158 | 21.682  | 19.7581 | 18.9997 | 18.7863 | 18.4773 |      22.9797 |          -99999 |           1 |    0.249189 | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.971775 |       14.1084  |                   |                   |             0 |                0 |          8 |                            3 |      1 |       0 |            0 |             0 |             0 |      0 |       0 |           0 |                        3 |      9 |       -41919.5 |       -42211.6 |             0 |          14.1792 |          -1.21305 |               0 | A0119    | Cluster | A0119_00000 |             |
|  1 | C901032610605729 | 14.6478 | -0.763664 | 1.86014 | 0.0439384 | 8.96826 | 21.2143 | 19.9089 | 19.1189 | 18.7793 | 18.6023 |      21.7095 |          -99999 |           1 |    1.17006  | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 1.12961  |        7.44054 |                   |                   |             0 |                0 |          8 |                            3 |      1 |       0 |            0 |             0 |             0 |      0 |       0 |           0 |                        3 |      9 |       105889   |       101561   |             0 |          14.1792 |          -1.21305 |               0 | A0119    | Cluster | A0119_00000 |             |
|  2 | C901032322101669 | 13.299  | -1.34657  | 2.42613 | 0.0452274 | 9.48658 | 19.3702 | 18.0423 | 17.4211 | 17.1349 | 16.986  |      20.5885 |          -99999 |           0 |    1.18942  | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.907358 |        9.70454 |                   |                   |             0 |                0 |          8 |                            3 |      1 |       0 |            0 |             0 |             0 |      0 |       0 |           0 |                        3 |      9 |      -198925   |       -30175.9 |             0 |          14.1792 |          -1.21305 |               0 | A0119    | Cluster | A0119_00000 |             |
|  3 | C901032178500697 | 14.2646 | -1.4119   | 1.89099 | 0.0427054 | 9.36869 | 20.3163 | 18.9655 | 18.1655 | 17.782  | 17.5939 |      20.7918 |          -99999 |           1 |    0.387329 | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 1.18349  |        7.56396 |                   |                   |             0 |                0 |          8 |                            3 |      1 |       0 |            0 |             0 |             0 |      0 |       0 |           0 |                        3 |      5 |        19283.3 |       -44939.9 |             0 |          14.1792 |          -1.21305 |               0 | A0119    | Cluster | A0119_00000 |             |
|  4 | C901032754505964 | 14.3973 | -0.400905 | 1.90943 | 0.0403539 | 9.04433 | 20.8462 | 19.2946 | 18.6092 | 18.2547 | 18.0909 |      21.2566 |          -99999 |           0 |    1.40884  | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 1.03986  |        7.63772 |                   |                   |             0 |                0 |          8 |                            3 |      1 |       0 |            0 |             0 |             0 |      0 |       0 |           0 |                        3 |      9 |        49275.3 |       183545   |             0 |          14.1792 |          -1.21305 |               0 | A0119    | Cluster | A0119_00000 |             |

