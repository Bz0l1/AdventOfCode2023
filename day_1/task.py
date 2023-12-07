filename = "./input.txt"

with open(filename, 'r') as file:
    inputs = file.readlines()


def part1():
    totalSum = 0
    for input in inputs:
        first_digit = None
        last_digit = None

        for character in input:
            if character.isdigit():
                first_digit = character
                break

        for character in reversed(input):
            if character.isdigit():
                last_digit = character
                break

        if first_digit is not None and last_digit is not None:
            totalSum += int(first_digit + last_digit)
    return totalSum


def replace_numbers(input_str, digits):
    output = ""
    i = 0
    while i < len(input_str):
        for word, digit in digits.items():
            if input_str[i:i + len(word)] == word:
                output += digit
                return output + input_str[i + len(word):]
        output += input_str[i]
        i += 1
    return output


def replace_numbers_reverse(input_str, digits):
    reversed_digits = {word[::-1]: digit for word, digit in digits.items()}
    reversed_output = replace_numbers(input_str[::-1], reversed_digits)
    return reversed_output[::-1]


def part2():
    totalSum = 0
    digits = { "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9' }

    for input in inputs:
        to_digits_forward = replace_numbers(input, digits)
        to_digits_reverse = replace_numbers_reverse(input, digits)

        first_digit = next((char for char in to_digits_forward if char.isdigit()), None)
        last_digit = next((char for char in reversed(to_digits_reverse) if char.isdigit()), None)

        if first_digit and last_digit:
            totalSum += int(first_digit + last_digit)

    return totalSum