import pygame
import random
from defined_game_pieces import *

class Field:
    def __init__(self, width, height, unit_scaling_factor, background_color):
        self.unit_size = 1
        self.width = width # in units -> 1 cell
        self.height = height
        self.unit_scaling_factor = unit_scaling_factor
        self.background_color = background_color
        self.screen = pygame.display.set_mode((self.width * unit_scaling_factor, self.height * unit_scaling_factor))
        self.game_state_list = [[False] * self.width] * self.height
        self.number_of_actions = 5
        self.action_list = [False] * self.number_of_actions


    def run(self):
        title = 'Tetris'
        pygame.display.set_caption(title)
        self.screen.fill(self.background_color)

        matrix_offset = 1
        init_x = (self.width // 2) - matrix_offset - 1
        init_y = 0

        falling_piece = Piece # creation of the variable for outer scope usage

        former_falling_piece = Piece(init_x, init_y) # piece used for clearing lingering cells
        former_falling_piece.matrix = [[0]]
        former_falling_piece.color = self.background_color

        running = True
        is_falling = False
        defined_piece_number = 7

        pygame.key.set_repeat(120)

        while running: # game loop
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
                        falling_piece = Pyramid(init_x, init_y)

                    case 7:
                        falling_piece = Square(init_x + 1, init_y)

                is_falling = True

            self.draw_piece(former_falling_piece)
            self.draw_piece(falling_piece)
            pygame.display.flip()

            former_falling_piece.matrix = falling_piece.matrix
            former_falling_piece.x = falling_piece.x
            former_falling_piece.y = falling_piece.y

            falling_piece.y += 0.0001 # todo


            for event in pygame.event.get():
                self.draw_piece(former_falling_piece)
                self.check_for_keydown(event, falling_piece)
                self.check_for_keyup(event, falling_piece)

                if event.type == pygame.QUIT:
                    running = False

            # self.alter_game_state(falling_piece)


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

    def alter_game_state(self, falling_piece):
        pass

    def execute_current_actions(self, falling_piece):
        for i in range(len(self.action_list)):
            if self.action_list[i]:
                match i:
                    case 0:
                        falling_piece.turn_clockwise()

                    case 1:
                        falling_piece.x -= self.unit_size

                    case 2:
                        falling_piece.x += self.unit_size

                    case 3:
                        falling_piece.y += self.unit_size

                    case 4:
                        falling_piece.turn_counterclockwise()

    def check_for_keydown(self, event, falling_piece):

        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w | pygame.K_UP:
                    self.action_list[0] = True

                case pygame.K_a | pygame.K_LEFT:
                    self.action_list[1] = True

                case pygame.K_d | pygame.K_RIGHT:
                    self.action_list[2] = True

                case pygame.K_s | pygame.K_DOWN:
                    self.action_list[3] = True

                case pygame.K_z:
                    self.action_list[4] = True
            self.execute_current_actions(falling_piece)


    def check_for_keyup(self, event, falling_piece):
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w | pygame.K_UP:
                    self.action_list[0] = False

                case pygame.K_a | pygame.K_LEFT:
                    self.action_list[1] = False

                case pygame.K_d | pygame.K_RIGHT:
                    self.action_list[2] = False

                case pygame.K_s | pygame.K_DOWN:
                    self.action_list[3] = False

                case pygame.K_z:
                    self.action_list[4] = False

