import pygame
import random

from defined_game_pieces import *

class Field:
    def __init__(self, width, height, unit_scaling_factor, background_color, init_tick_rate = 1000):
        self.unit_size = 1
        self.width = width # in units -> 1 cell
        self.height = height
        self.unit_scaling_factor = unit_scaling_factor
        self.background_color = background_color
        self.init_tick_rate = init_tick_rate
        self.tick_rate = self.init_tick_rate
        self.screen = pygame.display.set_mode((self.width * unit_scaling_factor, self.height * unit_scaling_factor))
        self.game_state_list = [[False] * self.width] * self.height
        self.number_of_actions = 5
        self.action_list = [False] * self.number_of_actions
        self.event_update_y_position = pygame.USEREVENT + 1
        self.event_left_key_held = pygame.USEREVENT + 2
        self.event_right_key_held = pygame.USEREVENT + 3
        self.event_down_key_held = pygame.USEREVENT + 4
        self.left_is_held = False
        self.right_is_held = False
        self.allow_x_left_tick_rate_change = True
        self.allow_x_right_tick_rate_change = True
        self.allow_y_tick_rate_change = True

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

        pygame.time.set_timer(self.event_update_y_position, self.tick_rate)

        while running:
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

            self.draw_piece(falling_piece)
            pygame.display.flip()

            former_falling_piece.matrix = falling_piece.matrix
            former_falling_piece.x = falling_piece.x
            former_falling_piece.y = falling_piece.y

            self.draw_piece(former_falling_piece)
            # pygame.time.delay(1000 // 60) # one frame at 60 fps

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.check_for_keydown(event, falling_piece)

                if event.type == pygame.KEYUP:
                    self.check_for_keyup(event)

                if not (self.left_is_held and self.right_is_held):
                    if event.type == self.event_left_key_held:
                        falling_piece.x -= 1

                    elif event.type == self.event_right_key_held:
                        falling_piece.x += 1

                if event.type == self.event_update_y_position or event.type == self.event_down_key_held:
                    falling_piece.y += 1

                if event.type == pygame.QUIT:
                    running = False

    def check_for_keydown(self, event, falling_piece):
        match event.key:
            case pygame.K_w | pygame.K_UP:
                falling_piece.turn_clockwise()

            case (pygame.K_a | pygame.K_LEFT) | (pygame.K_d | pygame.K_RIGHT):
                if self.left_is_held and self.right_is_held:
                    self.allow_x_left_tick_rate_change = True
                    self.allow_x_right_tick_rate_change = True

                    pygame.time.set_timer(self.event_left_key_held, 0)
                    pygame.time.set_timer(self.event_right_key_held, 0)

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.left_is_held = True
                    if self.allow_x_left_tick_rate_change:
                        self.allow_x_left_tick_rate_change = False
                        pygame.time.set_timer(self.event_left_key_held, self.init_tick_rate // 15)

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.right_is_held = True
                    if self.allow_x_right_tick_rate_change:
                        self.allow_x_right_tick_rate_change = False
                        pygame.time.set_timer(self.event_right_key_held, self.init_tick_rate // 15)

            case pygame.K_s | pygame.K_DOWN:
                if self.allow_y_tick_rate_change:
                    self.allow_y_tick_rate_change = False
                    pygame.time.set_timer(self.event_down_key_held, self.tick_rate // 15)

            case pygame.K_z:
                falling_piece.turn_counterclockwise()

    def check_for_keyup(self, event):
        match event.key:
            case pygame.K_a | pygame.K_LEFT:
                self.left_is_held = False
                pygame.time.set_timer(self.event_left_key_held, 0)
                self.allow_x_left_tick_rate_change = True

            case pygame.K_d | pygame.K_RIGHT:
                self.right_is_held = False
                pygame.time.set_timer(self.event_right_key_held, 0)
                self.allow_x_right_tick_rate_change = True

            case pygame.K_s | pygame.K_DOWN:
                pygame.time.set_timer(self.event_down_key_held, 0)
                self.allow_y_tick_rate_change = True

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
