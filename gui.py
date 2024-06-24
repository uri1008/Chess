from gui_constans import *
import pygame


class Gui:
    def __init__(self):
        self.running = True
        self.board: list = []
        self.screen: pygame.surface.SurfaceType = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(SCREEN_CAPTION)
        pygame.display.set_icon(SCREEN_ICON)
        self.clock = pygame.time.Clock()

    def run_game_loop(self, board) -> None:
        self.clock.tick(FPS)
        self.board = board

        self.handle_events()
        self.draw_board()
        self.update_screen()

    def end_game(self) -> None:
        self.running = False

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_game()

    def draw_board(self) -> None:
        pass

    @staticmethod
    def update_screen() -> None:
        pygame.display.update()
