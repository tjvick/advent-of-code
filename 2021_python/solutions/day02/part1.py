from solutions import helpers

filename = 'input'

strings = helpers.read_each_line_as_string(filename)

x = 0
y = 0
for instruction in strings:
    (direction, amt) = instruction.split()
    match direction:
        case "forward":
            x += int(amt)
        case "down":
            y += int(amt)
        case "up":
            y -= int(amt)


print(x, y)
print(x*y)


