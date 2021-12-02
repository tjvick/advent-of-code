from solutions import helpers

filename = 'input'

instructions = helpers.read_each_line_as_string(filename)

(x, y, aim) = (0, 0, 0)
for instruction in instructions:
    (direction, amt) = instruction.split()
    amt = int(amt)
    match direction:
        case "forward":
            x += amt
            y += amt * aim
        case "down":
            aim += amt
        case "up":
            aim -= amt


print(x, y)
print(x*y)


