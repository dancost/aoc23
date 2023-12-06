# https://adventofcode.com/2023/day/2

# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes,
# and 14 blue cubes. What is the sum of the IDs of those games?

bag_content = {"red": 12,
               "green": 13,
               "blue": 14}

with open("d2_input.txt") as in_file:
    input_strings = [line.strip() for line in in_file]

id_sum = 0

for line in input_strings:
    is_possible_game = True
    game_id, cubes_and_colors = line.split(":")[0].strip("Game "), line.split(":")[1].split(";")
    cubes_and_colors = [combination.strip() for item in cubes_and_colors for combination in item.split(",")]
    cubes_and_colors = [{combination.split(" ")[1]: int(combination.split(" ")[0])} for combination in cubes_and_colors]
    d = {game_id: cubes_and_colors}

    for k, v in bag_content.items():
        for item in d[game_id]:
            if item.get(k) is not None:
                if item[k] <= v:
                    continue
                else:
                    print(f"bad {item} found, game is not possible  - skipping")
                    is_possible_game = False
                    break
    if is_possible_game:
        id_sum += int(game_id)


print(id_sum)
