def get_seed_number_list(line):
    _, seed_numbers = line.split(': ')
    seeds = seed_numbers.split(' ')
    seeds = [int(seed) for seed in seeds]
    return seeds


def preprocess_seed_numbers(seeds):
    new_seeds = []
    for idx in range(0, len(seeds), 2):
        seed_start = seeds[idx]
        seed_end = seed_start + seeds[idx+1]
        new_seeds.append((seed_start, seed_end))
    return new_seeds


def get_min(seeds):
    m = 999999999999999
    for seed in seeds:
        if seed[0] < m:
            m = seed[0]
    return m

def perform_step(stepmap, seeds):
    new_seeds = set([])
    for line in stepmap:
        if line[0].isdigit():
            nums = line.split(' ')
            nums = [int(num) for num in nums]
            dest_start = nums[0]
            dest_end = dest_start + nums[-1] - 1
            source_start = nums[1]
            source_end = source_start + nums[-1] - 1
            for idx, seed in enumerate(seeds):
                if not seed[0] <= seed[1]:
                    continue
                if (seed[0] >= source_start and seed[0] <= source_end) and \
                   (seed[1] >= source_start and seed[1] <= source_end):
                    diff =  dest_start - source_start
                    new_seed = (seed[0] + diff, seed[1] + diff)
                    new_seeds.add(new_seed)
                    seeds[idx] = (seeds[idx][1]+1, seeds[idx][1])
                elif seed[0] < source_start and \
                     (seed[1] >= source_start and seed[1] <= source_end):
                    diff =  dest_start - source_start
                    new_seed_shifted = (dest_start, seed[1]+diff)
                    new_seeds.add(new_seed_shifted)
                    seeds[idx] = (seed[0], source_start - 1)
                elif (seed[0] >= source_start and seed[0] <= source_end) and \
                     seed[1] > source_end:
                    diff =  dest_start - source_start
                    new_seed_shifted = (seed[0]+diff, dest_end)
                    new_seeds.add(new_seed_shifted)
                    seeds[idx] = (source_end+1, seed[1])
                elif seed[0] < source_start and seed[1] > source_end:
                    diff =  dest_start - source_start
                    new_seed_shifted = (dest_start, dest_end)
                    new_seeds.add(new_seed_shifted)
                    new_seed_not_in_pre = (seed[0], source_start - 1)
                    new_seed_not_in_post = (source_end + 1, seed[1])
                    seeds[idx] = new_seed_not_in_pre
                    seeds.append(new_seed_not_in_post)
    for idx, seed in enumerate(seeds):
        if seed[0] <= seed[1]:
            new_seeds.add(seed)
    return list(new_seeds)


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
                seeds = preprocess_seed_numbers(seeds)
                isFirstLine = False
    if stepmap:
        seeds = perform_step(stepmap, seeds)
    print(f"The solution: {get_min(seeds)}")