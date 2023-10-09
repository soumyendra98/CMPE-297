window.onload = function() {
    var recipes = JSON.parse(recipes);
    var container = document.querySelector('.container .row');

    for (var i = 0; i < recipes.length; i++) {
        var card = document.createElement('div');
        card.className = 'card';
        card.style.width = '18rem';

        var img = document.createElement('img');
        img.className = 'card-img-top';
        img.src = recipes[i].image;
        card.appendChild(img);

        var cardBody = document.createElement('div');
        cardBody.className = 'card-body';

        var cardTitle = document.createElement('h5');
        cardTitle.className = 'card-title';
        cardTitle.textContent = recipes[i].name;
        cardBody.appendChild(cardTitle);

        var cardText = document.createElement('p');
        cardText.className = 'card-text';
        cardText.textContent = 'Diet: ' + recipes[i].diet + ', Skill: ' + recipes[i].skill;
        cardBody.appendChild(cardText);

        card.appendChild(cardBody);
        container.appendChild(card);
    }
};
