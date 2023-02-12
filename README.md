# python-nextjs-template

This is a minimal template for running a full stack webapp with
docker-compose, Python FastAPI, NextJS, and PostgreSQL.

This will set up a small webapp that retrieves and inserts `test` items
stored in PostgreSQL through a Python API.

For more details on the tools used, see:

* https://fastapi.tiangolo.com/
* https://nextjs.org/
* https://www.postgresql.org/

# Screenshots

![frontend](/screenshots/frontend.png)

# Getting started

Create a postgres password in the `.env` file used by docker compose:

```bash
echo "POSTGRES_PASSWORD=$(echo $RANDOM | md5sum | head -c 30)" > .env
```

Back this up somewhere

Make the directory for the postgres data:
```bash
mkdir postgres_data
```

Local Development (allows for updated changes on page refresh)

```bash
docker compose -f docker-compose-dev.yml up
```

Go to http://localhost:8080

Production Deployment

```bash
docker compose up
```
