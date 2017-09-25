import numpy as np
import os, time, random

def main():
    givens = 333
    proportion_in_box = 0

    sudokus = np.load('sudoku.npy')

    for i, sudoku in enumerate(sudokus):
        # Calculate no of givens
        gib = round(givens*proportion_in_box)
        gob = givens - gib

        reduce(sudoku, gib, gob)

        os.system('clear')
        print('{}/{}\nInside: {}\nOutside: {}'.format(i+1, len(sudokus), gib, gob))
        draw(sudoku)
        # time.sleep(0.5)

def reduce(sudoku, inside, outside):
    n_in = 0
    n_out = 0
    keep = []

    while True:
        # Select square at random
        i = random.randrange(0, sudoku.size)

        x = i // sudoku.shape[0]
        y = i % sudoku.shape[1]

        if sudoku[x, y] != 0 and (x, y) not in keep:
            # Inside
            if (6 <= x <= 8 or 12 <= x <= 14) and (6 <= y <= 8 or 12 <= y <= 14):
                if n_in < inside and (x, y):
                    n_in += 1
                    keep.append((x, y))

            # Outside
            else:
                if n_out < outside:
                    n_out += 1
                    keep.append((x, y))

        if n_in == inside and n_out == outside:
            break

    # Filter
    for x in range(sudoku.shape[0]):
        for y in range(sudoku.shape[1]):
            if (x, y) not in keep:
                sudoku[x, y] = 0







def draw(matrix):
    output = ''
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            n = matrix[x, y]
            if n == 0:
                if (6 <= x <= 8 or 12 <= x <= 14) and (6 <= y <= 8 or 12 <= y <= 14):
                    output += ' -'
                elif ((0 <= x <= 5 or 15 <= x <= 20) and (9 <= y <= 11)) or ((0 <= y <= 5 or 15 <= y <= 20) and (9 <= x <= 11)):
                    output += '  '
                else:
                    output += ' .'
            else:
                output += ' ' + str(n)
        output += '\n'

    print(output)

if __name__ == '__main__':
    main()
