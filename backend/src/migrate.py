from loguru import logger
import os
import psycopg2

POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
if not POSTGRES_PASSWORD:
    raise RuntimeError("PostgreSQL password not found in environment variables.")

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password=POSTGRES_PASSWORD,
    host="database",
    port="5432",
)

cur = conn.cursor()


# Homegrown DB migrations - these should be IDEMPOTENT statements
# These statements will be run before the database starts up
migrations: list[str] = [
    # Create users table
    """
    CREATE TABLE IF NOT EXISTS test (
        field1 TEXT
    );
    """,
]


for script in migrations:
    try:
        cur.execute(script)
    except psycopg2.DatabaseError as e:
        logger.error(f"Error executing migration script: {e}")
        conn.rollback()
        raise e
conn.commit()

logger.info(f"Executed {len(migrations)} migrations")
