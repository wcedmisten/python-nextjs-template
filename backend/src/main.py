from time import sleep
from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
import os

POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]

con = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password=POSTGRES_PASSWORD,
    host="database",
    port="5432",
)

cur = con.cursor()

# DB model
class Test(BaseModel):
    field_1: str

app = FastAPI()


async def get_tests():
    cur.execute("SELECT * FROM test;")
    rows = cur.fetchall()

    return list(
        [{"field_1": row[0]} for row in rows]
    )

async def post_test(test: Test):
    sleep(2)
    cur.execute(
        "INSERT INTO test VALUES(%s)",
        (
            test.field_1,
        ),
    )
    con.commit()

@app.get("/tests", response_model=list[Test])
async def read_user_details():
    return await get_tests()

@app.post("/test")
async def put_user_details(test: Test):
    return await post_test(test)
