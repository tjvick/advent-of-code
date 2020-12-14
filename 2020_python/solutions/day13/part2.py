import numpy as np
import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

schedule = file_contents[1]
# schedule = '7,13,x,x,59,x,31,19'
# schedule = '1789,37,47,1889'

bus_ids = np.array([int(bus) for bus in re.findall(r'(\d+),?', schedule)])
schedule = schedule.split(",")
req_departures = [int(np.argwhere(np.array(schedule) == str(bus_id))) for bus_id in bus_ids]


print(bus_ids)
print(req_departures)
print()


x = 0
search_index = 1
step = bus_ids[0]
started = False
period_start = 0
n_steps = 0
while True:
    time_to_departure = bus_ids - x % bus_ids
    if time_to_departure[search_index] == req_departures[search_index] % bus_ids[search_index]:
        if started:
            print("second time")
            period_end = x

            started = False
            search_index += 1
            step = period_end - period_start
            n_steps = 0
            x = x - step - step
            print("step size", step)
            print("returning to", x + step)
            print()
            if search_index == len(bus_ids):
                print("Answer:", period_start)
                break
        else:
            print("bus #", search_index)
            print("first time")
            period_start = x
            started = True

    n_steps += 1
    x += step