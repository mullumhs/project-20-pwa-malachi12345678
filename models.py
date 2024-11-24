from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True,)
    common_name = db.Column(db.String(100), nullable = False)
    scientific_name = db.Column(db.String(100), nullable = True)
    genus = db.Column(db.String(100), nullable = False)
    species = db.Column(db.String(100), nullable = False)
    habitat_conditions = db.Column(db.String(100), nullable = True)
    latitide_range = db.Column(db.String(100), nullable = True)
    population_level = db.Column(db.String(100), nullable = True)
    lifespan = db.Column(db.Integer, nullable = True)
    max_size = db.Column(db.String(100), nullable = True)
    more_info = db.Column(db.String(300), nullable = True)


