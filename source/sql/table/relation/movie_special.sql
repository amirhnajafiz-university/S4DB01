CREATE TABLE 'movie_special' as (
	special_id int,
	movie_id int,
	PRIMARY KEY (special_id, movie_id),
	FOREIGN KEY special_id REFERENCES ('special_movie'.movie_id),
	FOREIGN KEY movie_id REFERENCES ('movie'.movie_id)
);