def check_char(char):
    return ((not char.isdigit()) and char != '.')


def check_neighbors(mtx, location):
    i, j = location
    # check neighbors
    if i+1 < len(mtx) and check_char(mtx[i+1][j]): return True
    if i-1 >= 0 and check_char(mtx[i-1][j]): return True
    if j+1 < len(mtx[i]) and check_char(mtx[i][j+1]): return True
    if j-1 >= 0 and check_char(mtx[i][j-1]): return True
    # check diagonals
    if i+1 < len(mtx) and j+1 < len(mtx[i+1]) and check_char(mtx[i+1][j+1]): return True
    if i+1 < len(mtx) and j-1 >= 0 and check_char(mtx[i+1][j-1]): return True
    if i-1 >= 0  and j+1 < len(mtx[i-1]) and check_char(mtx[i-1][j+1]): return True
    if i-1 >= 0 and j-1 >= 0 and check_char(mtx[i-1][j-1]): return True
    return False

def is_good_number(mtx, locations):
    for loc in locations:
        if check_neighbors(mtx, loc):
            return True
    return False


def find_good_numbers_and_add(mtx):
    final_sum = 0
    good_num_count = 0
    bad_num_count = 0
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
                is_good = is_good_number(mtx, current_number_location)
                if is_good:
                    final_sum += current_number
                    good_num_count += 1
                else:
                    bad_num_count += 1
                num_start = False
                current_number = 0
                current_number_location = []
    #print(f"Good num count: {good_num_count}, bad_num_count: {bad_num_count}")
    #print(f"All numbers: {good_num_count+bad_num_count}")
    return final_sum


if __name__ == '__main__':
    mtx = []
    with open('day3/part1/input.txt', 'r') as f:
        #row_idx = 0
        for line in f:
            #mtx.append([])
            line = line.strip()
            mtx.append(line)
            #row_idx += 1
    final_sum = find_good_numbers_and_add(mtx)
    print(f"The solution: {final_sum}")