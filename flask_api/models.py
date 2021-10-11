from flask import app
from flask_api.__init__ import db

class VideoModel(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer(), nullable=False)
    views = db.Column(db.Integer(), nullable=False)