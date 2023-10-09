from flask import Flask, render_template, request
from user import User
from recipe import Recipe
from recommender import Recommender

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # Update user profile
        pass
    return render_template('profile.html')

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        # Update ingredient inventory
        pass
    return render_template('inventory.html')

@app.route('/recommendations')
def recommendations():
    # Get recipe recommendations
    pass

if __name__ == '__main__':
    app.run(debug=True)
