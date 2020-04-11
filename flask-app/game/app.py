from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# create and configure the app

app = Flask(__name__)
database_path = os.path.join(app.instance_path, 'game.sqlite')
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=database_path
)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{database_path}'

db = SQLAlchemy(app)

print(f'db path: {os.path.join(app.instance_path, "game.sqlite")}')
