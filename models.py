from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your database model here
class Tree(db.Model):
    id = db.Column(db.integer, primary_key=True)
    common_name = db.Column(db.integer, primary_key=True)
    scientific_name = db.Column(db.integer, primary_key=True)
    genus = db.Column(db.integer, primary_key=True)
    species = db.Column(db.integer, primary_key=True)
    habitat_conditions = db.Column(db.integer, primary_key=True)
    latitide_range  = db.Column(db.integer, primary_key=True)
    population_level = db.Column(db.integer, primary_key=True)
    max_age = db.Column(db.integer, primary_key=True)
    


