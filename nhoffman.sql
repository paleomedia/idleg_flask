CREATE TABLE IF NOT EXISTS users (
email VARCHAR(256) NOT NULL,
username VARCHAR(64) NOT NULL PRIMARY KEY,
password VARCHAR(64) NOT NULL,
firstname VARCHAR(64),
lastname VARCHAR(64),
party VARCHAR(12),
website VARCHAR(64),
district_cong TINYINT,
district_leg TINYINT,
registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
verified BOOL
);

CREATE TABLE IF NOT EXISTS comments (
comment_id BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(64),
comment MEDIUMBLOB,
comment_link VARCHAR(200),
comment_type VARCHAR(9),
votes_for TINYINT,
votes_against TINYINT,
flags TINYINT,
bill_id VARCHAR(20),
comment_ip VARCHAR(100),
comment TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
comment_parent BIGINT(20),
approved BOOL
);

CREATE TABLE IF NOT EXISTS topics (
topic_id BIGINT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,
topic VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS bills_topics (
bill_id BIGINT(20),
topic_id BIGINT(20)
);

CREATE TABLE IF NOT EXISTS bills (
bill_id VARCHAR(15) NOT NULL PRIMARY KEY,
year YEAR(4),
title MEDIUMBLOB,
bill_name VARCHAR(6),
votes_for BIGINT(20),
votes_against BIGINT(20)
);

CREATE TABLE IF NOT EXISTS lawmakers (
leg_id VARCHAR(9) NOT NULL PRIMARY KEY,
first_name VARCHAR(32) NOT NULL,
last_name VARCHAR(32) NOT NULL,
middle_name VARCHAR(32),
suffix VARCHAR(8),
nickname VARCHAR(32),
district INT(2),
twitter VARCHAR(64),
facebook VARCHAR(64),
website VARCHAR(64),
party VARCHAR(24),
active BOOL,
chamber VARCHAR(12),
photo_url VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS leg_geo (
district INT(2) PRIMARY KEY,
polygon POLYGON NOT NULL
);

CREATE TABLE IF NOT EXISTS user_bills (
bill_id BIGINT(20),
user_id VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS user_friends (
user_id VARCHAR(64),
friend_id VARCHAR(64)
);

CREATE TABLE IF NOT EXISTS user_topics (
user_id VARCHAR(64),
topic_id BIGINT(20)
);

CREATE TABLE IF NOT EXISTS user_lawmakers (
user_id VARCHAR(64),
lawmaker VARCHAR(9)
);

