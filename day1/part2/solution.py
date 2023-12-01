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

def check_if_startwith_digit(line, reversed = False):
    digit_strings = list(digits.keys())
    if reversed:
        for idx, digit_string in enumerate(digit_strings):
            digit_strings[idx] = digit_string[::-1]
        line = line[::-1]
    for digit_string in digit_strings:
        if line.startswith(digit_string):
            if reversed: return digits[digit_string[::-1]]
            else: return digits[digit_string]
    return False

with open('input.txt', 'r') as f:
    for line in f:
        first_digit = None
        last_digit = None
        if not line:
            break
        for idx in range(len(line)):
            if line[idx].isdigit():
                first_digit = int(line[idx])
                break
            string_number = check_if_startwith_digit(line[idx:])
            if string_number:
                first_digit = string_number
                break
        for idx in range(len(line)-1, 0, -1):
            if line[idx].isdigit():
                last_digit = int(line[idx])
                break
            string_number = check_if_startwith_digit(line[:idx+1], True)
            if string_number:
                last_digit = string_number
                break
        #print(f"Line {line[:-1]}, first: {first_digit}, last: {last_digit}")
        if not first_digit and not last_digit: num = 0
        elif not first_digit: num = last_digit*10+last_digit
        elif not last_digit: num = first_digit*10+first_digit
        else: num = first_digit*10+last_digit
        numbers.append(num)

print(f"The solution: {sum(numbers)}")