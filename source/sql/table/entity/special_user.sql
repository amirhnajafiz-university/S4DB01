CREATE TABLE "special_user" (
	pro_id int,
	username varchar(50) NOT NULL,
	expiredate date NOT NULL,
	PRIMARY KEY (pro_id),
	FOREIGN KEY (username) REFERENCES "user" (username) ON DELETE CASCADE
);