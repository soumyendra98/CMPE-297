from flask import Flask, render_template, request
from recipe_recommender import RecipeRecommender

app = Flask(__name__)
recommender = RecipeRecommender()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    ingredients = request.form.get('ingredients')
    dietary_preferences = request.form.get('dietary_preferences')
    skill_level = request.form.get('skill_level')

    recipes = recommender.get_recipes(ingredients, dietary_preferences, skill_level)

    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
