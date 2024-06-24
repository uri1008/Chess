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


@dataclass
class EmptySquare(Square):
    piece: enum = PieceType.empty_square

    def __repr__(self):
        return f"piece={self.piece}, row={self.row}, square={self.square}"


@dataclass
class Pawn(Square):
    piece_color: enum
    piece: enum = PieceType.pawn

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"


@dataclass
class Rock(Square):
    piece_color: enum
    piece: enum = PieceType.rock

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"


@dataclass
class Knight(Square):
    piece_color: enum
    piece: enum = PieceType.knight

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"


@dataclass
class Bishop(Square):
    piece_color: enum
    piece: enum = PieceType.bishop

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"


@dataclass
class Queen(Square):
    piece_color: enum
    piece: enum = PieceType.queen

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"


@dataclass
class King(Square):
    piece_color: enum
    piece: enum = PieceType.king

    def check_for_moves(self) -> list[int]:
        pass

    def __repr__(self):
        return f"piece={self.piece}, piece color={self.piece_color},row={self.row}, square={self.square}"
