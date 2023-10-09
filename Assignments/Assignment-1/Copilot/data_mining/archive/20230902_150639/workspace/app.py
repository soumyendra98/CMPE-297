from flask import Flask, render_template, request
from user import User
from recipe_recommender import RecipeRecommender

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        dietary_preferences = request.form.get('dietary_preferences')
        cooking_skills = request.form.get('cooking_skills')
        available_ingredients = request.form.get('available_ingredients').split(',')

        user = User(name, dietary_preferences, cooking_skills, available_ingredients)
        recommender = RecipeRecommender(user)
        recipes = recommender.get_recipes()

        return render_template('index.html', recipes=recipes)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
