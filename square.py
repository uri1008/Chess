from dataclasses import dataclass
import enum


class PieceType(enum.Enum):
    pawn = enum.auto()
    rock = enum.auto()
    knight = enum.auto()
    bishop = enum.auto()
    queen = enum.auto()
    king = enum.auto()
    empty_square = enum.auto


class PieceColor(enum.Enum):
    White = enum.auto()
    Black = enum.auto()


@dataclass(slots=True, kw_only=True, order=True)
class Square:
    row: int
    square: int
    piece: enum = None


@dataclass
class EmptySquare(Square):

    def __post_init__(self):
        self.piece = PieceType.empty_square


@dataclass
class Pawn(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

    def __post_init__(self):
        self.piece = PieceType.pawn


@dataclass
class Rock(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

    def __post_init__(self):
        self.piece = PieceType.rock


@dataclass
class Knight(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

    def __post_init__(self):
        self.piece = PieceType.knight


@dataclass
class Bishop(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

    def __post_init__(self):
        self.piece = PieceType.bishop


@dataclass
class Queen(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

    def __post_init__(self):
        self.piece = PieceType.queen


@dataclass
class King(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass
