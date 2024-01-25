# observing_runs

This table contains basic information about each Hector observing run.

## Columns

- __run_id__: ID of the observing run.
- __start_date__: First night of observing.
- __end_date__: Last night of observing.

## SQL

``` sql
CREATE TABLE observing_runs (
    run_id TEXT PRIMARY KEY,
    start_date TEXT,
    end_date TEXT
)
```


## Example rows

|    | run_id   | start_date          | end_date            |
|---:|:---------|:--------------------|:--------------------|
|  0 | 2023A_1A | 2023-04-17 00:00:00 | 2023-04-23 00:00:00 |
|  1 | 2023A_1B | 2023-04-24 00:00:00 | 2023-04-30 00:00:00 |
|  2 | 2023A_2A | 2023-06-13 00:00:00 | 2023-06-19 00:00:00 |
|  3 | 2023A_2B | 2023-06-20 00:00:00 | 2023-06-26 00:00:00 |
|  4 | 2023A_3A | 2023-07-10 00:00:00 | 2023-07-16 00:00:00 |