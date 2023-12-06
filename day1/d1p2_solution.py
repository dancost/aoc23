with open("d1_input.txt") as in_file:
    input_strings = [line.strip() for line in in_file]

word_to_digit = {"one": "1",
                 "two": "2",
                 "three": "3",
                 "four": "4",
                 "five": "5",
                 "six": "6",
                 "seven": "7",
                 "eight": "8",
                 "nine": "9"}


# this is crazy but it beats using regex
def convert_word_to_digit(line):
    for word, digit in word_to_digit.items():
        if word in line:
            # duplicate first and last letters to remove overlapping strings case
            line = line.replace(word, word[0] + word + word[-1])
        line = line.replace(word, digit)

    return line


def calculate_calibration_values(strings):
    total_sum = 0
    for line in strings:
        line = convert_word_to_digit(line)
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in reversed(line) if char.isdigit()), None)

        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit + last_digit)
            total_sum += calibration_value

    return total_sum


result = calculate_calibration_values(input_strings)

print(result)
