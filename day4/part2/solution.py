import json

def get_final_points(cards):
    final_points = 0
    for card in cards.keys():
        final_points += cards[card]['copies']
    return final_points


def count_copies(cards):
    for card in cards.keys():
        number_of_matches = cards[card]['number_of_matches']
        for match in range(number_of_matches):
            cards[card+match+1]['copies'] += cards[card]['copies']
    return cards


def build_summary_dict(line, cards):
    winning, numbers = line.split(' | ')
    card, winning = winning.split(': ')
    card_num = int(card.split(' ')[-1])
    winning_numers = winning.split(' ')
    numbers = numbers.split(' ')
    winning_numers = [int(winning_num) for winning_num in winning_numers if winning_num != '']
    numbers = [int(num) for num in numbers if num != '']
    points = 0
    number_of_matches = 0
    for idx, num in enumerate(winning_numers):
        if num in numbers:
            number_of_matches += 1
            if points == 0:
                points += 1
            else:
                points *= 2
    cards[card_num] = {
        'winnig_numbers': winning_numers,
        'numbers': numbers,
        'number_of_matches': number_of_matches,
        'points': points,
        'copies': 1,
    }
    return cards


if __name__ == "__main__":
    cards = {}
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line = line.replace('  ', ' ')
            cards = build_summary_dict(line, cards)
    cards = count_copies(cards)
    points = get_final_points(cards)
    #print(json.dumps(cards, indent=4))
    print(f"The solution: {points}")