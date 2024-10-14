FROM mysql:8.0

COPY ./migrations/init.sql /docker-entrypoint-initdb.d/
