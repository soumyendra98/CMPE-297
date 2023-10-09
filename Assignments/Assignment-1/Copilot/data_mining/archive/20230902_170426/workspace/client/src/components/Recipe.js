import React from 'react';

function Recipe({ recipe }) {
  return (
    <div>
      <h2>{recipe.title}</h2>
      <p>{recipe.instructions}</p>
    </div>
  );
}

export default Recipe;
