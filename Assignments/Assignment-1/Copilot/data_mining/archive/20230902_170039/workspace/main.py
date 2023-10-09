from flask import Flask, request, jsonify
from flask_cors import CORS
from user import User
from recipe import Recipe

app = Flask(__name__)
CORS(app)

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()
    user = User(**data['user'])
    ingredients = data['ingredients']
    # TODO: Implement the logic to get recommended recipes based on the user's dietary preferences, available ingredients, and cooking skills.
    recipes = []
    return jsonify([recipe.__dict__ for recipe in recipes])

if __name__ == '__main__':
    app.run(debug=True)
