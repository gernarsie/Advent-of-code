from typing import Literal
import numpy as np
from numpy.typing import NDArray

# Part 1:

# Finds the guard's starting point: '^'
def guard_start(arr: NDArray) -> tuple[int, int]:
    start_i, start_j = np.where(arr == "^")
    return (int(start_i[0]), int(start_j[0]))

# Gives the guard's next point based on the direction (0 up, 1 right, 2 down, 3 left)
def guard_next_step(i: int, j: int, direction: int) -> tuple[int, int]:
    direction = direction % 4
    match direction:
        case 0:
            return (i - 1, j)
        case 1:
            return (i, j + 1)
        case 2:
            return (i + 1, j)
        case 3:
            return (i, j - 1)
        case _: 
            print("Error in guard next step")
            return(i,j)

# Makes the guard path marking it with 'X' and returns the number of points and the path taken 
# (the path will be used in Part 2)
def guard_path(arr: NDArray, start: tuple[int, int]) -> tuple[int, list[tuple[int, int]]]:
    n, m = np.shape(arr)
    i = start[0]
    j = start[1]
    direction: int = 0
    path: list[tuple[int,int]] = []
    while True:
        next_i, next_j = guard_next_step(i,j, direction)
        arr[i,j] = "X"
        path.append((i,j))
        if (next_i == -1) or (next_i == n) or (next_j == -1) or (next_j == m):
            break
        elif arr[next_i,next_j] == "#":
            direction += 1
            direction = direction % 4
            path = path[:-1]
        else:
            i: int = next_i
            j: int = next_j
    return (np.count_nonzero(arr == "X"), path)

# Part 2:

# Given a disposition, checks if the guard will stay in a loop or will exit the array
# (this is very similar to the previous function, so it should be possible to combine them both, but
# since it was already done it was quicker to just remake it again for this specific purpose)
def guard_check_loop(arr: NDArray, start: tuple[int, int]) -> bool:
    n, m = np.shape(arr)
    i = start[0]
    j = start[1]
    direction: int = 0
    loop_check: set = set()
    while True:
        next_i, next_j = guard_next_step(i,j, direction)
        loop_check.add((i,j,direction))
        if (next_i,next_j,direction) in loop_check:
            loop = True
            break
        if (next_i == -1) or (next_i == n) or (next_j == -1) or (next_j == m):
            loop = False
            break
        elif arr[next_i,next_j] == "#":
            direction += 1
            direction = direction % 4
        else:
            i: int = next_i
            j: int = next_j
    return loop

# For each place in the guard's path (calculated in Part 1), checks if putting an obstacle there will 
# create a loop (using the previous function) and counts the number of possible places
def guard_loop_count(arr: NDArray, path: list[tuple[int, int]]) -> int:
    start: tuple[int, int] = path[0]
    loop_count: int = 0
    loop_try: NDArray = np.copy(arr)
    for place in set(path):
        loop_try[place[0], place[1]] = "#"
        if guard_check_loop(loop_try, start):
            loop_count += 1
        loop_try[place[0], place[1]] = "."
    return loop_count

def main() -> None:

    # Opening file
    with open(r"./2024/06/input.txt") as myfile:
        lines: list = []
        for line in myfile:
            lines.append(list(line.rstrip('\n')))

    arr: NDArray = np.array(lines) # Creating the array
    start: tuple[int, int] = guard_start(arr) # Getting the start point 
    part1, path = guard_path(np.copy(arr), start) # Separating Part 1 solution and the path

    print(f"The guard will travel {part1} positions") # Part 1
    print(f"There are {guard_loop_count(np.copy(arr), path)} possible positions for the obstruction") # Part 2 (takes a bit longer than part 1)

if __name__ == "__main__":
    main()