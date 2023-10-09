from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from recommendation_system import get_recommendations

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from models import User, Recipe

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], dietary_preference=data['dietary_preference'], cooking_skill_level=data['cooking_skill_level'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created!'})

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.to_dict())

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    user.update(data)
    db.session.commit()
    return jsonify({'message': 'User updated!'})

@app.route('/user/<int:user_id>/recommendations', methods=['GET'])
def get_recommendations_for_user(user_id):
    user = User.query.get(user_id)
    recommendations = get_recommendations(user)
    return jsonify([recipe.to_dict() for recipe in recommendations])

if __name__ == '__main__':
    app.run(debug=True)
