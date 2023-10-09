const express = require('express');
const mongoose = require('mongoose');
const recipeRoutes = require('./routes/recipeRoutes');

const app = express();

mongoose.connect('mongodb://localhost:27017/recipeRecommender', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.use(express.json());
app.use('/api/recipes', recipeRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
