from solutions import helpers
import numpy as np

filepath = 'input'
# filepath = 'test'

equation_input = helpers.read_each_line_as_string(filepath)

def does_compute(elements: list[int], result: int):
    elements.copy()

    last_element = elements.pop(-1)
    if len(elements) == 0:
        return last_element == result

    if result % last_element == 0:
        return does_compute(elements.copy(), int(result/last_element)) or does_compute(elements.copy(), result - last_element)
    else:
        return does_compute(elements.copy(), result - last_element)


sum_of_computables = 0

for line in equation_input:
    pre, post = line.split(':')
    result = int(pre)
    equation_elements = [int(x) for x in post.strip().split(" ")]

    is_computable = does_compute(equation_elements, result)
    if is_computable:
        sum_of_computables += result


print(sum_of_computables)