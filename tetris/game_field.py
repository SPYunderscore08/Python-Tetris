import pygame
from game_piece import Piece


class Field:
    def __init__(self, width, height, unit_scaling_factor, backround_color):
        self.width = width # in units -> 1 cell
        self.height = height
        self.unit_scaling_factor = unit_scaling_factor
        self.background_color = backround_color
        self.screen = pygame.display.set_mode((self.width * unit_scaling_factor, self.height * unit_scaling_factor))


    def run(self):
        title = 'Tetris'

        pygame.display.set_caption(title)
        self.screen.fill(self.background_color)
        pygame.display.flip()

        falling_piece = Piece(1, 2, (255, 255, 255)) # throwaway

        running = True
        while running: # game loop
            for event in pygame.event.get():
                self.draw_piece(falling_piece)

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()


    def draw_piece(self, falling_piece):
        pygame.draw.rect(
            self.screen,
            falling_piece.color,
        (
                falling_piece.x * self.unit_scaling_factor,
                falling_piece.y * self.unit_scaling_factor,
                self.unit_scaling_factor,
                self.unit_scaling_factor
            )
        )