import pygame
import random
from defined_game_pieces import *

class Field:
    def __init__(self, width, height, unit_scaling_factor, background_color):
        self.width = width # in units -> 1 cell
        self.height = height
        self.unit_scaling_factor = unit_scaling_factor
        self.background_color = background_color
        self.screen = pygame.display.set_mode((self.width * unit_scaling_factor, self.height * unit_scaling_factor))


    def run(self):
        title = 'Tetris'
        pygame.display.set_caption(title)
        self.screen.fill(self.background_color)

        falling_piece = Piece # creation of the variable for outer scope usage

        running = True
        is_falling = False

        matrix_offset = 1
        init_x = (self.width // 2) - matrix_offset - 1
        init_y = 0

        defined_piece_number = 7

        while running: # game loop
            for event in pygame.event.get():
                if not is_falling:
                    random_piece = random.randint(1, defined_piece_number)
                    match random_piece:
                        case 1:
                            falling_piece = LongPiece(init_x, init_y)

                        case 2:
                            falling_piece = LPiece(init_x, init_y)

                        case 3:
                            falling_piece = BackLPiece(init_x, init_y)

                        case 4:
                            falling_piece = SPiece(init_x, init_y)

                        case 5:
                            falling_piece = BackSPiece(init_x, init_y)

                        case 6:
                            falling_piece = Pyramid(init_x , init_y)

                        case 7:
                            falling_piece = Square(init_x + 1, init_y)

                    is_falling = True

                self.draw_piece(falling_piece)
                if event.type == pygame.QUIT:
                    running = False


    def draw_piece(self, piece):
        for i in range(len(piece.matrix)):
            for j in range(len(piece.matrix[i])):
                if piece.matrix[i][j]:
                    pygame.draw.rect(
                        self.screen,
                        piece.color,
                        (
                            (piece.x + j) * self.unit_scaling_factor,
                            (piece.y + i) * self.unit_scaling_factor,
                            self.unit_scaling_factor,
                            self.unit_scaling_factor
                        )
                    )
        pygame.display.flip()
