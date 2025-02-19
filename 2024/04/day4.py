import numpy as np
from numpy.typing import NDArray
import re


# Create numpy array:
def create_arr(lines_list: list[str]) -> NDArray:
    return np.array([list(line) for line in lines_list])

# Part 1

# Count "XMAS" in a list of lines:
def count_line(line: list[str]) -> int:
    regex = r"(?=XMAS|SAMX)"
    xmas_count: int = 0
    for item in line:
        xmas_count += len(re.findall(regex, item))
    return xmas_count

# Get a list of all the diagonals of the array as concatenated strings
def get_diagonals(arr: NDArray) -> list[str]:
    n, m = arr.shape
    diagonals_array: list[list] = [item.tolist() for item in [np.diagonal(arr, i) for i in range(-n+1,n, 1)]]
    diagonals: list[str] = ["".join(line) for line in diagonals_array]
    return diagonals

# Count all the "XMAS" 
def count_xmas_total(arr: NDArray) -> int:
    n, m = arr.shape
    arr_flip_vertical: NDArray = np.fliplr(arr)
    horizontal: list[str] = ["".join([arr[i,j] for j in range(m)]) for i in range(n)]
    vertical: list[str] = ["".join([arr[i,j] for i in range(n)]) for j in range(m)]
    diagonals_right: list[str] = get_diagonals(arr)
    diagonals_left: list[str] = get_diagonals(arr_flip_vertical)
    return count_line(horizontal) + count_line(vertical) + count_line(diagonals_left) + count_line(diagonals_right)

# Part 2 

# Given 2 chars checks if they are the extremes of "MAS"
def mas_check(char1: str, char2: str) -> bool:
    if char1 == "M" and char2 == "S":
        return True
    elif char1 == "S" and char2 == "M":
        return True
    else:
        return False

# Counts the "MAS" in X-shape
def mas_count(arr: NDArray) -> int:
    n, m = arr.shape
    mas_count: int = 0
    for i in range(1,n-1):
        for j in range(1,m-1):
            if arr[i,j] == "A" and mas_check(arr[i-1,j-1], arr[i+1,j+1]) and mas_check(arr[i-1,j+1], arr[i+1,j-1]):
                mas_count += 1
    return mas_count

def main() -> None:

    # Open file
    with open(r"./2024/04/input.txt") as myfile:
        lines: list[str] =  myfile.read().splitlines()

    arr: NDArray = create_arr(lines)

    print(f"'XMAS' appears {count_xmas_total(arr)} times") # Part 1
    print(f"There are {mas_count(arr)} 'X-MAS") # Part 2
    

if __name__ == "__main__":
    main()