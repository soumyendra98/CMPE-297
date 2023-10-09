from flask import Flask, render_template, request, redirect, url_for
from database import get_user, update_user, get_recipe, get_all_recipes
from recommender import Recommender
from user import User
from recipe import Recipe

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        user_id = request.form['user_id']
        dietary_preferences = request.form['dietary_preferences']
        available_ingredients = request.form['available_ingredients'].split(',')
        cooking_skills = request.form['cooking_skills']
        user = User(user_id, dietary_preferences, available_ingredients, cooking_skills)
        update_user(user)
        return redirect(url_for('recommendations', user_id=user_id))
    else:
        user_id = request.args.get('user_id')
        user = get_user(user_id)
        return render_template('profile.html', user=user)

@app.route('/recommendations')
def recommendations():
    user_id = request.args.get('user_id')
    user = get_user(user_id)
    recommender = Recommender(get_all_recipes())
    recommended_recipes = recommender.recommend(user)
    return render_template('recommendations.html', recipes=recommended_recipes)

@app.route('/recipe')
def recipe():
    recipe_id = request.args.get('recipe_id')
    recipe = get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
