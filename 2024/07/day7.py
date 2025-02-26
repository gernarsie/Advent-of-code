# Part 1:

# Check if one equation can be true inserting operators
# Each step of the loop we take the previos values, multiply and sum each with the new one 
# and repeat until we finish. Then we check if our target value appears in the last iteration 
def check_equation(value: int, options: list[int]) -> bool:
    if len(options) > 1:
        previous_results: list[list[int]] = [[options[0]]]
        for option in options[1:]:
            mult: list[int] = [option * previous for previous in previous_results[-1]]
            sum: list[int] = [option + previous for previous in previous_results[-1]]
            previous_results.append(sum+mult)
        if value in previous_results[-1]:
            return True
        else:
            return False
    else:
        return options[0] == value

# Sums the values of all true equations (using the previous function)
def total_calibration(equations: list[tuple[int, list[int]]]) -> int:
    calibration_count: int = 0
    for equation in equations:
        value: int = equation[0]
        numbers: list[int]= equation[1]
        if check_equation(value, numbers):
            calibration_count += value
    return calibration_count

# Part 2:

# We add the new operation (concatenation) to our previous 'check_equation' function
def check_equation2(value: int, options: list[int]) -> bool:
    if len(options) > 1:
        previous_results: list[list[int]] = [[options[0]]]
        for option in options[1:]:
            mult: list[int] = [previous * option for previous in previous_results[-1]]
            sum: list[int] = [previous + option  for previous in previous_results[-1]]
            concat: list[int] = [int(str(previous) + str(option)) for previous in previous_results[-1]]
            previous_results.append(sum + mult + concat)
        if value in previous_results[-1]:
            return True
        else:
            return False
    else:
        return options[0] == value

# We repeat the count as with 'total_calibration' but using our new 'check_equation2'
def total_calibration2(equations: list[tuple[int, list[int]]]) -> int:
    calibration_count: int = 0
    for equation in equations:
        value: int = equation[0]
        numbers: list[int]= equation[1]
        if check_equation2(value, numbers):
            calibration_count += value
    return calibration_count

# Run

def main() -> None:
    # Read input file and store equations as a list of tuples of the form '(value, [numbers])'
    with open(r"./2024/07/input.txt") as myfile:
        equations: list[tuple[int, list[int]]] = list()
        for line in myfile:
            line_list: list[str] = line.split()
            equations.append((int(line_list[0][:-1]), [int(x) for x in line_list[1:]]))

    print(f"Total calibration result: {total_calibration(equations)}") # Part 1
    print(f"Total calibration result with 3 operators: {total_calibration2(equations)}") # Part 2 (takes a bit longer than Part 1)


if __name__ == "__main__":
    main()