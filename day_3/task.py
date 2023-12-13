from collections import defaultdict

filename = "./input.txt"
inputs = []


with open(filename, 'r') as file:
    for input in file.readlines():
        inputs.append(input.strip())


def part1():
    def find_numbers():
        numbers = []
        for i, row in enumerate(inputs):
            j = 0
            while j < len(row):
                if row[j].isdigit():
                    start = j
                    while j < len(row) and row[j].isdigit():
                        j += 1
                    numbers.append((i, start, j))
                else:
                    j += 1
        return numbers

    def get_numbers(i, j1, j2, lenght, input_length):
        number_set = set()
        for j in range(j1, j2):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) != (0, 0):
                        nbri, nbrj = i + di, j + dj
                        if 0 <= nbri < lenght and 0 <= nbrj < input_length:
                            number_set.add((nbri, nbrj))
        return number_set

    def is_symbol(char):
        return not char.isdigit() and char != '.'

    def process_numbers(numbers):
        total = 0
        for i, j1, j2 in numbers:
            if any(is_symbol(inputs[nbri][nbrj]) for nbri, nbrj in get_numbers(i, j1, j2, len(inputs), len(inputs[0]))):
                num = int(inputs[i][j1:j2])
                total += num
        return total

    numbers = find_numbers()
    return process_numbers(numbers)


print(part1())

def part2():
    def find_numbers():
        numbers = []
        for i, row in enumerate(inputs):
            j = 0
            while j < len(row):
                if row[j].isdigit():
                    start = j
                    while j < len(row) and row[j].isdigit():
                        j += 1
                    numbers.append((i, start, j))
                else:
                    j += 1
        return numbers

    def get_numbers(i, j1, j2, lenght=len(inputs), input_length=len(inputs[0])):
        number_set = set()
        for j in range(j1, j2):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if (di, dj) != (0, 0):
                        nbri, nbrj = i + di, j + dj
                        if 0 <= nbri < lenght and 0 <= nbrj < input_length:
                            number_set.add((nbri, nbrj))
        return number_set

    def is_symbol(char):
        return not char.isdigit() and char != '.'

    def process_numbers(numbers):
        total_sum = 0
        star_numbers_map = defaultdict(list)
        for i, j1, j2 in numbers:
            num = int(inputs[i][j1:j2])
            if any(is_symbol(inputs[nbri][nbrj]) for nbri, nbrj in get_numbers(i, j1, j2)):
                for nbri, nbrj in get_numbers(i, j1, j2):
                    if inputs[nbri][nbrj] == '*':
                        star_numbers_map[(nbri, nbrj)].append(num)

        for x in star_numbers_map.values():
            if len(x) == 2:
                total_sum += (x[0] * x[1])
        return total_sum

    numbers = find_numbers()
    return process_numbers(numbers)


print(part2())
