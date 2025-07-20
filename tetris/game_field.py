import pygame
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
        pygame.display.flip()

        falling_piece = LongPiece(10, 10) # throwaway
        falling_piece.print_matrix()

        running = True
        while running: # game loop
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()


    def draw_piece(self, falling_piece):
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (
                falling_piece.x * self.unit_scaling_factor,
                falling_piece.y * self.unit_scaling_factor,
                self.unit_scaling_factor,
                self.unit_scaling_factor
            )
        )