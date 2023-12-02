
def power_min_set_of_cubes(game):
    game_id, bag = game.split(": ")
    game_id = int(game_id.split(" ")[-1])
    bag = bag.split("; ")
    min_game_counter = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    colors = list(min_game_counter.keys())
    for set_of_cude in bag:
        founds = set_of_cude.split(", ")
        for found in founds:
            for color in colors:
                if color in found:
                    found_num = int(found.split(" ")[0])
                    if found_num > min_game_counter[color]:
                        min_game_counter[color] = int(found_num)
    # print(min_game_counter)
    power_min = 1
    for color in colors:
        power_min *= min_game_counter[color]
    return power_min


if __name__ == "__main__":
    sum_power_min_set = 0
    with open('input.txt', 'r') as f:
        for line in f:
            sum_power_min_set += power_min_set_of_cubes(line)
            # print(line)
            # print(sum_power_min_set)
    print(f"The solution: {sum_power_min_set}")