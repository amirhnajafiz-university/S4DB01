CREATE TABLE "user" (
	username varchar(50),
	password varchar(50) NOT NULL,
	name varchar(50) NOT NULL,
	email varchar(50) NOT NULL,
	phonenumber varchar(50),
	nationalID varchar(10) UNIQUE,
	wallet int DEFAULT 0,
	point int DEFAULT 0,
	PRIMARY KEY (username)
);