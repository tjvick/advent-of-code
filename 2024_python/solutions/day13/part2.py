import re
from dataclasses import dataclass

from solutions import helpers

filepath = 'input'
# filepath = 'test'

input_lines_of_text = helpers.read_each_line_as_string(filepath)

button_a_matcher = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
button_b_matcher = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
prize_matcher = re.compile(r'Prize: X=(\d+), Y=(\d+)')

x_a = y_a = x_b = y_b = x_t = y_t = None
claw_machines = []

@dataclass
class ClawMachine:
    x_a: int
    y_a: int
    x_b: int
    y_b: int
    x_t: int
    y_t: int

    def compute_winning_button_presses(self) -> (float, float):
        s = self
        b_button_presses = (s.y_t * s.x_a - s.y_a * s.x_t) / (s.y_b * s.x_a - s.y_a * s.x_b)
        a_button_presses = (s.x_t / s.x_a - s.x_b / s.x_a * b_button_presses)

        return a_button_presses, b_button_presses

    def tokens_required_to_win_prize(self) -> int:
        a_button_presses, b_button_presses = self.compute_winning_button_presses()
        if not self.is_valid_number_of_presses(a_button_presses, b_button_presses):
            return -1

        return round(a_button_presses * 3 + b_button_presses * 1)

    @staticmethod
    def is_valid_number_of_presses(a_button_presses: float, b_button_presses: float):
        button_presses_are_whole_numbers =  (
                abs(a_button_presses - round(a_button_presses)) < 1e-3 and
                abs(b_button_presses - round(b_button_presses)) < 1e-3
        )
        return button_presses_are_whole_numbers


for line_of_text in input_lines_of_text:
    a_match = button_a_matcher.match(line_of_text)
    b_match = button_b_matcher.match(line_of_text)
    prize_match = prize_matcher.match(line_of_text)
    if a_match:
        x_a, y_a = a_match.groups()
    elif b_match:
        x_b, y_b = b_match.groups()
    elif prize_match:
        x_t, y_t = prize_match.groups()
    else:
        claw_machine = ClawMachine(
            int(x_a), int(y_a),
            int(x_b), int(y_b),
            10000000000000+int(x_t), 10000000000000+int(y_t)
        )
        claw_machines.append(claw_machine)

claw_machine = ClawMachine(
    int(x_a), int(y_a),
    int(x_b), int(y_b),
    10000000000000+int(x_t), 10000000000000+int(y_t)
)
claw_machines.append(claw_machine)


total_tokens_needed = 0

for claw_machine in claw_machines:
    tokens = claw_machine.tokens_required_to_win_prize()
    if 0 < tokens:
        total_tokens_needed += tokens


print(total_tokens_needed)

# 59933050290162 1e-6 too low
# 59933050290162 1e-5
# 73688977111195 1e-4
# 77204516023437 1e-3
# 77204516023437 1e-2