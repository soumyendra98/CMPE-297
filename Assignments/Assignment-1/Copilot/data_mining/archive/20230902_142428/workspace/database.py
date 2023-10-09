import sqlite3
from user import User
from recipe import Recipe

def get_user(user_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    else:
        return User(row[0], row[1], row[2].split(','), row[3])

def update_user(user):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE users SET dietary_preferences = ?, available_ingredients = ?, cooking_skills = ? WHERE user_id = ?', (user.dietary_preferences, ','.join(user.available_ingredients), user.cooking_skills, user.user_id))
    conn.commit()
    conn.close()

def get_recipe(recipe_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM recipes WHERE recipe_id = ?', (recipe_id,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    else:
        return Recipe(row[0], row[1].split(','), row[2], row[3])

def get_all_recipes():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM recipes')
    rows = c.fetchall()
    conn.close()
    return [Recipe(row[0], row[1].split(','), row[2], row[3]) for row in rows]
