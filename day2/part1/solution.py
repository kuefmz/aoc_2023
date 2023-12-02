available = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def is_possible_game(game):
    game_id, bag = game.split(": ")
    game_id = int(game_id.split(" ")[-1])
    bag = bag.split("; ")
    colors = list(available.keys())
    for set_of_cude in bag:
        founds = set_of_cude.split(", ")
        game_counter = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for found in founds:
            for color in colors:
                if color in found:
                    found_num = found.split(" ")[0]
                    game_counter[color] += int(found_num)
        for color in colors:
            if game_counter[color] > available[color]:
                return 0
    #print(game)
    return game_id


if __name__ == "__main__":
    sum_ids = 0
    with open('input.txt', 'r') as f:
        for line in f:
            sum_ids += is_possible_game(line)
    print(f"The solution: {sum_ids}")