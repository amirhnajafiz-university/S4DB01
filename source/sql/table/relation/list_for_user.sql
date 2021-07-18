CREATE TABLE 'list_for_user' as (
	username varchar(50),
	list_id int,
	PRIMARY KEY (username, list_id),
	FOREIGN KEY username REFERENCES ('user'.username),
	FOREIGN KEY list_id REFERENCES ('list'.list_id)
);