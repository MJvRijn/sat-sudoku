import argparse, random, os
import numpy as np

positions = [(0,0), (-2, -2), (-2, 2), (2, 2), (2, -2)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', type=int, required=True, metavar='N', help='number of sudokus')
    parser.add_argument('-o', '--output', type=str, required=True, metavar='NAME', help='name of output')
    args = parser.parse_args()

    name = args.output
    N = args.number

    overlapping_sudokus = []

    i = 0
    while True:
        sudokus = []
        for px, py in positions:
            sudoku = init_overlap(px, py, sudokus)
            if not solve(sudoku):
                break
            sudokus.append((px, py, sudoku))

        matrix = overlap_sudokus(sudokus)

        # Progress
        i += 1
        os.system('clear')
        print('{}/{}\n'.format(i, N))
        draw(matrix)

        overlapping_sudokus.append(matrix)

        if len(overlapping_sudokus) >= N:
            break

    np.save('{}.npy'.format(name), np.array(overlapping_sudokus))

def init_overlap(px, py, sudokus):
    newdoku = np.zeros(shape=(9,9), dtype=np.int)
    for px2, py2, sudoku in sudokus:
        for x in range(9):
            for y in range(9):
                i = x + 3*(px-px2)
                j = y + 3*(py-py2)

                if 0 <= i < 9 and 0 <= j < 9:
                    newdoku[x, y] = sudoku[i, j]

    return newdoku

def valid_insertion(sudoku, x, y, n):
    if not all([n != sudoku[x][i] for i in range(9)]): # Row
        return False

    if not all([n != sudoku[i][y] for i in range(9)]): # Column
        return False

    box_origin_x = 3*(x//3)
    box_origin_y = 3*(y//3)
    for i in range(box_origin_x, box_origin_x+3):
        for j in range(box_origin_y, box_origin_y+3):
            if sudoku[i][j] == n:
                return False
    return True

def next_empty(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y

    # None empty, sudoku complete
    return None, None


def solve(sudoku):
    x, y = next_empty(sudoku)
    if x == None:
        return True

    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for n in numbers:
        if valid_insertion(sudoku, x, y, n):
            sudoku[x][y] = n

            if solve(sudoku):
                return True

            # Conflict, try next number
            sudoku[x][y] = 0

    return False

def save(sudokus, positions):
    pass

def overlap_sudokus(sudokus):
    min_x = max_x = min_y = max_y = 0

    for px, py, _ in sudokus:
        if px < min_x:
            min_x = px
        if px > max_x:
            max_x = px
        if py < min_y:
            min_y = py
        if py > max_y:
            max_y = py

    matrix = np.zeros((3*(max_x-min_x)+9, 3*(max_y-min_y)+9), dtype=np.int)

    for px, py, sudoku in sudokus:
        for x in range(9):
            for y in range(9):
                i = x + (px-min_x)*3
                j = y + (py-min_y)*3
                matrix[i, j] = sudoku[x, y]

    return matrix


def draw(matrix):
    output = ''
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            n = matrix[x, y]
            if n == 0:
                output += '  '
            else:
                output += ' ' + str(n)
        output += '\n'

    print(output)

if __name__ == '__main__':
    main()
