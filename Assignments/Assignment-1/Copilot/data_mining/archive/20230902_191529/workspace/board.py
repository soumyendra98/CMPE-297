from snake import Snake
from ladder import Ladder
import random

class Board:
    def __init__(self):
        self.snakes = [Snake(random.randint(2, 99), random.randint(1, 98)) for _ in range(5)]
        self.ladders = [Ladder(random.randint(1, 98), random.randint(2, 99)) for _ in range(5)]
