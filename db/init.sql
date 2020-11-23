CREATE DATABASE MSCI;
USE MSCI;

CREATE TABLE Users(
userId INTEGER AUTO_INCREMENT,
userName VARCHAR(40),
userPassword VARCHAR(40),
bestTime VARCHAR(10) DEFAULT "00:00:00",
PRIMARY KEY (userId)
);

CREATE TABLE UserArtist(
userId INTEGER,
artist VARCHAR(40),
PRIMARY KEY (userId, artist),
FOREIGN KEY (userId) references Users(userId)
);