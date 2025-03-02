# Part 1

# Get the expanded blocks with a dot '.' representing an empty space
def individual_blocks(block_list: list[int]) -> list[int | str]:
    individual_blocks_list: list[int | str] = []
    k: int = 0
    for i in range(len(block_list)):
        if i % 2 == 0:
            individual_blocks_list += block_list[i] * [k]
            k += 1
        else:
            individual_blocks_list += block_list[i] * ["."]
    return individual_blocks_list

# Instead of moving the blocks and then doing the checksum, its done directly 
def filesystem_checksum(disk_map: list[int]) -> int:
    blocks: list[int | str] = individual_blocks(disk_map)
    n: int = len(blocks)
    i: int = 0
    k: int = 0
    checksum: int = 0
    while True:
        if (n + k) < i + 1:
            break
        elif isinstance(blocks[i], int):
            checksum += i * blocks[i] # type: ignore
        elif blocks[i] == ".":
            while True:
                k -= 1
                if isinstance(blocks[k], int):
                    checksum += i * blocks[k] # type: ignore
                    break 
        i += 1  
    return checksum

# Part 2:

# Here I hit the wall built by my approach of Part 1, where trying to do it like it results in an abomination so I have to 
# take another aproach (which would also work for the Part 1 with some adjustments)

# Intead of the expanded blocks, we get then as a list of tuples ('value', 'number of blocks'), 
# where value -1 indicates an empty space
def blocks_with_multiplicity(block_list: list[int]) -> list[tuple[int, int]]:
    blocks_mult_list: list[tuple[int, int]] = []
    k: int = 0
    for i in range(len(block_list)):
        if i % 2 == 0:
            blocks_mult_list.append((k, block_list[i]))
            k += 1
        else:
            blocks_mult_list.append((-1, block_list[i]))
    return blocks_mult_list

# Now we move the blocks as whole files (this is the slower step)
def file_move_blocks2(disk_map: list[int]) -> list[tuple[int, int]]:
    blocks_mult: list[tuple[int, int]] = blocks_with_multiplicity(disk_map)
    k: int = 0
    while True:
        n: int = len(blocks_mult)
        k += 1
        if blocks_mult[-k] == blocks_mult[0]:
            break
        moving: tuple[int, int] = blocks_mult[-k]
        if moving[0] != -1:
            for i, item in enumerate(blocks_mult):
                if (n - k) < i + 1:
                    break
                elif (item[0] == -1) and (item[1] >= moving[1]):
                    blocks_mult[i] = moving
                    if item[1] > moving[1]:
                        blocks_mult.insert(i + 1, (-1, item[1] - moving[1]))
                    blocks_mult[-k] = (-1, moving[1])
                    break
    return blocks_mult

# And finally we do the calculation (sum of position * value for all non empty blocks)
def filesystem_checksum2(disk_map: list[int]) -> int:
    blocks_moved: list[tuple[int, int]] = file_move_blocks2(disk_map)
    checksum: int = 0
    i = 0
    for item in blocks_moved:
        if item[0] == -1:
            i += item[1]
        else:
            for _ in range(item[1]):
                checksum += item[0] * i
                i += 1
    return checksum


def main() -> None:
    # Open file
    with open(r"./2024/09/input.txt") as myfile:
        disk_map: list[int] = [int(x) for x in myfile.read().strip()]
    
    print(f"The resulting file checksum is: {filesystem_checksum(disk_map)}") # Part 1
    print(f"The resulting file checksum using the new methos is: {filesystem_checksum2(disk_map)}") # Part 2 (takes a few seconds)

if __name__ == "__main__":
    main()