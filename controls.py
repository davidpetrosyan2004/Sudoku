import sys
import pygame

from settings import *
from board import Board,Board1


class Controls:
    pos = None

    def __init__(self, logic):
        self.logic = logic

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                self.pos = pygame.mouse.get_pos()
                if (BOARD_TOPLEFT_X - BOARD_WIDTH // 2 < self.pos[0] < BOARD_TOPLEFT_X - BOARD_WIDTH // 2 + 120
                        and BOARD_TOPLEFT_Y + BOARD_HEIGHT // 2 < self.pos[1] < BOARD_TOPLEFT_Y + BOARD_HEIGHT // 2 + 50):
                    self.logic.wrong_number_count = 0

                if (BOARD_TOPLEFT_X - BOARD_WIDTH // 2 - 50 < self.pos[0] < BOARD_TOPLEFT_X - BOARD_WIDTH // 2 + 220
                        and BOARD_TOPLEFT_Y + BOARD_HEIGHT//2+60 < self.pos[1] < BOARD_TOPLEFT_Y + BOARD_HEIGHT//2+110):
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                    self.logic.wrong_number_count = 0

                if 1000 < self.pos[0] < 1100 and BOARD_TOPLEFT_Y < self.pos[1] < BOARD_TOPLEFT_Y+60:
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    Puzzle.freq_nums = 30
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                if 1000 < self.pos[0] < 1100 and BOARD_TOPLEFT_Y+60 < self.pos[1] < BOARD_TOPLEFT_Y+120:
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    Puzzle.freq_nums = 40
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                if 1000 < self.pos[0] < 1100 and BOARD_TOPLEFT_Y+120 < self.pos[1] < BOARD_TOPLEFT_Y+180:
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    Puzzle.freq_nums = 50
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                if 1000 < self.pos[0] < 1100 and BOARD_TOPLEFT_Y+180 < self.pos[1] < BOARD_TOPLEFT_Y+240:
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    Puzzle.freq_nums = 80
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                if 1000 < self.pos[0] < 1100 and BOARD_TOPLEFT_Y+240 < self.pos[1] < BOARD_TOPLEFT_Y+300:
                    SOLVED_BOARD = Puzzle.generate_solved_puzzle()
                    BOARD = Puzzle.generate_unsolved_puzzle(SOLVED_BOARD)
                    Puzzle.freq_nums = 100
                    board = Board(BOARD)
                    board1 = Board1(SOLVED_BOARD)

                if (BOARD_TOPLEFT_X < self.pos[0] < BOARD_TOPLEFT_X + BOARD_WIDTH
                        and BOARD_TOPLEFT_Y < self.pos[1] < BOARD_TOPLEFT_Y + BOARD_HEIGHT):
                    Board.marked_cell(self.pos[0], self.pos[1])

            if event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9 and self.pos:
                    pressed_digit = event.key - pygame.K_0
                    i = int((self.pos[0] - BOARD_TOPLEFT_X)//CELL_WIDTH)
                    j = int((self.pos[1] - BOARD_TOPLEFT_Y)//CELL_HEIGHT)

                    if not Board.puzzle[i][j].fixed:
                        for k in range(LEN_BOARD):
                            if Board.puzzle[i][j].value == Board.puzzle[i][k].value and k != j:
                                Board.puzzle[i][k].cell_colour = WHITE
                            if Board.puzzle[i][j].value and Board.puzzle[i][k].value == Board.puzzle[i][j].value:
                                Board.puzzle[i][k].temp_cell_colour = CERULEAN

                            if Board.puzzle[i][j].value == Board.puzzle[k][j].value and k != i:
                                Board.puzzle[k][j].cell_colour = WHITE
                            if Board.puzzle[i][j].value and Board.puzzle[k][j].value == Board.puzzle[i][j].value:
                                Board.puzzle[k][j].temp_cell_colour = CERULEAN

                        for m in range(i // ROOT_BOARD * ROOT_BOARD, i // ROOT_BOARD * ROOT_BOARD + ROOT_BOARD):
                            for n in range(j // ROOT_BOARD * ROOT_BOARD, j // ROOT_BOARD * ROOT_BOARD + ROOT_BOARD):
                                if Board.puzzle[i][j].value == Board.puzzle[m][n].value and m != i and n != j:
                                    Board.puzzle[m][n].cell_colour = WHITE
                                if Board.puzzle[i][j].value and Board.puzzle[m][n].value == Board.puzzle[m][n].value:
                                    Board.puzzle[m][n].temp_cell_colour = CERULEAN

                        for row in Board.puzzle:
                            for cell in row:
                                if Board.puzzle[i][j].value and Board.puzzle[i][j].value == cell.value and cell.temp_cell_colour != CERULEAN:
                                    cell.temp_cell_colour = WHITE

                        Board.puzzle[i][j].value = pressed_digit
                        cell = Board.puzzle[i][j]
                        self.logic.is_right_value(i, j, cell)


