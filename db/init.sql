CREATE DATABASE MSCI;
USE MSCI;

CREATE TABLE Users(
userId INTEGER AUTO_INCREMENT,
userName VARCHAR(40),
userPassword VARCHAR(40),
PRIMARY KEY (userId)
);