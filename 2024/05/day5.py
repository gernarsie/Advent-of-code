import csv

# Transforming updates and rules into list of tuples (and from str to int)
def int_tuples_list(list_of_lists: list[list[str]]) -> list[tuple[int,...]]:
    updated_list: list = []
    for item in list_of_lists:
        new_item: tuple[int,...] = tuple([int(x) for x in item])
        updated_list.append(new_item)
    return updated_list

# Part 1: 

# Given the rules and an update, checks if its correct
def check_value(rules: list[tuple[int, ...]], update: tuple[int, ...]) -> bool:
    n: int = len(update)
    updates_error_pairs: list[tuple[int, int]] = [(update[j], update[i]) for i in range(n) for j in range(i+1,n)]
    status = True
    for possible_error in updates_error_pairs:
        if possible_error in rules:
            status = False
            break
    return status

# Given the rules and updates, sums the middle number of all correct updates 
def check_updates(rules: list[tuple[int, ...]], updates: list[tuple[int, ...]]) -> int:
        solution: int = 0
        for update in updates:
            if check_value(rules, update):
                n: int = len(update) // 2
                solution += update[n]
        return solution


# Part 2: (also functions from part 1 are used)

# Given the rules and a (incorrect) update, interchages all wrong pairs
def fix_step(rules: list[tuple[int, ...]], update: tuple[int, ...]) -> tuple[int, ...]:
    n: int = len(update)
    updates_error_pairs: list[tuple[int, int]] = [(update[j], update[i]) for i in range(n) for j in range(i+1,n)]
    update_fixed: list[int] = list(update)
    for possible_error in updates_error_pairs:
        i: int = update_fixed.index(possible_error[0])
        j: int = update_fixed.index(possible_error[1])
        if possible_error in rules:
            update_fixed[i] = possible_error[1]
            update_fixed[j] = possible_error[0]
    return tuple(update_fixed)

# Applies "fix_step" to all the incorrect updates repeteadly until they are correct and returns them in a list
def fix_updates(rules: list[tuple[int, ...]], updates: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    fixed_updates: list[tuple[int, ...]] = []
    for update in updates:
        if not check_value(rules, update):
            new_update: tuple[int, ...] = fix_step(rules, update)
            while not check_value(rules, new_update):
                    new_update = fix_step(rules, new_update)
            fixed_updates.append(new_update)
    return fixed_updates

# Run

def main() -> None:
    # Getting the rules and updates separately
    with open(r"./2024/05/input.txt", newline='') as myfile:
        r = csv.reader(myfile, delimiter="|")
        rules_str: list[list[str]] = []
        updates_str: list[list[str]] = []
        change = True
        for i, row in enumerate(r):
            if not row:
                n: int = i
                change = False
            elif change:
                rules_str.append(row)
            elif not change:
                updates_str += list(map(lambda x: x.split(","), row))

    # Making them a list of tuples of ints (in the end there is no strict need for them to be integers but but it's better that way)
    updates: list[tuple[int, ...]] = int_tuples_list(updates_str)
    rules: list[tuple[int, ...]] = int_tuples_list(rules_str)
    print(f"Sum of middle page numbers from correct updates: {check_updates(rules, updates)}") # Part 1
    print(f"Same for corrected incorrect updates: {check_updates(rules, fix_updates(rules, updates))}") # Part 2

if __name__ == "__main__":
    main()