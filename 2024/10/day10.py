import numpy as np
from numpy.typing import NDArray

# Part 1

# Given a point, returns the list of adjacent points with value increase 1:
def possible_moves(arr: NDArray, position: tuple[int, int]) -> list[tuple[int, int]]:
    n, m = np.shape(arr)
    i, j = position
    value: int = arr[i, j]
    i_limit_inf = -1
    i_limit_sup = 1
    j_limit_inf = -1
    j_limit_sup = 1
    if i == 0:
        i_limit_inf = 0
    elif i == n - 1:
        i_limit_sup = 0
    if j == 0:
        j_limit_inf = 0
    elif j == m -1:
        j_limit_sup = 0
    return [(i + k, j) for k in {i_limit_inf, i_limit_sup} if (arr[i + k, j] == value + 1)] + [
        (i, j + l) for l in {j_limit_inf, j_limit_sup} if (arr[i, j + l] == value + 1)
    ]

# Given a start (point with value 0), applies the previous function, then again to those points until its
# done 9 times. Then counts the unique points (hence the set use), which should be the points with value 9 that have been reached
def trailhead_score(arr: NDArray, start: tuple[int, int]) -> int:
    actual_points: set[tuple[int, int]] = {start}
    for _ in range(9):
        new_points: set[tuple[int, int]] = set()
        for point in actual_points:
            new_points.update(set(possible_moves(arr, point)))
        actual_points = new_points.copy()
    return len(actual_points)

# Finds all the trailheads (points with value 0), calculate their scores and sum them
def total_score_sum(arr: NDArray) -> int:
    zeros = np.where(arr == 0)
    trailheads: list[tuple[int, int]] = [(int(i), int(j)) for i, j in zip(zeros[0], zeros[1])]
    total: int = 0
    for point in trailheads:
        total += trailhead_score(arr, point)
    return total

# Part 2

# I do not know why but I struggled with the rating until I manage to get the 'trailhead_rating' function. Then I realised 
# I could just have switched the set in the 'trailhead_score' function with list and would have gotten what I needed. The 
# second function would be the same but using the updated score/rating calculation.

# This function does the same as 'trailhead_score' but counts how many times we reach a point with value 9 without unicity.
# As I said, using 'trailhead_score' with lists insead of sets would be the same, and viceversa you could chage this to 
# calculate the score.
def trailhead_rating(arr: NDArray, start: tuple[int, int]) -> int:
    points: list[tuple[int, int]] = [start]
    rating: int = 0
    while True:
        if points == []:
            break
        point: tuple[int, int] = points.pop()
        if arr[point[0], point[1]] == 9:
                rating += 1
        for move in possible_moves(arr, point):
                points.append(move)
    return rating

# Same as 'total_score_sum' but using 'trailhead_rating' instead of 'total_score_sum'
def total_rating_sum(arr: NDArray) -> int:
    zeros = np.where(arr == 0)
    trailheads: list[tuple[int, int]] = [(int(i), int(j)) for i, j in zip(zeros[0], zeros[1])]
    total: int = 0
    for point in trailheads:
        total += trailhead_rating(arr, point)
    return total

# Run

def main() -> None:
    # Opening file
    with open(r"./2024/10/input.txt") as myfile:
        lines: list = []
        for line in myfile:
            lines.append([int(x) for x in line.rstrip('\n')])

    arr: NDArray = np.array(lines) # Creating the array

    print(f"Sum of the scores of all trailheads: {total_score_sum(arr)}") # Part 1
    print(f"Sum of the ratings of all trailheads: {total_rating_sum(arr)}") # Part 2

if __name__ == "__main__":
    main()