class Piece:
    matrix = []
    color = False # temporary (to hopefully only use up 1 bit)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])
