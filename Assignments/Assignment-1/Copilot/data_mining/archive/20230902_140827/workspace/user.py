class User:
    def __init__(self, dietary_preferences, ingredient_inventory, cooking_skill_level, previous_interactions):
        self.dietary_preferences = dietary_preferences
        self.ingredient_inventory = ingredient_inventory
        self.cooking_skill_level = cooking_skill_level
        self.previous_interactions = previous_interactions

    def update_profile(self, dietary_preferences, cooking_skill_level):
        self.dietary_preferences = dietary_preferences
        self.cooking_skill_level = cooking_skill_level

    def update_inventory(self, ingredient_inventory):
        self.ingredient_inventory = ingredient_inventory
