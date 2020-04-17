DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS session;
DROP TABLE IF EXISTS game;
DROP TABLE IF EXISTS team;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  session_id INTEGER,
  is_authenticated BOOLEAN,
  is_active BOOLEAN,
  is_anonymous BOOLEAN,
  socketio_id TEXT,
  team_id INTEGER,
  wins INTEGER,
  losses INTEGER
);

CREATE TABLE session (
  id INTEGER,
  PRIMARY KEY (id)
);

CREATE TABLE game (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type ENUM,
  num_players INTEGER NOT NULL,
  num_teams INTEGER NOT NULL,
  game_state TEXT
);

CREATE TABLE team (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  game_id INTEGER NOT NULL,
  name TEXT NOT NULL
);
