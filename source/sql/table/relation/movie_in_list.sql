CREATE TABLE "movie_in_list" (
	movie_id int,
	list_id int,
	PRIMARY KEY (movie_id, list_id),
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id),
	FOREIGN KEY (list_id) REFERENCES "list" (list_id)
);