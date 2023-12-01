numbers = []

digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def preprocess_input_line(line):
    for key in digits.keys():
        if key in line:
            line = line.replace(key, key + str(digits[key])+ key)
    return line

with open('input.txt', 'r') as f:
    for line in f:
        line = preprocess_input_line(line)
        first_digit = None
        last_digit = None
        if not line:
            break
        for idx in range(len(line)):
            if line[idx].isdigit():
                first_digit = int(line[idx])
                break
        for idx in range(len(line)-1, 0, -1):
            if line[idx].isdigit():
                last_digit = int(line[idx])
                break
        if not first_digit and not last_digit: num = 0
        elif not first_digit: num = last_digit*10+last_digit
        elif not last_digit: num = first_digit*10+first_digit
        else: num = first_digit*10+last_digit
        numbers.append(num)

print(f"The solution: {sum(numbers)}")