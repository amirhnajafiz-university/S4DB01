CREATE TABLE "movie_tag" (
	tag_id int,
	movie_id int,
	PRIMARY KEY (tag_id, movie_id),
	FOREIGN KEY (tag_id) REFERENCES "tag" (tag_id) ON DELETE CASCADE,
	FOREIGN KEY (movie_id) REFERENCES "movie" (movie_id) ON DELETE CASCADE
);