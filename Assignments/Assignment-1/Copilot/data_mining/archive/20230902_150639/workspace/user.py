class User:
    def __init__(self, name, dietary_preferences, cooking_skills, available_ingredients):
        self.name = name
        self.dietary_preferences = dietary_preferences
        self.cooking_skills = cooking_skills
        self.available_ingredients = available_ingredients

    def update_ingredients(self, new_ingredients):
        self.available_ingredients = new_ingredients

    def get_dietary_preferences(self):
        return self.dietary_preferences

    def get_cooking_skills(self):
        return self.cooking_skills

    def get_available_ingredients(self):
        return self.available_ingredients

    def update_dietary_preferences(self, new_preferences):
        self.dietary_preferences = new_preferences

    def update_cooking_skills(self, new_skills):
        self.cooking_skills = new_skills
