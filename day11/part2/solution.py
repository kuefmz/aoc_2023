import copy


def pretty_print_mtx(mtx):
    for row in mtx:
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

    # handle emlty rows
    empty_row_idx = []
    for row_idx in  range(len(image)):
        rowEmpty = True
        for col_idx in range(len(image[row_idx])):
            if image[row_idx][col_idx] != '.' and image[row_idx][col_idx] != 1000000:
                rowEmpty = False
        if rowEmpty:
            empty_row_idx.append(row_idx)
    empty_row_idx.sort(reverse=True)
    return empty_row_idx, empty_col_idx


def replace_galaxies(image, empty_row_idx, empty_col_idx, expand = 1):
    galaxy_locations = []
    cnt = 1
    for row_idx in range(len(image)):
        for col_idx in range(len(image[row_idx])):
            if image[row_idx][col_idx] == '#':
                image[row_idx][col_idx] = str(cnt)
                expanded_dist_col = sum([ 1 for r in empty_row_idx if r<row_idx ])
                expanded_dist_row = sum([ 1 for r in empty_col_idx if r<col_idx ])
                galaxy_locations.append((row_idx+expanded_dist_col*(expand-1),col_idx+expanded_dist_row*(expand-1)))
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
    empty_row_idx, empty_col_idx = check_empty_rows_and_cols(image)
    galaxy_locations = replace_galaxies(image, empty_row_idx, empty_col_idx, 1000000)
    galaxy_pairs = []
    for x in range(len(galaxy_locations)):
        for y in range(x+1, len(galaxy_locations)):
            galaxy_pairs.append((galaxy_locations[x], galaxy_locations[y]))
    dist = sum([manhattan(loc[0], loc[1]) for loc in galaxy_pairs])
    print(f'The solution is: {dist}')