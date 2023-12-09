import math


def read_network(network, line, start_nodes):
    node, left_right = line.split(' = ')
    if node.endswith('A'):
        start_nodes.append(node)
    left, right = left_right.split(', ')
    left = left.replace('(', '')
    right = right.replace(')', '')
    network[node] = {
        'L': left,
        'R': right,
    }


def perform_steps(steps, network, current_node, number_of_steps):
    next_step = steps[number_of_steps%len(steps)]
    next_node = network[current_node][next_step]
    return next_node


def go_to_ZZZ(steps, network, current_node, number_of_steps):
    while not current_node.endswith('Z'):
        current_node = perform_steps(steps, network, current_node, number_of_steps)
        number_of_steps += 1
    return number_of_steps


if __name__ == "__main__":
    isFirstLine = True
    steps = ''
    network = {}
    start_nodes = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not isFirstLine and line != '':
                read_network(network, line, start_nodes)
            if isFirstLine:
                steps = line
                isFirstLine = False
    sol = 1
    for start_node in start_nodes:
        sol = math.lcm(sol, go_to_ZZZ(steps, network, start_node, 0))
    print(f'The solution is: {sol}')