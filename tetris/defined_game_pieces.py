from game_piece import Piece
import copy

class LongPiece(Piece):
    color = [50, 235, 235]
    matrix = [
        [False, False, False, False],
        [True , True , True , True ],
        [False, False, False, False],
        [False, False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = LongPiece.color.copy()
        self.matrix = copy.deepcopy(LongPiece.matrix)


class LPiece(Piece):
    color = [235, 155, 50]
    matrix = [
        [False, False, True ],
        [True , True , True ],
        [False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = LPiece.color.copy()
        self.matrix = copy.deepcopy(LPiece.matrix)


class BackLPiece(Piece):
    color = [50, 130, 235]
    matrix = [
        [True , False, False],
        [True , True , True ],
        [False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = BackLPiece.color.copy()
        self.matrix = copy.deepcopy(BackLPiece.matrix)


class SPiece(Piece):
    color = [50, 235, 60]
    matrix = [
        [False, True , True ],
        [True , True , False],
        [False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = SPiece.color.copy()
        self.matrix = copy.deepcopy(SPiece.matrix)


class BackSPiece(Piece):
    color = [235, 50, 50]
    matrix = [
        [True , True , False],
        [False, True , True ],
        [False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = BackSPiece.color.copy()
        self.matrix = copy.deepcopy(BackSPiece.matrix)


class Pyramid(Piece):
    color = [200, 50, 235]
    matrix = [
        [False, True , False],
        [True , True , True ],
        [False, False, False],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = Pyramid.color.copy()
        self.matrix = copy.deepcopy(Pyramid.matrix)


class Square(Piece):
    color = [235, 235, 50]
    matrix = [
        [True, True],
        [True, True],
    ]

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = Square.color.copy()
        self.matrix = copy.deepcopy(Square.matrix)
