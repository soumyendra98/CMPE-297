from flask import Flask, request, jsonify
from recipe import Recipe, get_recipes

app = Flask(__name__)

@app.route('/get_recipes', methods=['POST'])
def get_recipe_recommendations():
    data = request.get_json()
    ingredients = data['ingredients']
    category = data['category']
    recipes = get_recipes(ingredients, category)
    return jsonify([recipe.to_dict() for recipe in recipes])

if __name__ == '__main__':
    app.run(debug=True)
