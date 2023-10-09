from player import Player
from board import Board
from dice import Dice

class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.dice = Dice()
        self.current_player = 0

    def start(self):
        while not self.is_won():
            self.play_turn()

    def play_turn(self):
        roll = self.dice.roll()
        player = self.players[self.current_player]
        player.move(roll)
        self.check_snake_or_ladder(player)
        self.current_player = (self.current_player + 1) % 2

    def check_snake_or_ladder(self, player):
        for snake in self.board.snakes:
            if player.position == snake.head:
                player.position = snake.tail
        for ladder in self.board.ladders:
            if player.position == ladder.base:
                player.position = ladder.top

    def is_won(self):
        for player in self.players:
            if player.position == 100:
                print(f"{player.name} wins!")
                return True
        return False
