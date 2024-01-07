from functools import lru_cache

@lru_cache(maxsize=128)
def solve_row(record, groups):
    record = record.lstrip('.')
    #print(record)
    if record == '':
        #print('here')
        return int(groups == ()) 
    if groups == ():
        #print('here1')
        return int(record.find('#') == -1)
    
    if record[0] == '#':
        if len(record) < groups[0] or '.' in record[:groups[0]]:
            #print('here2')
            return 0
        elif len(record) == groups[0]:
            #print('here3')
            return int(len(groups) == 1)
        elif record[groups[0]] == '#':
            #print('here4')
            return 0
        else:
            #print('here5')
            return solve_row(record[groups[0]+1:], groups[1:])

    return solve_row('#'+record[1:], groups) + solve_row(record[1:], groups)


if __name__ == "__main__":
    records = []
    
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            record_str, groups = line.split(' ')
            record_str = (record_str+'?')*4 + record_str
            groups = groups.split(',')
            groups = [int(g) for g in groups]
            groups = groups*5
            records.append([record_str, tuple(groups)])

    sol = 0
    
    for [record, groups] in records:
        s = solve_row(record, groups)
        sol += s
        
print(f'The solution is {sol}')