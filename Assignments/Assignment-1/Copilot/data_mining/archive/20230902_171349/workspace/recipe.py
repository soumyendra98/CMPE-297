class Recipe:
    @staticmethod
    def get_all():
        # This method should return all recipes from the database.
        # For simplicity, we will return a list of dummy recipes.
        return [
            Recipe(['lettuce', 'tomato', 'cucumber'], 'vegan', 1),
            Recipe(['chicken', 'lettuce', 'tomato'], 'high-protein', 2),
            Recipe(['beef', 'lettuce', 'tomato'], 'low-carb', 3)
        ]

    def __init__(self, ingredients, dietary_info, difficulty_level):
        self.ingredients = ingredients
        self.dietary_info = dietary_info
        self.difficulty_level = difficulty_level
