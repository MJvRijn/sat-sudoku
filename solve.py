import numpy as np
import pycosat, math


def main():
    sudokus = np.load('sudoku.npy')

    with open('squares.cnf', 'r') as f:
        content = [x.strip() for x in f.readlines()]

        cnf = []
        for rule in content:
            literals = [int(x) for x in rule.split(' ')]
            cnf.append(literals)


    solution = pycosat.solve(cnf, verbose=1)

    if solution != 'UNSAT':
        decode(solution)


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
