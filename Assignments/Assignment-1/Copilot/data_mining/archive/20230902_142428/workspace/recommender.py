class Recommender:
    def __init__(self, all_recipes):
        self.all_recipes = all_recipes

    def recommend(self, user):
        recommended_recipes = []
        for recipe in self.all_recipes:
            if user.dietary_preferences == recipe.dietary_category and set(user.available_ingredients).issubset(set(recipe.ingredients)) and user.cooking_skills == recipe.difficulty:
                recommended_recipes.append(recipe)
        return recommended_recipes
