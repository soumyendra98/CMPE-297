document.getElementById('get-recipes').addEventListener('click', function() {
    // Here we should implement the logic to get the ingredients from the user and send them to the server
    // For now, let's just send a hardcoded list of ingredients
    fetch('/get-recipes', {
        method: 'POST',
        body: JSON.stringify({
            ingredients: ['tomato', 'cheese', 'basil']
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Here we should implement the logic to display the recipes to the user
        // For now, let's just log the data
        console.log(data);
    });
});
