document.getElementById('preferences-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var dietaryPreferences = document.getElementById('dietary-preferences').value;
    var skillLevel = document.getElementById('skill-level').value;
    var availableIngredients = document.getElementById('available-ingredients').value.split(',');
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            dietary_preferences: dietaryPreferences,
            skill_level: skillLevel,
            available_ingredients: availableIngredients
        })
    })
    .then(response => response.json())
    .then(data => {
        var recommendations = document.getElementById('recommendations');
        recommendations.innerHTML = '';
        data.forEach(function(recipe) {
            var recipeElement = document.createElement('div');
            recipeElement.textContent = recipe.name;
            recommendations.appendChild(recipeElement);
        });
    });
});
