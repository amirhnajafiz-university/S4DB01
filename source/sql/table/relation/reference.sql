CREATE TABLE "reference" (
	username varchar(50),
	reference varchar(50) NOT NULL,
	PRIMARY KEY (username),
	FOREIGN KEY (username) REFERENCES "user".username,
	FOREIGN KEY (reference) REFERENCES "user".username,
);