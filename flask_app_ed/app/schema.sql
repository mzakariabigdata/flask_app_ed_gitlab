-- Initialize the database.
-- Drop any existing data and create empty tables.

-- DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL
-- );

CREATE TABLE book (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title INTEGER NOT NULL,
  author TEXT NOT NULL
);
