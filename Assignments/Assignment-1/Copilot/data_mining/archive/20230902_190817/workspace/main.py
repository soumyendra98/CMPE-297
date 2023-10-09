from game import Game
from gameboard import GameBoard

def main():
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    board = GameBoard()
    game = Game(player1, player2, board)
    game.start_game()
    while input("Do you want to play again? (yes/no) ").lower() == "yes":
        game.restart_game()

if __name__ == "__main__":
    main()
