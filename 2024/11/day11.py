# This time Part 2 demanded basically to improve efficiency in Part 1, so the functions of Part 2 are just better than the
# ones of Part 1. I have still included them because those are the ones I used first to solve Part 1.

# Part 1

# 2 things are wrong here: 1) Despite what the text may seem to say, the order of the stones does not matter, so 
# inserting the new stones in their rigth place is not needed, they could just be appended to the end. 2) As I realized 
# in part 2, i am repeating a lot of operations unneceserally, making this function unefficient.

# Given a list of stones, returns the resulting list of stones after the blink changes
def blink(stones: list[str]) -> list[str]:
    stones_after_blink: list[str] = list()
    i: int = 0
    for stone in stones:
        if stone == "0":
            stones_after_blink.insert(i, "1")
            i += 1
        elif len(stone) % 2 == 0:
            mid: int = len(stone) // 2
            stones_after_blink.insert(i, stone[:mid])
            trim: str = stone[mid:].lstrip("0")
            if trim:
                stones_after_blink.insert(i + 1, trim)
            else:
                stones_after_blink.insert(i + 1, "0")
            i += 2
        else:
            stones_after_blink.insert(i, str(int(stone) * 2024))
            i += 1
    return stones_after_blink

# It just repeats the previous function n times and counts the number of blocks (the length of the list)
def stones_after_n_blinks(initial_arrangement: list[str], n: int) -> int:
    stones = initial_arrangement.copy()
    for i in range(n):
        stones: list[str] = blink(stones)
    return len(stones)

# Part 2

# I struggled a while with this part, trying to find a formula or a way to predict of many stones would a single-digit stone
# produce in n blinks. In the end, all I needed was to stop repeating operations and instead of a list of stones 
# (numbers), using a dictionary with keys the numbers and values the number of stones with that number (number of ocurrences)

# Given a list of stones, returns a dictionary where 'key = number, value = number of stones with that number' (multiplicity)
def dict_multiplicity(stones : list[str]) -> dict[str, int]:
    unique_values = list(set(stones))
    mult_dict = dict()
    for value in unique_values:
        mult_dict[value] = stones.count(value)
    return mult_dict

# This is the upgrade from Part 1. Becase of the dictionary use with unique numbers, we are appliying the rule 
# to only one appearance of the number in each step, and carrying over / updating the number of ocurrencess of 
# that number, which results in a big boost in efficiency.
def blink2(initial_arrangement: dict[str, int])  -> dict[str, int]:
    stones_after_blink = dict()
    for value in initial_arrangement:
        if value == "0":
            increment = initial_arrangement.get("0", 0)
            new_value = ["1"]
        elif len(value) % 2 == 0:
            mid: int = len(value) // 2
            trim: str = value[mid:].lstrip("0")
            increment: int = initial_arrangement.get(value, 0)
            value1: str = value[:mid]
            if trim:
                value2: str = trim
            else:
                value2 = "0"
            new_value: list[str] = [value1, value2]
        else:
            increment = initial_arrangement.get(value, 0)
            new_value = [str(int(value) * 2024)] 
        for item in new_value:
            if item in stones_after_blink:
                stones_after_blink[item] += increment
            else:
                stones_after_blink[item] = increment
    return stones_after_blink

# Repeats previous function n times and then counts the number of stones (sum of all values in the dictionary)
def count_n_blinks(stones: list[str], n: int) -> int:
    initial_arrangement: dict[str, int] = dict_multiplicity(stones)
    for _ in range(n):
        initial_arrangement = blink2(initial_arrangement)
    count = 0
    for key in initial_arrangement:
        count += initial_arrangement[key]
    return count

# Run

def main() -> None:
    with open(r"./2024/11/input.txt") as myfile:
        stones: list[str] = myfile.read().strip().split()

    print(f" Numer of stones after blinking 25 times: {stones_after_n_blinks(stones, 25)}") # Part 1 original 
    print(f" Numer of stones after blinking 25 times: {count_n_blinks(stones, 25)}") # Part 1 with Part 2 upgrade
    print(f" Numer of stones after blinking 75 times: {count_n_blinks(stones, 75)}") # Part 2

if __name__ == "__main__":
    main()