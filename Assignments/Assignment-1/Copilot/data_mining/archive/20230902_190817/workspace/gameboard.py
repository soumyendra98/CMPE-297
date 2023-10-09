import random

class GameBoard:
    def __init__(self, size=10):
        self.size = size
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [0] * (self.size * self.size + 1)
        for _ in range(5):
            start_snake = random.randint(2, self.size * self.size - 1)
            end_snake = random.randint(1, start_snake - 1)
            board[start_snake] = -end_snake

            start_ladder = random.randint(2, self.size * self.size - 1)
            end_ladder = random.randint(start_ladder + 1, self.size * self.size)
            board[start_ladder] = end_ladder
        return board

    def move_player(self, player, roll):
        player.position += roll
        if player.position > self.size * self.size:
            player.position -= roll
            return
        while self.board[player.position] != 0:
            if self.board[player.position] > 0:
                player.position = self.board[player.position]
            else:
                player.position = -self.board[player.position]
