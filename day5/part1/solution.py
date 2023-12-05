def get_seed_number_list(line):
    _, seed_numbers = line.split(': ')
    seeds = seed_numbers.split(' ')
    seeds = [int(seed) for seed in seeds]
    return seeds


def perform_step(stepmap, seeds):
    new_seeds = [seed for seed in seeds]
    for line in stepmap:
        if line[0].isdigit():
            nums = line.split(' ')
            nums = [int(num) for num in nums]
            dest_start = nums[0]
            source_start = nums[1]
            source_end = source_start + nums[-1] - 1
            for idx, seed in enumerate(seeds):
                if seed >= source_start and seed <= source_end:
                    diff = seed - source_start
                    new_seeds[idx] = dest_start + diff
        #else:
        #    print(line)
    return new_seeds


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        isFirstLine = True
        seeds = []
        isStartStep = False
        stepmap = []
        for line in f:
            line = line.strip()
            if not isFirstLine and line != '':
                stepmap.append(line)
            if line == '':
                if stepmap:
                    seeds = perform_step(stepmap, seeds)
                    stepmap = []
            if isFirstLine:
                seeds = get_seed_number_list(line)
                #print(seeds)
                isFirstLine = False
    if stepmap:
        seeds = perform_step(stepmap, seeds)
    print(f"The solution: {min(seeds)}")