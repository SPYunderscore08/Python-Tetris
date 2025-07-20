from game_piece import Piece

class LongPiece(Piece):
    color = [50, 235, 235]
    matrix = [
        [False, False, False, False],
        [True , True , True , True ],
        [False, False, False, False],
        [False, False, False, False],
    ]


class LPiece(Piece):
    color = [235, 155, 50]
    matrix = [
        [False, False, True ],
        [True , True , True ],
        [False, False, False],
    ]


class BackLPiece(Piece):
    color = [50, 130, 235]
    matrix = [
        [True , False, False],
        [True , True , True ],
        [False, False, False],
    ]


class SPiece(Piece):
    color = [50, 235, 60]
    matrix = [
        [False, True , True ],
        [True , True , False],
        [False, False, False],
    ]


class BackSPiece(Piece):
    color = [235, 50, 50]
    matrix = [
        [True , True , False],
        [False, True , True ],
        [False, False, False],
    ]


class Square(Piece):
    color = [235, 235, 50]
    matrix = [
        [True, True],
        [True, True],
    ]


class Pyramid(Piece):
    color = [200, 50, 235]
    matrix = [
        [False, True , False],
        [True , True , True ],
        [False, False, False],
    ]
