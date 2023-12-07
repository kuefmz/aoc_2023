def define_hand_type(data, hand, points):
    hand_dict = {}
    for card in hand:
        if card in hand_dict.keys():
            hand_dict[card] += 1
        else:
            hand_dict[card] = 1
    if 'J' in hand_dict.keys():
        number_of_J = hand_dict['J']
        if number_of_J != 5:
            card_occurance = []
            for k in hand_dict.keys():
                if k != 'J':
                    card_occurance.append((k, hand_dict[k]))
            card_occurance.sort(key=lambda x: x[1], reverse=True)
            hand_dict[card_occurance[0][0]] += number_of_J
            hand_dict.pop('J')
    if len(hand_dict.keys()) == 5:
        data['high_card'].append((hand, points))
    elif len(hand_dict.keys()) == 1:
        data['five_of_a_kind'].append((hand, points))
    elif len(hand_dict.keys()) == 4:
        data['ope_pair'].append((hand, points))
    elif len(hand_dict.keys()) == 3:
        keys = list(hand_dict.keys())
        values = set([hand_dict[k] for k in keys])
        if 3 in values:
            data['three_of_a_kind'].append((hand, points))
        else:
            data['two_pair'].append((hand, points))
    elif len(hand_dict.keys()) == 2:
        keys = list(hand_dict.keys())
        values = set([hand_dict[k] for k in keys])
        if 2 in values and 3 in values:
            data['full_house'].append((hand, points))
        elif 4 in values:
            data['four_of_a_kind'].append((hand, points))
    return data


def sorting_key(string):
    custom_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    return [custom_order.index(char) if char in custom_order else float('inf') for char in string]


def order_data(data):
    hand_types = list(data.keys())
    for type in hand_types:
        hands = data[type]
        hands_sorted = sorted(hands, key=lambda x: sorting_key(x[0]), reverse=True)
        data[type] = hands_sorted
    return data


def calculate_points(data):
    points = 0
    ranking = 1
    order_of_hand_types = ['high_card', 'ope_pair', 'two_pair', 'three_of_a_kind', 'full_house', 'four_of_a_kind', 'five_of_a_kind']
    for type in order_of_hand_types:
        for hand, point in data[type]:
            points = points + (ranking * point)
            ranking += 1
    return points


if __name__ == "__main__":
    data = {
        'five_of_a_kind': [],
        'four_of_a_kind': [],
        'full_house': [],
        'three_of_a_kind': [],
        'two_pair': [],
        'ope_pair': [],
        'high_card': [],
    }
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            hand, points = line.split(' ')
            data = define_hand_type(data, hand, int(points))
    ordered_data = order_data(data)
    final_points = calculate_points(ordered_data)
    print(f'The solution is: {final_points}')