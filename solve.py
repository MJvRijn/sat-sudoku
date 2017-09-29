import numpy as np
import pycosat, math, random, os, argparse, ast


def main():
    num_givens, proportion_in_box, arrangements = process_arguments()

    sudokus = np.load('sudoku.npy')

    with open('rules.cnf', 'r') as f:
        content = [x.strip() for x in f.readlines()]

        cnf = []
        for rule in content:
            literals = [int(x) for x in rule.split(' ')]
            cnf.append(literals)

    # Iterate over parameters
    for givens in num_givens:
        for proportion in proportion_in_box:
            inside = round(givens*proportion)
            outside = givens - inside

            # Generate 20 configurations of givens to keep
            samples = []
            for i in range(arrangements):
                samples.append(select_givens(inside, outside))

            for i, sudoku in enumerate(sudokus):
                if i > 0:
                    continue
                for j, sample in enumerate(samples):
                    # Prepare data
                    testdoku = reduce(sudoku, sample)
                    givens_cnf = encode_givens(testdoku)
                    rules = cnf + givens_cnf

                    # Solve sudoku
                    print('{{"givens":{}, "proportion": {}, "inside":{}, "outside":{}, "sudoku":{} "arrangement":{}}}'.format(givens, proportion, inside, outside, i, j))
                    solution = pycosat.solve(rules, verbose=1)

                    if solution == 'UNSAT':
                        print('Unsatifiable, BUG?')


def process_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--givens', type=str, metavar='[MIN, MAX, N]', help='range of givens to test')
    parser.add_argument('-a', '--arrangements', type=int, metavar='N', help='number of arrangements per conf')
    parser.add_argument('-p', '--proportions', type=str, metavar='[MIN, MAX, N]', help='range of proportions to test')
    args = parser.parse_args()

    if args.givens:
        givens = ast.literal_eval(args.givens)
    else:
        givens = [200, 200, 1]

    givens = np.linspace(givens[0], givens[1], num = givens[2], dtype=np.int)

    if args.proportions:
        proportions = ast.literal_eval(args.proportions)
    else:
        proportions = [0.1, 0.1, 1]

    proportions = np.linspace(proportions[0], proportions[1], num = proportions[2])

    if args.arrangements:
        arrangements = args.arrangements
    else:
        arrangements = 20

    return givens, proportions, arrangements

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

    return matrix

def encode_givens(sudoku):
    cnf = []

    for column in range(sudoku.shape[0]):
        for row in range(sudoku.shape[1]):
            number = sudoku[column, row]
            if number != 0:
                cnf.append([int('{0:0>2}{1:0>2}{2}'.format(row+1, column+1, number))])

    return cnf

def select_givens(inside, outside):
    DIM = 21

    n_in = 0
    n_out = 0
    keep = []

    while True:
        # Select square at random
        i = random.randrange(0, DIM*DIM)

        x = i // DIM
        y = i % DIM

        # Check whether already chosen
        if (x, y) in keep:
            continue

        # Check whether outside puzle (top/bottom)
        if 9 <= x <= 11 and (0 <= y <= 5 or 15 <= y <= 20):
            continue

        # Check whether outside puzle (left/right)
        if 9 <= y <= 11 and (0 <= x <= 5 or 15 <= x <= 20):
            continue

        # Check whether inside overlap_sudokus
        if (6 <= x <= 8 or 12 <= x <= 14) and (6 <= y <= 8 or 12 <= y <= 14):
            if n_in < inside:
                n_in += 1
                keep.append((x, y))
        else:
            if n_out < outside:
                n_out += 1
                keep.append((x, y))

        if n_in == inside and n_out == outside:
            return keep

def reduce(sudoku, givens):
    newdoku = np.zeros((21, 21), dtype=np.int)

    for x in range(sudoku.shape[0]):
        for y in range(sudoku.shape[1]):
            if (x, y) in givens:
                newdoku[x, y] = sudoku[x, y]

    return newdoku

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
