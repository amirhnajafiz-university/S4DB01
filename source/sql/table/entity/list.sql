CREATE TABLE "list" (
	list_id int,
	username varchar(50) NOT NULL,
	name varchar(1024) NOT NULL,
	description varchar(1024),
	PRIMARY KEY (list_id),
	FOREIGN KEY (username) REFERENCES "user" (username) ON DELETE CASCADE
);