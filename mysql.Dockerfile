FROM mysql:8.0

ENV MYSQL_ALLOW_EMPTY_PASSWORD=yes
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password
ENV MYSQL_DATABASE=database

COPY ./lab1/sql/init.sql /docker-entrypoint-initdb.d/
