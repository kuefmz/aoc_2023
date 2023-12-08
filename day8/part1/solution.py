def read_network(network, line):
    node, left_right = line.split(' = ')
    left, right = left_right.split(', ')
    left = left.replace('(', '')
    right = right.replace(')', '')
    network[node] = {
        'L': left,
        'R': right,
    }
    return network


def perform_steps(steps, network, current_node, number_of_steps):
    next_step = steps[number_of_steps]
    next_node = network[current_node][next_step]
    return next_node


def go_to_ZZZ(steps, network, current_node, number_of_steps):
    while current_node != 'ZZZ':
        if number_of_steps >= len(steps)-1:
            steps += steps
        current_node = perform_steps(steps, network, current_node, number_of_steps)
        number_of_steps += 1
    return number_of_steps


if __name__ == "__main__":
    isFirstLine = True
    steps = ''
    network = {}
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not isFirstLine and line != '':
                read_network(network, line)
            if isFirstLine:
                steps = line
                isFirstLine = False
    steps_needed = go_to_ZZZ(steps, network, 'AAA', 0)
    print(f'The solution is: {steps_needed}')