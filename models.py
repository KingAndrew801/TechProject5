from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)

tree = "Pine"
season = "winter"


def tree_talk(t, s):
    tree = t
    season = s
    print("I love {} trees in {}".format(tree, season))

class Project(db.Model):
    id = db.Column('Id', db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.DateTime, default=datetime.datetime.now)
    desc = db.Column('Description', db.Text())
    skills = db.Column('Skills', db.String())
    github = db.Column("Git", db.String())

    def __repr__(self):
        return f'''Project: {self.title}
                Skills: {self.skills}'''



    tree_talk(tree, season)
    tree_talk("Palm", "summer")
    tree_talk(tree, season)