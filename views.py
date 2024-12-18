from flask import render_template, request, redirect, url_for, flash
from models import db, Tree # Also import your database model here

# Define your routes inside the 'init_routes' function
# Feel free to rename the routes and functions as you see fit
# You may need to use multiple methods such as POST and GET for each route
# You can use render_template or redirect as appropriate
# You can also use flash for displaying status messages

def init_routes(app):
    #route for home page
    @app.route('/', methods=['GET'])
    def get_items():

        search_query = request.args.get('query')

        

        if search_query:
            # If there's a search query, filter the results
            trees = Tree.query.filter(Tree.common_name.ilike(f'%{search_query}%')).all()

        else:
            # If no search query, return all items
            trees = Tree.query.all()

        return render_template('index.html', trees = trees)


        #route for individual tree display
    @app.route('/display', methods=['GET'])
    def get_item():  
        id = request.args.get("id")
        tree = Tree.query.get(id)
        return render_template('display.html', tree = tree)
    

    #route for add tree form
    @app.route('/add', methods=['POST'])
    def create_item():
        tree = Tree(
            common_name = request.form["common_name"],
            genus = request.form["genus"],
            species = request.form["species"],
            scientific_name = request.form["scientific_name"],
            habitat_biome = request.form["habitat_biome"],
            lifespan = request.form["lifespan"],
            height = request.form["height"],
            image = request.form["image"],
            additional_info = request.form["additional_info"]
        )
        db.session.add(tree)
        db.session.commit()
        # This route should handle adding a new item to the database. 
        return redirect(url_for('get_items'))

        #route for edit form
    @app.route('/update', methods=['POST'])
    def update_item():

        if request.method == 'POST':
            id = request.form['id']
            tree = Tree.query.get(id)
            tree.common_name = request.form["common_name"]
            tree.genus = request.form["genus"]
            tree.species = request.form["species"]
            tree.scientific_name = request.form["scientific_name"]
            tree.habitat_biome = request.form["habitat_biome"]
            tree.lifespan = request.form["lifespan"]
            tree.height = request.form["height"]
            tree.image = request.form["image"]
            tree.additional_info = request.form["additional_info"]
            db.session.add(tree)
            db.session.commit()
            return redirect(url_for('get_items'))
        
            #route for getting id for edit form
    @app.route('/edit', methods=['GET'])
    def edit_item():   
         # This route should handle updating an existing item identified by the given ID.
        id = request.args.get("id")
        tree = Tree.query.get(id)
        return render_template('edit.html', tree = tree)
       
        #route for delete
    @app.route('/delete', methods=['GET'])
    def delete_item():
        id = request.args.get("id")
        tree = Tree.query.get(id)
        db.session.delete(tree)
        db.session.commit()
        # This route should handle deleting an existing item identified by the given ID.
        return redirect(url_for('get_items'))
    