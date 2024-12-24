import numpy as np

class Board:
    def __init__(self, size):
        self.size = size
        self.board = np.full((size, size), 'X')
        self.ships = []

    def show_board(self):
        print(self.board)

    def place_ship(self, ship):
        for x, y in ship.ship_location:
            self.board[x][y] = 'S'
        self.ships.append(ship)

    def register_shot(self, x, y):
        if self.board[x][y] == 'S':
            self.board[x][y] = 'H'
            for ship in self.ships:
                if (x, y) in ship.ship_location:
                    ship.hits += 1
                    break
            return "Hit!"
        elif self.board[x][y] == 'X':
            self.board[x][y] = 'M'
            return "Miss!"
        else:
            return "Already targeted!"
