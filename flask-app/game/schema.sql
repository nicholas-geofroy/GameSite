DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS session;
DROP TABLE IF EXISTS inSession;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  wins INTEGER,
  losses INTEGER
);

CREATE TABLE session (
  sessionId TEXT,
  hostId INTEGER,
  PRIMARY KEY (sessionId, hostId)
  FOREIGN KEY (hostID) REFERENCES user (id)
);

CREATE TABLE inSession (
  sessionId TEXT,
  userId INTEGER,
  PRIMARY KEY (sessionId, userId)
  FOREIGN KEY (sessionID) REFERENCES session (id),
  FOREIGN KEY (userId) REFERENCES user(id)
);
