import math
from solutions import helpers

filepath = 'input'
# filepath = 'test'

equation_input = helpers.read_each_line_as_string(filepath)


def does_compute(elements: list[int], total: int):
    last_element = elements.pop(-1)
    if len(elements) == 0:
        return last_element == total

    order_of_magnitude = 10**(math.floor(math.log10(last_element)) + 1)

    if total % last_element == 0:
        return (
                does_compute(elements.copy(), int(total/last_element)) or
                does_compute(elements.copy(), total - last_element) or
                does_compute(elements.copy(), (total - last_element) / order_of_magnitude)
        )
    else:
        return (
            does_compute(elements.copy(), total - last_element) or
            does_compute(elements.copy(), (total - last_element) / order_of_magnitude)
        )

sum_of_computables = 0

for line in equation_input:
    pre, post = line.split(':')
    result = int(pre)
    equation_elements = [int(x) for x in post.strip().split(" ")]

    is_computable = does_compute(equation_elements, result)
    if is_computable:
        sum_of_computables += result

print(sum_of_computables)

# 2941973819040 part 1
# 249943041417600
