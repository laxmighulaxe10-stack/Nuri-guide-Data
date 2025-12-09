CREATE DATABASE nuriguide;

USE nuriguide;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    height FLOAT,
    weight FLOAT,
    gender VARCHAR(10),
    bmi FLOAT,
    disease VARCHAR(50)
);
