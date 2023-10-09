from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-recipes', methods=['POST'])
def get_recipes():
    data = json.loads(request.data)
    ingredients = data.get('ingredients')
    # Here we should implement the logic to get the recipes based on the ingredients
    # For now, let's just return the ingredients as a JSON response
    return jsonify(ingredients)

if __name__ == '__main__':
    app.run(debug=True)
