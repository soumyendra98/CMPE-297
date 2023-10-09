from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models import Recipe

def train_model():
    recipes = Recipe.query.all()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([recipe.ingredients for recipe in recipes])
    return tfidf_matrix

def get_recommendations(user):
    tfidf_matrix = train_model()
    user_vector = tfidf_matrix[user.id]
    cosine_similarities = cosine_similarity(user_vector, tfidf_matrix)
    similar_indices = cosine_similarities.argsort().flatten()[-10:]
    recommended_recipes = [Recipe.query.get(index) for index in similar_indices]
    return recommended_recipes
