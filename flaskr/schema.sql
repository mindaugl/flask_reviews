CREATE TABLE IF NOT EXISTS books (
  id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  title varchar(200) NOT NULL,
  author varchar(100) NOT NULL,
  rating real NOT NULL,
  reviews integer NOT NULL,
  publication_year integer NOT NULL
);