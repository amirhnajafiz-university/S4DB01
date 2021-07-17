CREATE TABLE 'movie' as (
	movie_id int,
	movie_file varchar(1024) NOT NULL,
	name varchar(50) NOT NULL,
	creators varchar(50),
	movie_year int,
	description varchar(50),
	PRIMARY KEY (movie_id)
);