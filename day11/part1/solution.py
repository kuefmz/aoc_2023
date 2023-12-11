import copy


def pretty_print_mtx(mtx):
    for row in mtx:
        row = ''.join(row)
        print(row, len(row))


def check_empty_rows_and_cols(image):
    # handle empty cols
    empty_col_idx = []
    for col_idx in  range(len(image[0])):
        colEmpty = True
        for row_idx in range(len(image)):
            if image[row_idx][col_idx] != '.':
                colEmpty = False
        if colEmpty:
            empty_col_idx.append(col_idx)
    empty_col_idx.sort(reverse=True)
    for col_idx in empty_col_idx:
        for row_idx in range(len(image)):
            image[row_idx].insert(col_idx, '.')

    # handle emlty rows
    empty_row_idx = []
    for row_idx in  range(len(image)):
        rowEmpty = True
        for col_idx in range(len(image[row_idx])):
            if image[row_idx][col_idx] != '.':
                rowEmpty = False
        if rowEmpty:
            empty_row_idx.append(row_idx)
    empty_row_idx.sort(reverse=True)
    empty_row = ['.' for _ in range(len(image)+len(empty_col_idx))]
    for row_idx in empty_row_idx:
        image.insert(row_idx, empty_row)
    return copy.deepcopy(image)


def replace_galaxies(image):
    galaxy_locations = []
    cnt = 1
    galaxies = []
    for row_idx in range(len(image)):
        for col_idx in range(len(image[row_idx])):
            if image[row_idx][col_idx] == '#':
                image[row_idx][col_idx] = str(cnt)
                galaxy_locations.append((row_idx, col_idx))
                galaxies.append(cnt)
                cnt += 1
    return galaxy_locations


def manhattan(loc1, loc2):
    return abs(loc1[0]-loc2[0]) + abs(loc1[1]-loc2[1])


if __name__ == "__main__":
    image = []
    row_counter = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            image.append([])
            for c in line:
                image[row_counter].append(c)
            row_counter += 1
    image = check_empty_rows_and_cols(image)
    galaxy_locations = replace_galaxies(image)
    galaxy_pairs = []
    for x in range(len(galaxy_locations)):
        for y in range(x+1, len(galaxy_locations)):
            galaxy_pairs.append((galaxy_locations[x], galaxy_locations[y]))
    dist = sum([manhattan(loc[0], loc[1]) for loc in galaxy_pairs])
    print(f'The solution is: {dist}')