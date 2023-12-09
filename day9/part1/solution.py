def check_if_all_zeros(diffs):
    for d in diffs:
        if d != 0:
            return False
    return True


def get_diffs(seq):
    diffs = []
    for idx in range(len(seq)-1):
        diff = seq[idx+1]-seq[idx]
        diffs.append(diff)
    return diffs


def get_extra_num(all_diffs):
    extra_num = 0
    for idx in range(len(all_diffs)-1, -1, -1):
        extra_num += all_diffs[idx][-1]
    return extra_num


def process_line(line):
    seq = line.split(' ')
    seq = [int(s) for s in seq]
    allZeros = False
    all_diffs = [seq]
    while not allZeros:
        diffs = get_diffs(seq)
        all_diffs.append(diffs)
        allZeros = check_if_all_zeros(diffs)
        seq = diffs
    return get_extra_num(all_diffs)


if __name__ == "__main__":
    sol = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            sol += process_line(line)
    print(f'The solution is {sol}')