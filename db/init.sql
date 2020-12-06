CREATE DATABASE MSCI;
USE MSCI;

CREATE TABLE Users(
userId INTEGER AUTO_INCREMENT,
userName VARCHAR(40),
userPassword VARCHAR(40),
bestTime TIME DEFAULT NULL,
PRIMARY KEY (userId)
);

CREATE TABLE UserArtist(
userId INTEGER,
artist VARCHAR(40),
PRIMARY KEY (userId, artist),
FOREIGN KEY (userId) references Users(userId)
);