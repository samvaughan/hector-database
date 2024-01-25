# observers

A list of the Hector team members who have been on at least one observing run.

## Columns

- __id__: 
- __observer_ID__: Unique ID for the Hector obsevrer. 
- __first_name__: First Name
- __last_name__: Last Name
- __affiliation__: University Affiliation


## SQL

```SQL
CREATE TABLE IF NOT EXISTS observers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_ID TEXT,
    first_name TEXT,
    last_name TEXT,
    affiliation TEXT
);
```

## Example rows

|    |   id | observer_ID      | first_name   | last_name   | affiliation   |
|---:|-----:|:-----------------|:-------------|:------------|:--------------|
|  0 |    0 | juliabryant      | Julia        | Bryant      | USyd          |
|  1 |    1 | tomwoodrow       | Thomas       | Woodrow     | ANU           |
|  2 |    2 | tomrutherford    | Thomas       | Rutherford  | USyd          |
|  3 |    3 | susietuntipong   | Susie        | Tuntipong   | USyd          |
|  4 |    4 | stefaniabarsanti | Stefania     | Barsanti    | ANU           |