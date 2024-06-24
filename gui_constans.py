import pygame

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
ROWS = 8
SQUARES_IN_A_ROW = 8
SQUARE_WIDTH: float = SCREEN_WIDTH / SQUARES_IN_A_ROW
SQUARE_HEIGHT: float = SCREEN_HEIGHT / ROWS
SCREEN_CAPTION: str = 'interactive board'
SCREEN_ICON: pygame.surface.SurfaceType = pygame.image.load(
    "images\\chess_icon.png")
FPS: int = 60
SQUARES_COLOR_1: tuple = (200, 120, 95)
SQUARES_COLOR_2: tuple = (75, 75, 75)

__BLACK_PAWN_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black_pawn.png")
__BLACK_KNIGHT_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black_knight.png")
__BLACK_BISHOP_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black_bishop.png")
__BLACK_ROCK_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black_rock.png")
__BLACK_QUEEN_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black.queen.png")
__BLACK_KING_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\black_king.png")

__BLACK_PAWN_IMAGE: pygame.surface.SurfaceType = __BLACK_PAWN_FILE_NAME
__BLACK_KNIGHT_IMAGE: pygame.surface.SurfaceType = __BLACK_KNIGHT_FILE_NAME
__BLACK_BISHOP_IMAGE: pygame.surface.SurfaceType = __BLACK_BISHOP_FILE_NAME
__BLACK_ROCK_IMAGE: pygame.surface.SurfaceType = __BLACK_ROCK_FILE_NAME
__BLACK_QUEEN_IMAGE: pygame.surface.SurfaceType = __BLACK_QUEEN_FILE_NAME
__BLACK_KING_IMAGE: pygame.surface.SurfaceType = __BLACK_KING_FILE_NAME

__WHITE_PAWN_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_pawn.png")
__WHITE_KNIGHT_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_knight.png")
__WHITE_BISHOP_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_bishop.png")
__WHITE_ROCK_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_rock.png")
__WHITE_QUEEN_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_queen.png")
__WHITE_KING_FILE_NAME: pygame.surface.SurfaceType = pygame.image.load(
    "images\\white_king.png")

__WHITE_PAWN_IMAGE: pygame.surface.SurfaceType = __WHITE_PAWN_FILE_NAME
__WHITE_KNIGHT_IMAGE: pygame.surface.SurfaceType = __WHITE_KNIGHT_FILE_NAME
__WHITE_BISHOP_IMAGE: pygame.surface.SurfaceType = __WHITE_BISHOP_FILE_NAME
__WHITE_ROCK_IMAGE: pygame.surface.SurfaceType = __WHITE_ROCK_FILE_NAME
__WHITE_QUEEN_IMAGE: pygame.surface.SurfaceType = __WHITE_QUEEN_FILE_NAME
__WHITE_KING_IMAGE: pygame.surface.SurfaceType = __WHITE_KING_FILE_NAME

tools = [__BLACK_PAWN_IMAGE, __BLACK_KNIGHT_IMAGE, __BLACK_BISHOP_IMAGE,
         __BLACK_ROCK_IMAGE,
         __BLACK_QUEEN_IMAGE,
         __BLACK_KING_IMAGE, __WHITE_PAWN_IMAGE, __WHITE_KNIGHT_IMAGE,
         __WHITE_BISHOP_IMAGE, __WHITE_ROCK_IMAGE,
         __WHITE_QUEEN_IMAGE, __WHITE_KING_IMAGE]
