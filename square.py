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
    piece: enum = PieceType.empty_square


@dataclass
class EmptySquare(Square):

    def __repr__(self):
        return f"piece={self.piece}, row={self.row}, square={self.square}"


@dataclass
class Pawn(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass


@dataclass
class Rock(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass


@dataclass
class Knight(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass


@dataclass
class Bishop(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass


@dataclass
class Queen(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass

@dataclass
class King(Square):
    piece_color: enum

    def check_for_moves(self) -> list[int]:
        pass
