const Recipe = require('../models/Recipe');
const recipeRecommender = require('../utils/recipeRecommender');

exports.getRecipes = async (req, res) => {
  try {
    const userPreferences = req.body;
    const recipes = await Recipe.find();
    const recommendedRecipes = recipeRecommender.recommend(recipes, userPreferences);
    res.json(recommendedRecipes);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};

// Other controller methods go here
