
def get_winning_number_points(line):
    winning, numbers = line.split(' | ')
    game, winning = winning.split(': ')
    winning_numers = winning.split(' ')
    numbers = numbers.split(' ')
    points = 0
    for num in winning_numers:
        if num.isdigit() and num in numbers:
            if points == 0:
                points += 1
            else:
                points *= 2
    return points


if __name__ == "__main__":
    points = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line.replace('  ', ' ')
            points += get_winning_number_points(line)
    print(f"The solution: {points}")