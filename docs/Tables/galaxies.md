# galaxies

This table is the master collection of galaxy properties across every region in the Hector Survey.

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
- __N_observations_to_complete__: Number of observations to complete this target.
- __bad_class__: Whether this object falls into any of the SAMI "bad classes". 0 means a good target.
- __Field__: Name of the top level field the target is in. Will be one of "WAVES_N", "WAVES_S" or "Cluster"
- __Region__: The name of the region the target is from, e.g. "H01", "G12", "A0119", etc. 

## SQL 

```SQL
CREATE TABLE IF NOT EXISTS galaxies(
    ID TEXT PRIMARY KEY,
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
    bad_class INTEGER,
    Field TEXT,
    Region TEXT,
    FOREIGN KEY ([ID]) REFERENCES "targets" ([ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
    )
```

## Example Rows

|    | ID               |      RA |       DEC |      Re |         z |    Mstar |   u_mag |   g_mag |   r_mag |   i_mag |   z_mag |   GAL_MU_E_R |   Ellipticity_r |   RS_member |   r_on_rtwo | ClusterName   |   ClusterMember | GAL_MU_E_U   | GAL_MU_0_U   | GAL_MU_E_G   | GAL_MU_0_G   | GAL_MU_0_R   | GAL_MU_E_I   | GAL_MU_0_I   | GAL_MU_E_Z   | GAL_MU_0_Z   | SersicIndex_r   | MassHIpred   | WALLABYflag   | Dingoflag   |    g_m_i |   IFU_diam_2Re | GAL_MU_R_at_2Re   | GAL_MU_R_at_3Re   |   MW_analogue |   EO_wind_galaxy |   priority |   N_observations_to_complete |   bad_class | Field   | Region   |
|---:|:-----------------|--------:|----------:|--------:|----------:|---------:|--------:|--------:|--------:|--------:|--------:|-------------:|----------------:|------------:|------------:|:--------------|----------------:|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:----------------|:-------------|:--------------|:------------|---------:|---------------:|:------------------|:------------------|--------------:|-----------------:|-----------:|-----------------------------:|------------:|:--------|:---------|
|  0 | C901033186400641 | 14.0174 |  0.261004 | 4.46941 | 0.0458982 | 10.1193  | 17.7857 | 16.4614 | 15.8588 | 15.625  | 15.3929 |      20.353  |          -99999 |           0 |    2.33349  | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.836312 |       17.8776  |                   |                   |             0 |                0 |          4 |                            1 |           0 | Cluster | A0119    |
|  1 | C901032178409951 | 14.241  | -1.55472  | 3.36356 | 0.0429916 |  9.28584 | 19.4497 | 18.5804 | 17.9734 | 17.62   | 17.5009 |      21.8502 |          -99999 |           0 |    0.532294 | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.960463 |       13.4542  |                   |                   |             0 |                0 |          8 |                            3 |           0 | Cluster | A0119    |
|  2 | C901032178603925 | 14.6039 | -1.40148  | 2.16608 | 0.0514648 |  8.7016  | 20.5431 | 19.4204 | 18.9968 | 18.849  | 18.7222 |      21.9181 |          -99999 |           0 |    0.855234 | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.571415 |        8.66434 |                   |                   |             0 |                0 |          8 |                            3 |           0 | Cluster | A0119    |
|  3 | C901033042501675 | 14.2998 |  0.11102  | 3.52956 | 0.0445623 |  9.10708 | 20.5351 | 19.2745 | 18.6075 | 18.2913 | 18.1029 |      22.589  |          -99999 |           0 |    2.1318   | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.983167 |       14.1182  |                   |                   |             0 |                0 |          8 |                            3 |           0 | Cluster | A0119    |
|  4 | C901031602506671 | 14.465  | -2.60234  | 3.18357 | 0.0461423 |  8.61583 | 20.3137 | 19.1043 | 18.8339 | 18.6436 | 18.6632 |      22.5914 |          -99999 |           0 |    2.15996  | A0119         |               1 |              |              |              |              |              |              |              |              |              |                 |              |               |             | 0.460726 |       12.7343  |                   |                   |             0 |                0 |          4 |                            1 |           0 | Cluster | A0119    |