import pygame

class Field:
    def __init__(self, width, height, unit_scaling_factor, backround_color):
        self.width = width # in units -> 1 cell
        self.height = height
        self.unit_scaling_factor = unit_scaling_factor
        self.background_color = backround_color


    def run(self):
        screen = pygame.display.set_mode((self.width * self.unit_scaling_factor, self.height * self.unit_scaling_factor))
        title = 'Tetris'

        pygame.display.set_caption(title)
        screen.fill(self.background_color)
        pygame.display.flip()

        running = True
        while running: # game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
