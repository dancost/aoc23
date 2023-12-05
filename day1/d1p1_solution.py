# https://adventofcode.com/2023/day/1
with open("d1_input.txt") as in_file:
    input_strings = [line.strip() for line in in_file]


# def calculate_calibration_values(line):
#     numbers = []
#     for i in range(len(line)):
#         if line[i].isnumeric():
#             numbers.append(line[i])
#     return f"{numbers[0] + numbers[-1]}"

# result = 0
# for item in input_strings:
#     result += int(calculate_calibration_values(item))
#
# print(result)


def calculate_calibration_values(document):
    total_sum = 0
    for line in document:
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum


result = calculate_calibration_values(input_strings)
