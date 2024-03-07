"""
This script creates various tables and views to do with Hector observations.
They are:
* observing_runs (table): A list of the start/end dates of every observing run
* observers (table): A list of observers, with their names and affiliations
* observers_observing_runs (table): Who gets assigned to each observing run
* observed_tiles (table): The Hector tiles we've successfully observed.
* nights_observed_per_person (view): The number of nights each team member has completed.
* tiles_observed_per_person (view): The number of tiles each team member has observed.
* master_observer_summary (view): A combined view of summary statistics for each observer.
* tiles_per_observing_run (view): A view of the tiles observed per observing run
* master_survey_summary (view): A combined view of summary statistics for each observing run
"""

import pandas as pd
import sqlite3

conn = sqlite3.connect("hector.db")
cur = conn.cursor()
cur.executescript(
    """
    DROP TABLE IF EXISTS observing_runs;
    DROP TABLE IF EXISTS observers;
    DROP TABLE IF EXISTS observers_observing_runs;
    DROP TABLE IF EXISTS observed_tiles;
    DROP VIEW IF EXISTS tiles_observed_per_person;
    DROP VIEW IF EXISTS nights_observed_per_person;
    DROP VIEW IF EXISTS master_observer_summary;
    DROP VIEW IF EXISTS tiles_per_observing_run;
    DROP VIEW IF EXISTS master_survey_summary;
    """
)

observing_runs = pd.read_csv(
    "CSV_files_to_update/observing_runs.csv", parse_dates=[1, 2]
)
# Create the observing runs table
observing_runs_sql = """
CREATE TABLE IF NOT EXISTS observing_runs (
    run_id TEXT PRIMARY KEY,
    start_date TEXT,
    end_date TEXT
);
"""

cur.executescript(observing_runs_sql)
observing_runs.to_sql("observing_runs", conn, if_exists="append", index=False)


# create the observers table
observers = pd.read_csv("CSV_files_to_update/observers.csv")
observers_sql = """
CREATE TABLE IF NOT EXISTS observers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    observer_ID TEXT,
    first_name TEXT,
    last_name TEXT,
    affiliation TEXT
);
"""
cur = conn.cursor()
cur.executescript(observers_sql)
observers.to_sql("observers", conn, if_exists="append", index=True, index_label="id")


# Create the join
observers_observing_runs = pd.read_csv(
    "CSV_files_to_update/observers_observing_runs.csv"
)
observers_observing_runs_sql = """
CREATE TABLE IF NOT EXISTS observers_observing_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    [run_id] TEXT NOT NULL,
    [observer_id] TEXT NOT NULL,
    FOREIGN KEY ([run_id]) REFERENCES "observing_runs" ([run_id])
                ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([observer_id]) REFERENCES "observers" ([observer_id])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
"""
cur = conn.cursor()
cur.executescript(observers_observing_runs_sql)
observers_observing_runs.to_sql(
    "observers_observing_runs", conn, if_exists="append", index_label="id"
)

# Create the Observed tiles table
# TODO: make the tile_id a foreign key for the tile table
observations = pd.read_csv("CSV_files_to_update/observed_tiles.csv")
observations_sql = """
CREATE TABLE IF NOT EXISTS observed_tiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    [tile_ID] TEXT NOT NULL,
    [run_ID] TEXT NOT NULL,
    FOREIGN KEY ([run_id]) REFERENCES "observing_runs" ([run_ID])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
"""
cur = conn.cursor()
cur.executescript(observations_sql)
observations.to_sql("observed_tiles", conn, if_exists="append", index_label="id")


# Some example queries

# # Who's gone on an observing run to date?
# pd.read_sql(
#     """
#             SELECT observers.first_name, observers.last_name
#             FROM observers
#             JOIN observers_observing_runs
#                 ON observers.observer_ID = observers_observing_runs.observer_ID
#             JOIN observing_runs
#                 ON observers_observing_runs.run_ID = observing_runs.run_ID
#             WHERE observing_runs.start_date < date('now')
#             """,
#     conn,
# )

# Count up all the tiles finished by everyone
cur.executescript(
    """CREATE VIEW tiles_observed_per_person
            AS
            SELECT observers.observer_ID, observers.first_name, observers.last_name, COUNT(tile_ID) as N_tiles_observed
            FROM observers
            JOIN observers_observing_runs
                ON observers.observer_ID = observers_observing_runs.observer_id
            JOIN observing_runs
                ON observers_observing_runs.run_ID = observing_runs.run_ID
            JOIN observed_tiles
                ON observed_tiles.run_ID = observers_observing_runs.run_ID
            WHERE observing_runs.start_date < date('now')
            GROUP BY observers.observer_id
            ORDER BY N_tiles_observed DESC;
            """
)

cur.executescript(
    """
    CREATE VIEW nights_observed_per_person
    AS
    SELECT observers.observer_ID, observers.first_name, observers.last_name, CAST(SUM(JULIANDAY(end_date) - JULIANDAY(start_date)) as integer) as N_nights_observed
    FROM observers
    JOIN observers_observing_runs
        ON observers.observer_ID = observers_observing_runs.observer_id
    JOIN observing_runs
        ON observers_observing_runs.run_ID = observing_runs.run_ID
    WHERE observing_runs.start_date < date('now')
    GROUP BY observers.observer_id
    ORDER BY N_nights_observed DESC;
    """,
)

cur.executescript(
    """
    CREATE VIEW master_observer_summary
    AS
    SELECT nights_observed_per_person.first_name, nights_observed_per_person.last_name, N_nights_observed, N_tiles_Observed
    FROM nights_observed_per_person
    JOIN tiles_observed_per_person
        ON tiles_observed_per_person.observer_ID = nights_observed_per_person.observer_ID
    """
)

cur.execute(
    """
    CREATE VIEW tiles_per_observing_run
    AS
    SELECT observing_runs.run_ID, start_date, end_date, COUNT(observing_runs.run_ID) as N_tiles_observed
    from observing_runs
    JOIN observed_tiles
        ON observing_runs.run_ID = observed_tiles.run_ID
    GROUP BY observing_runs.run_ID
    """
)

cur.execute(
    """
    CREATE VIEW master_survey_summary
    AS
    SELECT run_ID, N_tiles_observed, CAST(JULIANDAY(end_date) - JULIANDAY(start_date) as integer) as N_nights, N_tiles_observed / (JULIANDAY(end_date) - JULIANDAY(start_date)) as tiles_per_night
    from tiles_per_observing_run
    """
)
