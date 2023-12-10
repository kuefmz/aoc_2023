import copy


def find_animal(map):
    for row_idx in range(len(map)):
        for col_idx in range(len(map[row_idx])):
            if map[row_idx][col_idx] == 'S':
                return (row_idx, col_idx)


def make_step(loc, map, map_visited):
    map_visited[loc[0]][loc[1]] = 1
    pipe = map[loc[0]][loc[1]]
    if pipe == '|':
        if map_visited[loc[0]-1][loc[1]] == 0: return (loc[0]-1, loc[1])
        elif map_visited[loc[0]+1][loc[1]] == 0: return (loc[0]+1, loc[1])
        else: return None
    elif pipe == '-':
        if map_visited[loc[0]][loc[1]-1] == 0: return (loc[0], loc[1]-1)
        elif map_visited[loc[0]][loc[1]+1] == 0: return (loc[0], loc[1]+1)
        else: return None
    elif pipe == 'L':
        if map_visited[loc[0]-1][loc[1]] == 0: return (loc[0]-1, loc[1])
        elif map_visited[loc[0]][loc[1]+1] == 0: return (loc[0], loc[1]+1)
        else: return None
    elif pipe == 'J':
        if map_visited[loc[0]-1][loc[1]] == 0: return (loc[0]-1, loc[1])
        elif map_visited[loc[0]][loc[1]-1] == 0: return (loc[0], loc[1]-1)
        else: return None
    elif pipe == '7':
        if map_visited[loc[0]+1][loc[1]] == 0: return (loc[0]+1, loc[1])
        elif map_visited[loc[0]][loc[1]-1] == 0: return (loc[0], loc[1]-1)
        else: return None
    elif pipe == 'F' or pipe == 'S':
        if map_visited[loc[0]+1][loc[1]] == 0: return (loc[0]+1, loc[1])
        elif map_visited[loc[0]][loc[1]+1] == 0: return (loc[0], loc[1]+1)
        else: return None


def check_inside(loc, map_visited, map):
    x, y = loc
    weight = 0
    for col_idx in range(0, y):
        if map_visited[x][col_idx] == 1:
            pipe = map[x][col_idx]
            if pipe in ['|', 'S', 'F', '7']:
                weight += 1
    return weight%2==1


def cunt_island_blocks(map, map_visited):
    cnt = 0
    for row_idx in range(len(map)):
        for col_idx in range(len(map[row_idx])):
            isInside = False
            if map_visited[row_idx][col_idx] == 0:
                isInside = check_inside((row_idx, col_idx), map_visited, map)
            if isInside: cnt += 1
    return cnt


def create_new_map_and_find_max(animal_loc, map):
    map_visited  = []
    for row_idx in range(len(map)):
        map_visited.append([])
        for col_idx in range(len(map[row_idx])):
            map_visited[row_idx].append(0)
    next_loc = animal_loc
    while next_loc:
        next_loc = make_step(next_loc, map, map_visited)
    return cunt_island_blocks(map, map_visited)


if __name__ == '__main__':
    map = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            map.append(line)
    animal_loc = find_animal(map)
    m = create_new_map_and_find_max(animal_loc, map)
    print(f'The solution is: {int(m)}')