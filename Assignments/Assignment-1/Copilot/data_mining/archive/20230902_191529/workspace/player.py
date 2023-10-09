class Player:
    def __init__(self, name):
        self.name = name
        self.position = 1

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100
