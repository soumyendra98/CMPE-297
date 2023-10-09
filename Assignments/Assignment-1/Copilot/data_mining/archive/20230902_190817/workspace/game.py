from player import Player
from gameboard import GameBoard
from dice import Dice

class Game:
    def __init__(self, player1, player2, board):
        self.players = [Player(player1), Player(player2)]
        self.board = board
        self.dice = Dice()

    def start_game(self):
        while True:
            for player in self.players:
                roll = self.dice.roll()
                self.board.move_player(player, roll)
                print(f"{player.name} rolled a {roll} and is now on square {player.position}")
                if player.position == self.board.size * self.board.size:
                    print(f"{player.name} wins!")
                    return

    def restart_game(self):
        for player in self.players:
            player.position = 1
        self.board = GameBoard()
        self.start_game()
