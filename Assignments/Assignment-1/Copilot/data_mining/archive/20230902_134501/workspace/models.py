from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dietary_preference = db.Column(db.String(50), nullable=False)
    cooking_skill_level = db.Column(db.String(50), nullable=False)
    ingredient_inventory = db.Column(db.PickleType, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'dietary_preference': self.dietary_preference,
            'cooking_skill_level': self.cooking_skill_level,
            'ingredient_inventory': self.ingredient_inventory
        }

    def update(self, data):
        self.name = data.get('name', self.name)
        self.dietary_preference = data.get('dietary_preference', self.dietary_preference)
        self.cooking_skill_level = data.get('cooking_skill_level', self.cooking_skill_level)
        self.ingredient_inventory = data.get('ingredient_inventory', self.ingredient_inventory)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.PickleType, nullable=False)
    dietary_type = db.Column(db.String(50), nullable=False)
    skill_level_required = db.Column(db.String(50), nullable=False)
    cuisine = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'dietary_type': self.dietary_type,
            'skill_level_required': self.skill_level_required,
            'cuisine': self.cuisine
        }
