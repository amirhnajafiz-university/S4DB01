CREATE TABLE comment (
	rate int,
	user_comment varchar(1024),
	username varchar(50),
	movie_id int,
	PRIMARY KEY (username, movie_id),
	FOREIGN KEY (username) REFERENCES "user".username,
	FOREIGN KEY (movie_id) REFERENCES "movie".movie_id
);