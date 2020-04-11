DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS session;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  session_id INTEGER,
  is_authenticated BOOLEAN,
  is_active BOOLEAN,
  is_anonymous BOOLEAN,
  wins INTEGER,
  losses INTEGER
);

CREATE TABLE session (
  id INTEGER,
  PRIMARY KEY (id)
);
