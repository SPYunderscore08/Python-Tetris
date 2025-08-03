class Piece:
    matrix = []
    color = ()

    def __init__(self, x, y):
        self.x = x # most left point of the matrix
        self.y = y # highest point of the matrix

    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def turn_clockwise(self): # https://www.enjoyalgorithms.com/blog/rotate-a-matrix-by-90-degrees-in-an-anticlockwise-direction (modified)
        n = len(self.matrix[0])
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[n - 1 - j][i]
                self.matrix[n - 1 - j][i] = self.matrix[n - 1 - i][n - 1 - j]
                self.matrix[n - 1 - i][n - 1 - j] = self.matrix[j][n - 1 - i]
                self.matrix[j][n - 1 - i] = temp

    def turn_counterclockwise(self): # https://www.enjoyalgorithms.com/blog/rotate-a-matrix-by-90-degrees-in-an-anticlockwise-direction
        n = len(self.matrix[0])
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][n - 1 - i]
                self.matrix[j][n - 1 - i] = self.matrix[n - 1 - i][n - 1 - j]
                self.matrix[n - 1 - i][n - 1 - j] = self.matrix[n - 1 - j][i]
                self.matrix[n - 1 - j][i] = temp


