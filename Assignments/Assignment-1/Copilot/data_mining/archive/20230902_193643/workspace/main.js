// Function to create the game board
function createGameBoard() {
    const gameBoard = document.getElementById('game-board');

    // Create 100 divs for the game board
    for (let i = 1; i <= 100; i++) {
        const div = document.createElement('div');
        div.id = `cell-${i}`;
        div.className = 'p-2 border';
        gameBoard.appendChild(div);
    }

    // Add classes for snakes and ladders
    for (let key in snakesAndLadders) {
        const cell = document.getElementById(`cell-${key}`);
        if (snakesAndLadders[key] < key) {
            cell.classList.add('snake');
        } else {
            cell.classList.add('ladder');
        }
    }
}

// Function to move the player
function movePlayer(player, position) {
    let newPosition = position + rollDice();

    // Check for snakes or ladders
    if (snakesAndLadders[newPosition]) {
        newPosition = snakesAndLadders[newPosition];
    }

    // Update player position
    if (player === 1) {
        if (player1Position) {
            document.getElementById(`cell-${player1Position}`).classList.remove('player1');
        }
        player1Position = newPosition;
        document.getElementById(`cell-${player1Position}`).classList.add('player1');
    } else {
        if (player2Position) {
            document.getElementById(`cell-${player2Position}`).classList.remove('player2');
        }
        player2Position = newPosition;
        document.getElementById(`cell-${player2Position}`).classList.add('player2');
    }

    // Switch player
    currentPlayer = currentPlayer === 1 ? 2 : 1;
}

// Function to restart the game
function restartGame() {
    if (player1Position) {
        document.getElementById(`cell-${player1Position}`).classList.remove('player1');
    }
    if (player2Position) {
        document.getElementById(`cell-${player2Position}`).classList.remove('player2');
    }
    player1Position = 0;
    player2Position = 0;
    currentPlayer = 1;
}

// Create the game board when the page loads
window.onload = createGameBoard;
