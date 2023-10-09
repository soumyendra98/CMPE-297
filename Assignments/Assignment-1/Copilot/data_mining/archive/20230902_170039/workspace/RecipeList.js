import React from 'react';

const RecipeList = ({ recipes }) => {
  const renderedList = recipes.map(recipe => {
    return <div key={recipe.id}>{recipe.name}</div>;
  });

  return <div>{renderedList}</div>;
};

export default RecipeList;
