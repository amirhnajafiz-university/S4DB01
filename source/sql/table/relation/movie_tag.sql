CREATE TABLE 'movie_tag' as (
	tag_id int,
	movie_id int,
	PRIMARY KEY (tag_id, movie_id),
	FOREIGN KEY tag_id REFERENCES ('tag'.tag_id),
	FOREIGN KEY movie_id REFERENCES ('movie'.movie_id)
);