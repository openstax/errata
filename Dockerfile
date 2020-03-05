FROM postgres:latest
FROM python:3.7.6

ENV PYTHONUNBUFFERED 1

COPY . /code/

WORKDIR /code/

# install requirements
RUN pip install -r requirements/dev.txt

# install psycopg2 library with PIP
RUN pip install psycopg2

# expose Postgres port
EXPOSE 5432

# bind mount Postgres volumes for persistent data
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]


ENTRYPOINT ["/code/docker/entrypoint"]

CMD docker/start