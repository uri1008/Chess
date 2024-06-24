import pygame

from board import Board
from gui import Gui
from backend_costants import *


class Backend:
    def __init__(self) -> None:
        self.board: list = []
        self.game_interface = Gui()

    def start_new_game(self) -> None:
        self.board = Board.create_board()
        while True:
            self.game_interface.run_game_loop(self.board)
            if not self.is_game_running():
                break
        pygame.quit()

    def is_game_running(self):
        return self.game_interface.running
