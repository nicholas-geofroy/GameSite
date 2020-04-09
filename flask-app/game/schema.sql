DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS session;
DROP TABLE IF EXISTS in_session;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  wins INTEGER,
  losses INTEGER
);

CREATE TABLE session (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  host_id INTEGER,
  FOREIGN KEY (host_id) REFERENCES user (id)
);

CREATE TABLE in_session (
  session_id INTEGER,
  user_id INTEGER,
  FOREIGN KEY (session_id) REFERENCES session (id),
  FOREIGN KEY (user_id) REFERENCES user(id)
);
