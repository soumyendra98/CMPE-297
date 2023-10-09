from flask import Flask, request, jsonify
from recipe import Recipe
from user import User, update_user_ingredients, get_matching_recipes

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user = User(data['dietary_preferences'], data['skill_level'], data['available_ingredients'])
    recipes = [Recipe(**recipe_data) for recipe_data in data['recipes']]
    matching_recipes = get_matching_recipes(user, recipes)
    return jsonify([recipe.__dict__ for recipe in matching_recipes])

@app.route('/update_ingredients', methods=['POST'])
def update_ingredients():
    data = request.get_json()
    user = User(data['dietary_preferences'], data['skill_level'], data['available_ingredients'])
    update_user_ingredients(user, data['new_ingredients'])
    return jsonify(user.__dict__)

if __name__ == '__main__':
    app.run(debug=True)
