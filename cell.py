import pygame
from settings import *


class Cell:
    colour = (10, 20, 40)

    def __init__(self, value, fixed, board, temp_cell_colour=WHITE):
        self.temp_cell_colour = temp_cell_colour
        self.board = board
        self.value = value
        self.fixed = fixed
        self.rect = None
        self.cell_colour = WHITE
        self.value_colour = BLACK
        self.x = None
        self.y = None

