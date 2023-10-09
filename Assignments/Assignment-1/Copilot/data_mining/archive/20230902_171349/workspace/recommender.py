from recipe import Recipe

class Recommender:
    def __init__(self, user):
        self.user = user
        self.recipes = Recipe.get_all()

    def recommend_recipes(self):
        recommended_recipes = []
        for recipe in self.recipes:
            if self.user.cooking_skills >= recipe.difficulty_level and \
               set(recipe.ingredients).issubset(set(self.user.available_ingredients)) and \
               recipe.dietary_info in self.user.dietary_preferences:
                recommended_recipes.append(recipe)
        return recommended_recipes
