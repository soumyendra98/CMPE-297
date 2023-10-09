class Recipe:
    def __init__(self, name, ingredients, category, level):
        self.name = name
        self.ingredients = ingredients
        self.category = category
        self.level = level

    def to_dict(self):
        return {
            'name': self.name,
            'ingredients': self.ingredients,
            'category': self.category,
            'level': self.level,
        }

def get_recipes(ingredients, category):
    # This is a placeholder function. In a real application, this function would query a database or an API to get the recipes.
    return [
        Recipe('Recipe 1', ['ingredient 1', 'ingredient 2'], 'vegetarian', 'beginner'),
        Recipe('Recipe 2', ['ingredient 3', 'ingredient 4'], 'non-vegetarian', 'intermediate'),
        Recipe('Recipe 3', ['ingredient 5', 'ingredient 6'], 'vegan', 'advanced'),
    ]
