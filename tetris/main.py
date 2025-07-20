import pygame
from game_field import Field

def main():
    field_width = 10
    field_height = 20
    unit_scaling_factor = 45
    background_color = (20, 20, 20)

    game_field = Field(field_width, field_height, unit_scaling_factor, background_color)

    game_field.run()


if __name__ == '__main__':
    main()