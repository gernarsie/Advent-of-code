with open(r"./2024/02/input.txt") as myfile:
    lines: list[str] = myfile.read().splitlines()

values: list[list[int]] = [[int(i) for i in line.split(" ")] for line in lines]

# Condition 1: Checks if list is all increasing or all decreasing by comparing it to the sorted versions
def inc_or_dec(vals) -> bool:
    return vals == sorted(vals) or vals == sorted(vals, reverse=True)

# Condition 2: Makes a list with the differences of adjacent elements, turns it into a set (so we get rid of copies) and checks if
# its elements are only 1, 2 or 3
def differ(vals) -> bool: 
    return set([abs(vals[i]-vals[i+1]) for i in range(len(vals)-1)]).issubset({1,2,3})

# Check conditions 1 and 2 (if there is only 1 value then both are true)
def check(vals) -> bool:
    if len(vals) == 1:
        return True
    else: 
        return inc_or_dec(vals) and differ(vals)

def safe_reports(vals_list) -> int:
    safe_reports = 0
    for vals in vals_list:
        if check(vals):
            safe_reports += 1
    return safe_reports

def values_dampened(vals) -> list:
    return [vals[:i] + vals[i+1:] for i in range(len(vals))]

# I realized later that the first "check(vals)" is redundant, since for a list of values for which bot conditions are true,
# the same is for the list without the first or last item
def problem_dampener(vals_list) -> int:
    safe_reports = 0
    for vals in vals_list:
        if check(vals):
            safe_reports += 1
        elif any([check(vals_damp) for vals_damp in values_dampened(vals)]):
            safe_reports += 1
    return safe_reports
    

def main() -> None:
    print(f"Number of safe reports: {safe_reports(values)}") # Problem 1
    print(f"Number of safe reports using The Problem Dampener: {problem_dampener(values)}") # Problem 2

if __name__ == "__main__":
    main()