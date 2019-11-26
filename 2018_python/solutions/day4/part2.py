import re
from functools import reduce
from statistics import mode
from collections import Counter

all_data = []

with open('input.txt', 'r') as f:
    for line in f:
        pattern = re.compile(r'^\[(.+)\](( falls asleep)|( wakes up)| Guard #(\d+) begins shift)$')
        m = pattern.match(line.strip('\n'))
        timestamp = m.group(1)  # timestamp
        asleep = m.group(3) is not None  # falls asleep
        awake = m.group(4) is not None  # wakes up
        guard_id = m.group(5)  # guard id

        time = int(re.sub(r'[-: ]', '', timestamp))

        line_data = (time, asleep, awake, guard_id)
        all_data.append(line_data)

chron_data = sorted(all_data, key=lambda line_data: line_data[0])

guard_id = None
sleep_record = dict()
asleep_time = 0
awake_time = 0
for event in chron_data:
    time = event[0]
    if event[3] is not None:
        guard_id = event[3]

    if event[1]:
        asleep_time = time

    if event[2]:
        awake_time = time
        minutes_asleep = awake_time - asleep_time
        sleep_minutes = list(range(int(str(asleep_time)[10:]), int(str(awake_time)[10:])))
        if guard_id in sleep_record:
            sleep_record[guard_id] = (sleep_record[guard_id][0] + minutes_asleep, sleep_record[guard_id][1] + sleep_minutes)
        else:
            sleep_record[guard_id] = (minutes_asleep, sleep_minutes)

print(sleep_record)


def max_index(a, b):
    minute_occurrences_b = sorted(Counter(b[1][1]).items(), key=lambda kv: kv[1], reverse=True)
    mode_b = minute_occurrences_b[0][1]

    minute_occurrences_a = sorted(Counter(a[1][1]).items(), key=lambda kv: kv[1], reverse=True)
    mode_a = minute_occurrences_a[0][1]
    if mode_b > mode_a:
        return b
    return a


sleepiest_guard = reduce(max_index, sleep_record.items())
print(sleepiest_guard)
print(sleepiest_guard[0])
print(mode(sleepiest_guard[1][1]))
print(int(sleepiest_guard[0])*mode(sleepiest_guard[1][1]))
