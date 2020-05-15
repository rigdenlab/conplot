CREATE EXTENSION pgcrypto;
CREATE TABLE user_data (id serial primary key, username varchar(15) not null unique, email varchar(65) not null unique, password text not null);
CREATE TABLE session_data (id serial primary key, user_id int references user_data(id), sequence bit varying, contact bit varying, membrane bit varying, secondarystructure bit varying, custom bit varying, disorder bit varying, conservation bit varying, date date not null default current_date)
