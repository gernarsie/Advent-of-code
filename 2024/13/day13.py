# So my first instict was to use numpys linalg.solve but float and calculations are not exact and 
# since we need the integer solutions that's not use for us (we can not decide 100% wheter a solution is integral or not)
# Instead I will be solving the linear equations directly. Since programming Gaussian elimination would be overkill I will be
# using Cramer's rule (https://en.wikipedia.org/wiki/Cramer%27s_rule). It is far from optimal in terms of number of computations but since we are working with 2x2 matrices its ok


class Machine:
    
    # Each machine has button A, B and price as tuples (X, Y)
    def __init__(self, a: tuple[int, int], b: tuple[int, int], price: tuple[int, int]) -> None:
        self.buttonA: tuple[int, int] = a
        self.buttonB: tuple[int, int] = b
        self.price: tuple[int, int] = price
    
    def __str__(self) -> str:
        return f"A: {self.buttonA}, B: {self.buttonB}, Price: {self.price}"
    
    
    # For i = 0 it calculates the determinant of the matrix representing the equation system
    # For i > 0 it calculates the determinant of the matrix where column i has been changed by the price
    # as needed for Cramer's rule
    def calculate_determinant(self, i = 0) -> int:
        col1: tuple[int, int] =  self.buttonA
        col2: tuple[int, int] = self.buttonB
        if i == 1:
            col1 = self.price
        elif i == 2:
            col2 = self.price
        return col1[0]*col2[1] - col2[0]*col1[1]
    

    # If a matrix has determinant 0 it either has multiple solutions or 0, here we check that
    def check_singularities(self) -> bool:
        if (self.buttonA[0] / self.buttonA[1]) != (self.price[0]/self.price[1]):
            return True
        else:
            return False
    

    def solution(self) -> tuple[float, float]:
        det: int = self.calculate_determinant()
        
        # If the determinant is not 0, we apply cramers rule
        if det != 0:
            sol: tuple[float, float] = (self.calculate_determinant(i = 1) / det, self.calculate_determinant(i = 2) / det)
        
        # Else we check wheter it has 0 or multiple solutions, and if it has multiple we pick the one that uses less tokens
        else:
            if self.check_singularities():
                sol = (0, 0)
            else:
                sol1: float = self.price[0] / self.buttonA[0]
                sol2: float = self.price[0] / self.buttonB[0]
                if (3 * sol1) < sol2:
                    sol = (sol1, 0)
                else:
                    sol = (0, sol2)  
        return sol

    # We check if the solution is integer and if it is we calculate the tokens needed
    def count_tokens(self) -> int:
        sol: tuple[float, float] = self.solution()
        if (sol[0].is_integer()) and (sol[1].is_integer()):
            return 3 * int(sol[0]) + int(sol[1])
        else:
            return 0

    # For part 2 we use this to change the price by an ammount
    def change_price(self, ammount: int) -> None:
        self.price = (self.price[0] + ammount, self.price[1] + ammount)



def main() -> None:
    
    # Read input and create list of Machines (the input file follows the rule: each machine has 3 lines: button A,
    #  button B and Price, then there is a blank line before next machine)
    with open(r"./2024/13/input.txt") as myfile:
        machine_list = []
        for i, line in enumerate(myfile):
            i: int = i % 4
            numbers: list[int] = [int(x.strip(",XY+=")) for x in line.split() if ("+" in x) or ("=" in x)]
            match i:
                case 0:
                    machine_A: tuple[int, int] = (numbers[0], numbers[1])
                case 1:
                       machine_B: tuple[int, int] = (numbers[0], numbers[1])
                case 2:
                    machine_price: tuple[int, int] = (numbers[0], numbers[1])
                    machine_list.append(Machine(machine_A, machine_B, machine_price)) #type: ignore
                case 3:
                    pass

    # Part 1 solution
    total_part1 = 0
    for machine in machine_list:
        total_part1 += machine.count_tokens()
    print(f"Tokens needed: {total_part1}")

    # Part 2 solution
    machine_list2 = machine_list.copy()
    total_part2 = 0
    for machine in machine_list2:
        machine.change_price(10000000000000)
        total_part2 += machine.count_tokens()
    print(f"Tokens needed with the corrected coordinates: {total_part2}")

if __name__ == "__main__":
    main()