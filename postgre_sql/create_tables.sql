CREATE EXTENSION pgcrypto;
CREATE TABLE user_data
(
    id           serial primary key,
    username     varchar(15) not null unique,
    email        varchar(65) unique,
    password     text        not null,
    created_date date        not null,
    last_login   date        not null
);
CREATE TABLE session_data
(
    id                 serial primary key,
    owner_username     int references user_data (id),
    sequence           bit varying,
    contact            bit varying,
    membrane           bit varying,
    secondarystructure bit varying,
    custom             bit varying,
    disorder           bit varying,
    conservation       bit varying,
    date               date not null default current_date
)
