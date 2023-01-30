CREATE SCHEMA IF NOT EXISTS shortner_srv;
GRANT USAGE ON SCHEMA shortner_srv TO shortner_user;

create table shortner_srv.shortlink
(
    id          varchar(40) not null primary key,
    short_link  varchar(30) not null unique,
    usual_link  varchar(4096),
    modified_on timestamp,
    valid_up_to timestamp
);
