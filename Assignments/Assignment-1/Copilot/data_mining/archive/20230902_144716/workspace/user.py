class User:
    def __init__(self, dietary_preferences, skill_level, available_ingredients):
        self.dietary_preferences = dietary_preferences
        self.skill_level = skill_level
        self.available_ingredients = available_ingredients

def get_matching_recipes(user, recipes):
    return [recipe for recipe in recipes if recipe.dietary_preferences == user.dietary_preferences and recipe.skill_level == user.skill_level and all(ingredient in user.available_ingredients for ingredient in recipe.ingredients)]

def update_user_ingredients(user, ingredients):
    user.available_ingredients = ingredients
