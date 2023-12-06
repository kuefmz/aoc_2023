def can_it_win(time_left, distance_left, speed):
    distance_possible = (time_left-1) * speed
    if distance_possible > distance_left:
        return True
    return False



def number_of_ways_to_win_the_race(time, distance):
    number_of_ways = 0
    time_left = time
    distance_left = distance
    for speed in range(1, time):
        time_left -= 1
        distance_left -= 1
        canwin = can_it_win(time_left, distance_left, speed)
        if canwin:
            number_of_ways += 1
        if not canwin and number_of_ways > 0:
            break
    return number_of_ways


if __name__ == '__main__':
    times_list = []
    distances_list = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Time: '):
                _, times = line.split('Time: ')
                times = times.split(' ')
                for time in times:
                    if time.isdigit():
                        times_list.append(int(time))
            if line.startswith('Distance: '):
                _, distances = line.split('Distance: ')
                distances = distances.split(' ')
                for distance in distances:
                    if distance.isdigit():
                        distances_list.append(int(distance))
    all_the_different_ways = 1
    for idx in range(len(times_list)):
        all_the_different_ways *= number_of_ways_to_win_the_race(times_list[idx], distances_list[idx])
    print(f"The solution: {all_the_different_ways}")