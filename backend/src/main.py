from fastapi import FastAPI
import os
import psycopg2
from pydantic import BaseModel

POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
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

# DB model
class Test(BaseModel):
    field_1: str


app = FastAPI()


async def get_tests() -> list[Test]:
    """
    Get test data from the database.

    Returns:
        list[Test]: A list of Test objects representing the retrieved test data.
    """
    cur.execute("SELECT * FROM test;")
    rows = cur.fetchall()
    return [Test(field_1=row[0]) for row in rows]


async def post_test(test: Test) -> None:
    """
    Insert test data into the database.

    Args:
        test (Test): The Test object to be inserted into the database.

    Returns:
        None
    """
    cur.execute(
        "INSERT INTO test VALUES(%s)",
        (test.field_1,),
    )
    conn.commit()


@app.get("/tests", response_model=list[Test])
async def read_test_details() -> list[Test]:
    """
    Route handler to get test data.

    Returns:
        List[Test]: A list of Test objects representing the retrieved test data.
    """

    return await get_tests()


@app.post("/test")
async def put_test_details(test: Test) -> None:
    """
    Route handler to insert test data.

    Args:
        test (Test): The Test object to be inserted into the database.

    Returns:
        None
    """

    return await post_test(test)
