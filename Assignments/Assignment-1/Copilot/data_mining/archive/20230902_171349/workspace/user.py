class User:
    def __init__(self, form_data):
        self.dietary_preferences = form_data.getlist('dietary_preferences')
        self.available_ingredients = form_data.get('available_ingredients').split(',')
        self.cooking_skills = form_data.get('cooking_skills')
