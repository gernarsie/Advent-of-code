import numpy as np
from numpy.typing import NDArray

# Part 1

# Get a dictionary where the keys are the antenna frequency and the values a list of the coordinates of all 
# antennas with that frequency (as tuples)
def get_antennas(arr: NDArray) -> dict[str, list[tuple[int, int]]]:
    antennas: dict[str, list[tuple[int,int]]] = dict()
    n, m = np.shape(arr)
    for i in range(n):
        for j in range(m):
            if  arr[i,j] != '.' and arr[i,j] not in antennas:
                antennas[str(arr[i,j])] =  [(int(x), int(y)) for x,y in zip(np.where(arr == arr[i,j])[0], np.where(arr == arr[i,j])[1])]
    return antennas

# Given 2 points in the array, it calculates the distance between them and then the 2 possible 'antinodes' (points
# that are in a line with them and twice as distance from one than the other, i. e. points in the same line as
# our input points at the calculated distance from the first and the second one
def calculate_antinodes(point1: tuple[int, int], point2: tuple[int, int]) -> list[tuple[int, int]]:
    dist: tuple[int, int] = (point2[0] - point1[0], point2[1] - point1[1])
    antinode1 = (point1[0] - dist[0], point1[1] - dist[1])
    antinode2 = (point2[0] + dist[0], point2[1] + dist[1])
    return [antinode1, antinode2]

# Puts an # in each antinode place and then counts them. The 'updated_model' is for diferentiating
# between part 1 and part 2 (which use different 'calculate_antinodes' functions) 
def count_antinodes(arr: NDArray, updated_model: bool = False) -> int:
    antennas: dict[str, list[tuple[int, int]]] = get_antennas(arr)
    n, m = np.shape(arr)
    for antenna, coordinates in antennas.items():
        k: int = len(coordinates)
        pairs: list[tuple[tuple[int, int], tuple[int, int]]] = [(coordinates[i], coordinates[j]) for i in range(k) for j in range(i+1,k)]
        for item in pairs:
            if updated_model:
                antinodes: list[tuple[int, int]] = calculate_antinodes2(item[0], item[1], (n,m))
            else:
                antinodes: list[tuple[int, int]] = calculate_antinodes(item[0], item[1])
            for antinode in antinodes:
                if -1 < antinode[0] < n and -1 < antinode[1] < m:
                    arr[antinode[0], antinode[1]] = "#"
    return np.count_nonzero(arr == "#")

# Part 2

# Instead of just 2 points, we rewrite 'calculate_antinodes' so it gives as a list of possible points (all the line)
# (bounded by the array size) that we will later see if they get out of bounds or not
def calculate_antinodes2(point1: tuple[int, int], point2: tuple[int, int], limits: tuple[int, int]) -> list[tuple[int, int]]:
    dist: tuple[int, int] = (point2[0] - point1[0], point2[1] - point1[1])
    limit: int = max(limits)
    antinodes: list[tuple[int, int]] = [(point1[0] + k * dist[0], point1[1] + k* dist[1]) for k in range(-limit, limit)]
    return antinodes

# Run

def main() -> None:
    # Opening file
    with open(r"./2024/08/input.txt") as myfile:
        lines: list = []
        for line in myfile:
            lines.append(list(line.rstrip('\n')))

    arr: NDArray = np.array(lines) # Creating the array

    print(f"Number of unique locations containing antinodes: {count_antinodes(np.copy(arr))}") # Part 1
    print(f"Number of unique locations containing antinodes with the updated model: {count_antinodes(np.copy(arr), updated_model= True)}") # Part 2

if __name__ == "__main__":
    main()