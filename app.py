import os
import time
from copy import deepcopy


def count_neighbors(matrix, row, col):
    num = 0
    for x in range(-1, 2):
        if (row + x >= 0) and (row + x < len(matrix)):
            for y in range(-1, 2):
                if (col + y >= 0) and (col + y < len(matrix[0])):
                    if not ((x == 0) and (y == 0)):
                        num += matrix[row + x][col + y]

    return num


def count_population(matrix):
    return sum([row.count(1) for row in matrix])


def clear():
    os.system("clear" if os.name == "posix" else "cls")


def display(matrix):
    for col in range(0, len(matrix[0]) + 2):
        print("_", end="")
    print("")

    for row in range(0, len(matrix)):
        print("|", end="")
        for col in range(0, len(matrix[0])):
            if matrix[row][col]:
                print("O", end="")
            else:
                print(" ", end="")
        print("|")

    for col in range(0, len(matrix[0]) + 2):
        print("_", end="")
    print("")


def main(matrix):
    clear()
    population = count_population(matrix)
    print("Population: {}".format(population))
    display(matrix)
    time.sleep(0.25)

    step = 0
    repeats = 0
    while population > 0 and repeats < MAX_REPEATS and step < MAX_STEPS:
        new_matrix = deepcopy(matrix)
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                neighbors = count_neighbors(matrix, row, col)
                if neighbors == 3:
                    new_matrix[row][col] = 1
                elif matrix[row][col] == 1 and neighbors == 2:
                    new_matrix[row][col] = 1
                else:
                    new_matrix[row][col] = 0

        if new_matrix == matrix:
            repeats += 1
        else:
            repeats = 0

        clear()
        population = count_population(new_matrix)
        print("Population: {}".format(population))
        display(new_matrix)
        time.sleep(0.25)

        matrix = deepcopy(new_matrix)

        step += 1


start_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

MAX_STEPS = 500
MAX_REPEATS = 5

if __name__ == "__main__":
    main(start_matrix)
