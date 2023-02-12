import os
import psycopg2

POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

con = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password=POSTGRES_PASSWORD,
    host="database",
    port="5432",
)

cur = con.cursor()


# home grown DB migrations these should be IDEMPOTENT statements
# these statements will be run before the database starts up
migrations = [
    # create users table
    "CREATE TABLE IF NOT EXISTS test ("
    "field1 TEXT"
    ");",

    # add default values
    "INSERT INTO test VALUES ('foo');",
    "INSERT INTO test VALUES ('bar');",
]


for script in migrations:
    cur.execute(script)
con.commit()

print("Executed ", len(migrations), " migrations")
