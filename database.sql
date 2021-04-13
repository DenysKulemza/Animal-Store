DROP DATABASE animal_store;

CREATE DATABASE IF NOT EXISTS animal_store;

CREATE TABLE animal_store.users (
    id INT NOT NULL PRIMARY KEY,
    login VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255),
    address VARCHAR(255)
);


CREATE TABLE animal_store.centers (
    address VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

CREATE TABLE animal_store.specie (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    price FLOAT
);

CREATE TABLE animal_store.stuff_type (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE animal_store.stuff (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    stuff_type_id INT REFERENCES animal_store.stuff_type(id),
    description VARCHAR(255),
    price FLOAT
);

CREATE TABLE animal_store.review (
    id INT NOT NULL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    comment VARCHAR(255) NOT NULL
);

CREATE TABLE animal_store.animals(
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    center_address VARCHAR(255) REFERENCES animal_store.centers(address),
    stuff_type_id INT REFERENCES animal_store.stuff_type(id),
    description VARCHAR(255),
    price FLOAT

);

