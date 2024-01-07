from functools import lru_cache

@lru_cache(maxsize=128)
def solve_row(record, groups):
    record = record.lstrip('.')
    if record == '':
        return int(groups == ()) 
    if groups == ():
        return int(record.find('#') == -1)
    
    if record[0] == '#':
        if len(record) < groups[0] or '.' in record[:groups[0]]:
            return 0
        elif len(record) == groups[0]:
            return int(len(groups) == 1)
        elif record[groups[0]] == '#':
            return 0
        else:
            return solve_row(record[groups[0]+1:], groups[1:])

    return solve_row('#'+record[1:], groups) + solve_row(record[1:], groups)


if __name__ == "__main__":
    records = []
    
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            record_str, groups = line.split(' ')
            groups = groups.split(',')
            groups = [int(g) for g in groups]
            records.append([record_str, tuple(groups)])

    sol = 0
    
    for [record, groups] in records:
        s = solve_row(record, groups)
        sol += s
        
print(f'The solution is {sol}')