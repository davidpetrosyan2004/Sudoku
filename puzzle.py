import copy
from random import randint
from random import sample

class Puzzle:
    freq_nums = 100
    base = 3
    side = base * base
    @classmethod
    def generate_unsolved_puzzle(cls, solved_puzzle):
        unsolved_puzzle = copy.deepcopy(solved_puzzle)
        for i in range(cls.freq_nums):
            j = randint(0, cls.side-1)
            k = randint(0, cls.side-1)
            unsolved_puzzle[j][k] = 0

        return unsolved_puzzle




    @classmethod
    def generate_solved_puzzle(cls):
        base = 3
        side = base * base

        def pattern(r, c):
            return (base * (r % base) + r // base + c) % side

        def shuffle(s):
            return sample(s, len(s))

        rBase = range(base)
        rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums = shuffle(range(1, base * base + 1))

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        return board


if __name__ == "__main__":
    board = Puzzle.generate_solved_puzzle()
    board1 = Puzzle.generate_unsolved_puzzle(board)
    for row in board1:
        print(row)
    print("\n")
    for row in board:
        print(row)

