# https://adventofcode.com/2023/day/2

# The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
# The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
# Adding up these five powers produces the sum 2286.
# For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

with open("d2_input.txt") as in_file:
    input_strings = [line.strip() for line in in_file]


colors = ["red", "green", "blue"]
sum_of_powers = 0

for line in input_strings:
    power = 1  # initialize with value 1 to avoid multiplying by 0
    _, cubes_and_colors = line.split(":")[0].strip("Game "), line.split(":")[1].split(";")
    cubes_and_colors = [combination.strip() for item in cubes_and_colors for combination in item.split(",")]
    cubes_and_colors = [{combination.split(" ")[1]: int(combination.split(" ")[0])} for combination in cubes_and_colors]
    for color in colors:
        color_list = [item[color] for item in cubes_and_colors if item.get(color) is not None]
        power *= max(color_list)

    sum_of_powers += power

print(sum_of_powers)
