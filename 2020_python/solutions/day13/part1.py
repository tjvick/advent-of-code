import numpy as np
import re

with open('input', 'r') as f:
    file_contents = [line.strip('\n') for line in f]

departure = int(file_contents[0])
schedule = file_contents[1]

buses = np.array([int(bus) for bus in re.findall(r'(\d+),', schedule)])
print(buses)
print(departure % buses)
x = buses - departure % buses

print(x[np.argmin(x)])
print(buses[np.argmin(x)])
print(x[np.argmin(x)] * buses[np.argmin(x)])

