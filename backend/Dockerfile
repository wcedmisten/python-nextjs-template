FROM python:3.11.4-slim

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./src /backend/app

# Start the application using gunicorn with uvicorn worker
# -w 4: number of workers
# -k uvicorn.workers.UvicornWorker: worker class
CMD [ "/bin/bash", "-c", "python3 /backend/app/migrate.py && gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:4000"]
