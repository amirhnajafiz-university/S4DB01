CREATE TABLE 'movie_in_list' as (
	username varchar(50),
	list_id int,
	PRIMARY KEY (username, list_id),
	FOREIGN KEY username REFERENCES ('user'.username),
	FOREIGN KEY list_id REFERENCES ('list'.list_id)
);