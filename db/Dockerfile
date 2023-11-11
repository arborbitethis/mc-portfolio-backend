FROM postgres:12 as db
WORKDIR /app
COPY ./db-scripts/init.sh /docker-entrypoint-initdb.d
COPY ./db-scripts/seed.sql ./scripts/db/seed.sql
