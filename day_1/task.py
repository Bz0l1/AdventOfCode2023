filename = "./input.txt"
totalSum = 0

with open(filename, 'r') as file:
    inputs = file.readlines()


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

print(totalSum)
