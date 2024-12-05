from flask import render_template, request, redirect, url_for, flash
from models import db, Tree # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):

    @app.route('/', methods=['GET'])
    def get_items():
        trees = Tree.query.all()
        return render_template('index.html', trees = trees)



    @app.route('/add', methods=['POST'])
    def create_item():
        tree = Tree(
            common_name = request.form("common_name"),
            genus = request.form("genus"),
            species = request.form("species"),
            scientific_name = request.form("scientific_name"),
            habitat_biome = request.form("habitat_biome"),
            lifespan = request.form("lifespan"),
            height = request.form("height"),
            image = request.form("image"),
            additional_info = request.form("additional_info")
        )
        db.session.add(tree)
        db.session.commit()
        # This route should handle adding a new item to the database.
        #return redirect(url_for('get_items'))
        return render_template('index.html', message='Item added successfully')



    @app.route('/update', methods=['POST'])
    def update_item():
        # This route should handle updating an existing item identified by the given ID.
        return render_template('index.html', message=f'Item updated successfully')



    @app.route('/delete', methods=['POST'])
    def delete_item():
        # This route should handle deleting an existing item identified by the given ID.
        return render_template('index.html', message=f'Item deleted successfully')