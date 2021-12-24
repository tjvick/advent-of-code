from solutions import helpers
import numpy as np

np.set_printoptions(edgeitems=30, linewidth=100000)

filename = 'input'

strings = helpers.read_each_line_as_string(filename)


def run_instruction_chunk(d, z, x_var, y_var, z_var):
    if (z % 26) + x_var == d:
        z = int(z / z_var)
    else:
        z = int(z / z_var) * 26 + d + y_var

    return z


def parse_instruction_set():
    x_vars = []
    y_vars = []
    z_vars = []
    for row in strings:
        match row.split():
            case ['inp', _]:
                add_y_count = 0
            case ['add', a, b]:
                if a == 'x':
                    if b != 'z':
                        x_vars.append(int(b))
                if a == 'y':
                    add_y_count += 1
                    if add_y_count == 4:
                        y_vars.append(int(b))
            case ['div', 'z', b]:
                z_vars.append(int(b))

    return x_vars, y_vars, z_vars


# def run_monad(input_digits):
#     digits = iter(str(input_digits))
#
#     register = {
#         'w': 0,
#         'x': 0,
#         'y': 0,
#         'z': 0
#     }
#     register_keys = register.keys()
#
#     def eval_variable(b):
#         if b in register_keys:
#             return register[b]
#         else:
#             return int(b)
#
#     for row in strings:
#         match row.split():
#             case ['inp', a]:
#                 register[a] = int(next(digits))
#             case ['add', a, b]:
#                 b_val = eval_variable(b)
#                 register[a] = register[a] + b_val
#             case ['mul', a, b]:
#                 b_val = eval_variable(b)
#                 register[a] = register[a] * b_val
#             case ['div', a, b]:
#                 b_val = eval_variable(b)
#                 if b_val == 0:
#                     return -1
#                 register[a] = int(register[a] / b_val)
#             case ['mod', a, b]:
#                 b_val = eval_variable(b)
#                 if register[a] < 0 or b_val <= 0:
#                     return -1
#                 register[a] = register[a] % b_val
#             case ['eql', a, b]:
#                 b_val = eval_variable(b)
#                 register[a] = int(register[a] == b_val)
#
#     return register['z']


x_vars, y_vars, z_vars = parse_instruction_set()

upper_bounds = {ix: 26 ** (min(5, 14 - ix)) for ix in range(0, 15)}

all_z_vals = {0: ''}
for ix_digit, (x_var, y_var, z_var) in enumerate(zip(x_vars, y_vars, z_vars)):
    upper_bound = upper_bounds[ix_digit + 1]
    new_z_values = {}
    for z, v in all_z_vals.items():
        for d in range(1, 10):
            k = run_instruction_chunk(d, z, x_var, y_var, z_var)
            if k <= upper_bound:
                new_z_values[k] = v + str(d)

    all_z_vals = new_z_values
    print(f'n z_values after {ix_digit}: {len(new_z_values)}')

print(all_z_vals[0])