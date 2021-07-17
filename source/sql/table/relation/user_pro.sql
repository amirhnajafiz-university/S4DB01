CREATE TABLE 'user_pro' as (
	username varchar(50),
	pro_id int,
	PRIMARY KEY (username, pro_id),
	FOREIGN KEY username REFERENCES ('user'.username),
	FOREIGN KEY pro_id REFERENCES ('special_user'.pro_id),
);