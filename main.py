import pygame
from controls import Controls
from settings import *
from drawing import Drawing
from board import Board, Board1
from logic import Logic

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
logic = Logic()
controls = Controls(logic)
drawing = Drawing(sc)
board = Board(BOARD)
board1 = Board1(SOLVED_BOARD)
pygame.font.init()

def run():
    while True:
        controls.events()
        sc.fill(BLACK)
        drawing.background()
        drawing.update_cells(board)
        # drawing.update_solved_cells(board1)
        drawing.board()
        if logic.is_game_over():
            drawing.game_over()
        if logic.is_game_won(board):
            drawing.game_won()
        drawing.puzzle_level()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    run()




