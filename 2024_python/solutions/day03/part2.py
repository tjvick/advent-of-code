import re

from solutions import helpers

filepath = 'input'
# filepath = 'test'

instructions = helpers.read_each_line_as_string(filepath)
single_line_instructions = ''.join(instructions)

mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
do_pattern = re.compile(r'do\(\)')
dont_pattern = re.compile(r'don\'t\(\)')

mul_matcher = mul_pattern.finditer(single_line_instructions)
do_matcher = do_pattern.finditer(single_line_instructions)
dont_matcher = dont_pattern.finditer(single_line_instructions)

switches = {
    -1: True,
    **{m.start(): True for m in do_matcher},
    **{m.start(): False for m in dont_matcher}
}
products = {m.start(): int(m.group(1)) * int(m.group(2)) for m in mul_matcher}

total = 0
for product_index in products:
    previous_switch_index = max(switch_index for switch_index in switches if switch_index < product_index)
    if switches[previous_switch_index]:
        total += products[product_index]


print(total)