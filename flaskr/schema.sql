-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS figure;
DROP TABLE IF EXISTS skill;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE figure (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  videolink link,
  category TEXT NOT NULL
);

CREATE TABLE skill (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  figure_id INTEGER NOT NULL,
  category TEXT NOT NULL,
  level TEXT,
  FOREIGN KEY (user_id) REFERENCES user (id),
  FOREIGN KEY (figure_id) REFERENCES figure (id)
);
