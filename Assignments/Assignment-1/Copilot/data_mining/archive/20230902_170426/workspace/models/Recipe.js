const mongoose = require('mongoose');

const RecipeSchema = new mongoose.Schema({
  title: String,
  ingredients: [String],
  instructions: String,
  dietaryPreferences: [String],
  skillLevel: String,
});

module.exports = mongoose.model('Recipe', RecipeSchema);
