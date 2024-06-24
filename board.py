from board_constant import *
from square import Pawn, Rock, Knight, Bishop, Queen, King, EmptySquare, PieceColor


class Board:
    @staticmethod
    # get board location by the row and square
    def get_board_location(row, square) -> int:
        return row * 8 + square

    @staticmethod
    def create_board() -> list:
        board = []
        # create board structure
        for row in range(ROWS):
            for square in range(SQUARES):
                board.append(EmptySquare(row=row, square=square))

        # add pieces to board
        for row in range(ROWS):
            for square in range(SQUARES):
                if row == 0 or row == 7:
                    current_piece_color = PieceColor.White if row == 7 else PieceColor.Black
                    if square == 0 or square == 7:
                        board[Board.get_board_location(row=row, square=square)] = Rock(
                            piece_color=current_piece_color,
                            row=row, square=square, piece=Rock)
                    elif square == 1 or square == 6:
                        board[Board.get_board_location(row=row, square=square)] = Knight(
                            piece_color=current_piece_color, row=row, square=square, piece=Knight)
                    elif square == 2 or square == 5:
                        board[Board.get_board_location(row=row, square=square)] = Bishop(
                            piece_color=current_piece_color, row=row, square=square, piece=Bishop)
                    elif square == 3:
                        board[Board.get_board_location(row=row, square=square)] = Queen(
                            piece_color=current_piece_color, row=row, square=square, piece=Queen)
                    elif square == 4:
                        board[Board.get_board_location(row=row, square=square)] = King(
                            piece_color=current_piece_color, row=row, square=square, piece=King)

                elif row == 1 or row == 6:
                    current_piece_color = PieceColor.White if row == 6 else PieceColor.Black
                    board[Board.get_board_location(row=row, square=square)] = Pawn(piece_color=current_piece_color,
                                                                                   row=row, square=square, piece=Pawn)
        return board
