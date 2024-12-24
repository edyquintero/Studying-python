class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.board = None
        self.ships = []

    def set_board(self, board):
        self.board = board

    def add_ship(self, ship):
        self.ships.append(ship)
