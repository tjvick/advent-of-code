total = 0
frequency_set = {0}
solution_found = False
loop_count = 0

while not solution_found:
    print('loop count', loop_count)
    loop_count += 1
    with open('input.txt', 'r') as f:
        for line in f:
            val = int(line.strip('\n'))
            total += val
            if total in frequency_set:
                solution_found = True
                print(total)
                break
            frequency_set.add(total)
