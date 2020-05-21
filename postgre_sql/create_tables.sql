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
    owner_username     varchar(25) references user_data (username),
    session_name       varchar(25)   not null,
    sequence           bytea,
    contact            bytea,
    membranetopology   bytea,
    secondarystructure bytea,
    conservation       bytea,
    disorder           bytea,
    custom             bytea,
    shared_with        varchar(25)[] not null default '{}',
    created_date       date          not null default current_date,
    last_access_date   date          not null default current_date
)