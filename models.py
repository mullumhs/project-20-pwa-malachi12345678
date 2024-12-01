from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    common_name = db.Column(db.String(100), nullable = False)
    genus = db.Column(db.String(100), nullable = False)
    species = db.Column(db.String(100), nullable = False)
    scientific_name = db.Column(db.String(100), nullable = True)
    habitat_biome = db.Column(db.String(100), nullable = True)
    lifespan = db.Column(db.Integer, nullable = True)
    height = db.Column(db.String(100), nullable = True)
    image = db.Column(db.String(100), nullable = True)
    additional_info = db.Column(db.String(300), nullable = True)


