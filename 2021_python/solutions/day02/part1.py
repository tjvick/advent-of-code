from solutions import helpers

filename = 'input'

instructions = helpers.read_each_line_as_string(filename)

(x, y) = (0, 0)
for instruction in instructions:
    (direction, amt) = instruction.split()
    amt = int(amt)
    match direction:
        case "forward":
            x += amt
        case "down":
            y += amt
        case "up":
            y -= amt

print(x, y)
print(x*y)


