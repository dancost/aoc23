# https://adventofcode.com/2023/day/1
with open("d1p1_input.txt") as in_file:
    input_strings = [line.strip() for line in in_file]


def calculate_calibration_values(line):
    numbers = []
    for i in range(len(line)):
        if line[i].isnumeric():
            numbers.append(line[i])
    return f"{numbers[0] + numbers[-1]}"


result = 0
for item in input_strings:
    result += int(calculate_calibration_values(item))

print(result)
