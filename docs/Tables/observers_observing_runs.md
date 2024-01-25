# observers_observing_runs

This table has a record of which observers have been present at each observing run.

## Columns

- __id__: Row number
- __run_id__: ID of the observing run
- __observer_id__: ID of the observer

## SQL

``` sql
CREATE TABLE observers_observing_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    [run_id] TEXT NOT NULL,
    [observer_id] TEXT NOT NULL,
    FOREIGN KEY ([run_id]) REFERENCES "observing_runs" ([run_id])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([observer_id]) REFERENCES "observers" ([observer_id])
                ON DELETE NO ACTION ON UPDATE NO ACTION
)
```

## Example rows

|    |   id | run_id   | observer_id      |
|---:|-----:|:---------|:-----------------|
|  0 |    0 | 2023A_1A | juliabryant      |
|  1 |    1 | 2023A_1A | tomwoodrow       |
|  2 |    2 | 2023A_1A | tomrutherford    |
|  3 |    3 | 2023A_1A | susietuntipong   |
|  4 |    4 | 2023A_1B | stefaniabarsanti |

