#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.

def find_animal(map):
    for row_idx in range(len(map)):
        for col_idx in range(len(map[row_idx])):
            if map[row_idx][col_idx] == 'S':
                return (row_idx, col_idx)


def pretty_print_mtx(mtx):
    for row_idx in range(len(mtx)):
        print(mtx[row_idx])


def make_step(loc, map, current_num, map_visited):
    map_visited[loc[0]][loc[1]] = 1
    pipe = map[loc[0]][loc[1]]
    if pipe == '|':
        if map_visited[loc[0]-1][loc[1]] == 0:
            return (loc[0]-1, loc[1]), current_num+1
        elif map_visited[loc[0]+1][loc[1]] == 0:
            return (loc[0]+1, loc[1]), current_num+1
        else:
            return None, current_num+1
    elif pipe == '-':
        if map_visited[loc[0]][loc[1]-1] == 0:
            return (loc[0], loc[1]-1), current_num+1
        elif map_visited[loc[0]][loc[1]+1] == 0:
            return (loc[0], loc[1]+1), current_num+1
        else:
            return None, current_num+1
    elif pipe == 'L':
        if map_visited[loc[0]-1][loc[1]] == 0:
            return (loc[0]-1, loc[1]), current_num+1
        elif map_visited[loc[0]][loc[1]+1] == 0:
            return (loc[0], loc[1]+1), current_num+1
        else:
            return None, current_num+1
    elif pipe == 'J':
        if map_visited[loc[0]-1][loc[1]] == 0:
            return (loc[0]-1, loc[1]), current_num+1
        elif map_visited[loc[0]][loc[1]-1] == 0:
            return (loc[0], loc[1]-1), current_num+1
        else:
            return None, current_num+1
    elif pipe == '7':
        if map_visited[loc[0]+1][loc[1]] == 0:
            return (loc[0]+1, loc[1]), current_num+1
        elif map_visited[loc[0]][loc[1]-1] == 0:
            return (loc[0], loc[1]-1), current_num+1
        else:
            return None, current_num+1
    elif pipe == 'F' or pipe == 'S':
        if map_visited[loc[0]+1][loc[1]] == 0:
            return (loc[0]+1, loc[1]), current_num+1
        elif map_visited[loc[0]][loc[1]+1] == 0:
            return (loc[0], loc[1]+1), current_num+1
        else:
            return None, current_num+1


def create_new_map_and_find_max(animal_loc, map):
    map_visited  = []
    for row_idx in range(len(map)):
        map_visited.append([])
        for col_idx in range(len(map[row_idx])):
            map_visited[row_idx].append(0)
    next_loc = animal_loc
    current_num = 0
    while next_loc:
        #print('Map visited:')
        #pretty_print_mtx(map_visited)
        #print(next_loc)
        next_loc, current_num = make_step(next_loc, map, current_num, map_visited)
    return current_num


if __name__ == '__main__':
    map = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            map.append(line)
    animal_loc = find_animal(map)
    m = create_new_map_and_find_max(animal_loc, map)
    print(f'The solution is: {int(m/2)}')