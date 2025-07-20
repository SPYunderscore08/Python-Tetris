class Piece:
    matrix = []
    color = ()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
