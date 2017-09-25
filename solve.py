import numpy as np
import pycosat, math, random, os


def main():
    sudokus = np.load('sudoku.npy')

    with open('rules.cnf', 'r') as f:
        content = [x.strip() for x in f.readlines()]

        cnf = []
        for rule in content:
            literals = [int(x) for x in rule.split(' ')]
            cnf.append(literals)


    num_givens = 33
    proportion_in_box = 0

    for i, sudoku in enumerate(sudokus):
        # Calculate no of givens
        gib = round(num_givens*proportion_in_box)
        gob = num_givens - gib

        reduce(sudoku, gib, gob)

        givens = encode_givens(sudoku)
        rules = cnf + givens

        os.system('clear')
        print('{}/{}\nInside: {}\nOutside: {}'.format(i+1, len(sudokus), gib, gob))
        draw(sudoku)

        solution = pycosat.solve(rules, verbose=1)

        if solution != 'UNSAT':
            decode(solution)
        else:
            print('NOOOOO')

        if i > 1:
            break


def decode(solution):
    matrix = np.zeros((21, 21), dtype=np.int)

    for assignment in solution:
        if assignment > 0:
            number = str(assignment)

            if len(number) == 4:
                y = int(number[:1]) - 1
                x = int(number[1:3]) - 1
                n = int(number[-1])
                matrix[x,y] = n

            if len(number) == 5:
                y = int(number[:2]) - 1
                x = int(number[2:4]) - 1
                n = int(number[-1])
                matrix[x,y] = n


    draw(matrix)

def encode_givens(sudoku):
    cnf = []

    for column in range(sudoku.shape[0]):
        for row in range(sudoku.shape[1]):
            number = sudoku[column, row]
            if number != 0:
                cnf.append([int('{0:0>2}{1:0>2}{2}'.format(row+1, column+1, number))])

    return cnf

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
