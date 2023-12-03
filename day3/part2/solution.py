def check_asterix(char):
    return char == '*'


def check_neighbors(mtx, location):
    i, j = location
    # check neighbors
    if i+1 < len(mtx) and check_asterix(mtx[i+1][j]):
        return True, (i+1, j)
    if i-1 >= 0 and check_asterix(mtx[i-1][j]):
        return True, (i-1, j)
    if j+1 < len(mtx[i]) and check_asterix(mtx[i][j+1]):
        return True, (i, j+1)
    if j-1 >= 0 and check_asterix(mtx[i][j-1]):
        return True, (i, j-1)
    # check diagonals
    if i+1 < len(mtx) and j+1 < len(mtx[i+1]) and check_asterix(mtx[i+1][j+1]):
        return True, (i+1, j+1)
    if i+1 < len(mtx) and j-1 >= 0 and check_asterix(mtx[i+1][j-1]):
        return True, (i+1, j-1)
    if i-1 >= 0  and j+1 < len(mtx[i-1]) and check_asterix(mtx[i-1][j+1]):
        return True, (i-1, j+1)
    if i-1 >= 0 and j-1 >= 0 and check_asterix(mtx[i-1][j-1]):
        return True, (i-1, j-1)
    return False, ()


def is_good_number(mtx, locations, num, ratios):
    for loc in locations:
        is_good, loc_asterix = check_neighbors(mtx, loc)
        if is_good:
            if loc_asterix in ratios.keys(): ratios[loc_asterix].append(num)
            else: ratios[loc_asterix] = [num]
            break


def find_good_numbers_and_add(mtx):
    ratios = {}
    for row_idx, row in enumerate(mtx):
        current_number_location = []
        current_number = 0
        num_start = False
        for col_idx, _ in enumerate(row):
            cell = mtx[row_idx][col_idx]
            if cell.isdigit():
                num_start = True
                current_number = current_number * 10 + int(cell)
                current_number_location.append((row_idx, col_idx))
            if (num_start and not cell.isdigit()) or \
                (num_start and col_idx+1 == len(mtx[row_idx])):
                is_good_number(mtx, current_number_location, current_number, ratios)
                num_start = False
                current_number = 0
                current_number_location = []
    return ratios


def postprocess_ratios(ratios):
    final_sum = 0
    for key in ratios.keys():
        if len(ratios[key]) == 2:
            final_sum += (ratios[key][0] * ratios[key][1])
    return final_sum


if __name__ == '__main__':
    mtx = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            mtx.append(line)
    ratios = find_good_numbers_and_add(mtx)
    final_sum = postprocess_ratios(ratios)
    print(f"The solution: {final_sum}")