import re

with open(r"./2024/03/input.txt") as myfile:
    corrupted_memory: str = myfile.read()

# Problem 1
# Filtering
regex: str = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
mul_instructions: list[str] = re.findall(regex, corrupted_memory)

# Dropping parenthesis and "mul"
def mul_numbers(mul_list: list[str]) -> list[list[str]]:
    return [mul[4:][:-1].split(",") for mul in mul_list]

# Sum of products
def mul_sum_prod(numbers: list[list[str]]) -> int:
    return sum([int(i[0])*int(i[1]) for i in numbers])

# Solution
mul_solution: int = mul_sum_prod(mul_numbers(mul_instructions))

# Problem 2
# New filter
regex_conditional =  regex + r"|do\(\)|don't\(\)"
mul_instructions_conditional: list[str] = re.findall(regex_conditional, corrupted_memory)

# Conditional:
def mul_pass(mylist: list, char, cond: bool) -> None:
    if cond:
        mylist.append(char)

# Drop all "muls" between don'ts and dos:
def mul_conditional(mul_list: list[str]) -> list[str]:
    new_mul_list: list = []
    cond = True
    for inst in mul_list:
        if inst == "don't()":
            cond = False
        elif inst == "do()":
            cond = True
        else:
            mul_pass(new_mul_list, inst, cond)
    return new_mul_list

# Solution
mul_conditional_solution: int = mul_sum_prod(mul_numbers(mul_conditional(mul_instructions_conditional)))

# Run

def main() -> None:
    print(f"Sum of all uncorrupted multiplications: {mul_solution}") # Problem 1
    print(f"Sum of all uncorrupted enabled multiplications: {mul_conditional_solution}") # Problem 2

if __name__ == "__main__":
    main()