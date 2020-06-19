CREATE EXTENSION pgcrypto;

CREATE TABLE user_data
(
    id           serial primary key,
    username     varchar(25) not null unique,
    email        varchar(65) unique,
    password     text        not null,
    created_date date        not null default current_date,
    last_login   date        not null default current_date
);
CREATE TABLE session_data
(
    primary key (owner_username, session_name),
    owner_username   varchar(25) references user_data (username),
    session_name     varchar(25)   not null,
    session_json     json          not null,
    shared_with      varchar(25)[] not null default '{}',
    created_date     date          not null default current_date,
    last_access_date date          not null default current_date,
    session_pkid     serial        not null unique
)