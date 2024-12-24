from Board import Board
from Player import Player
from Ship import Ship

board_size = int(input("Ingrese el tamaño del tablero: "))
player_1 = Player(input("Ingrese el nombre del jugador 1: "))
player_2 = Player(input("Ingrese el nombre del jugador 2: "))

board_player_1 = Board(board_size)
board_player_2 = Board(board_size)

player_1.set_board(board_player_1)
player_2.set_board(board_player_2)

ship_1 = Ship([(0, 0), (0, 1), (0, 2)], 3, 'H')
board_player_1.place_ship(ship_1)

print(f"\nTablero de {player_1.player_name}:")
board_player_1.show_board()
