from flask import Flask, render_template, request
from user import User
from recommender import Recommender

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = User(request.form)
        recommender = Recommender(user)
        recommended_recipes = recommender.recommend_recipes()
        return render_template('index.html', recommended_recipes=recommended_recipes)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
