import pygame

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
ROWS = 8
SQUARES_IN_A_ROW = 8
SQUARE_WIDTH: float = SCREEN_WIDTH/SQUARES_IN_A_ROW
SQUARE_HEIGHT: float = SCREEN_HEIGHT/ROWS
SCREEN_CAPTION: str = 'interactive board'
SCREEN_ICON: pygame.surface.SurfaceType = pygame.image.load(
    "images\\chess_icon.png")
FPS: int = 60
SQUARES_COLOR_1: tuple = (200, 120, 95)
SQUARES_COLOR_2: tuple = (75, 75, 75)

