document.getElementById('recipe-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const ingredients = document.getElementById('ingredients').value.split(',');
    const category = document.getElementById('category').value;
    fetch('/get_recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            ingredients: ingredients,
            category: category,
        }),
    })
    .then(response => response.json())
    .then(data => {
        const recipeList = document.getElementById('recipe-list');
        recipeList.innerHTML = '';
        data.forEach(recipe => {
            const recipeDiv = document.createElement('div');
            recipeDiv.className = 'mb-4 p-4 border rounded';
            recipeDiv.innerHTML = `
                <h2 class="text-2xl">${recipe.name}</h2>
                <p>${recipe.ingredients.join(', ')}</p>
                <p>${recipe.category}</p>
                <p>${recipe.level}</p>
            `;
            recipeList.appendChild(recipeDiv);
        });
    });
});
