import re

passports = []
passport = []
with open('input.txt', 'r') as f:
    for line in f:
        content = line.strip('\n')
        passport.append(content)

        empty = re.compile(r"^$")
        m = empty.match(content)
        if m:
            passports.append(passport[:-1])
            passport = []

passports.append(passport)
print(len(passports))


def hgt_validator(x):
    if re.match(r"^\d{3}cm$", x) or re.match(r"^\d{2}in$", x):
        if "cm" in x:
            return 150 <= int(x[0:3]) <= 193
        elif "in" in x:
            return 59 <= int(x[0:2]) <= 76

    return False


rules = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': hgt_validator,
    'hcl': lambda x: re.match(r"^#[0-9a-f]{6}$", x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match(r"^[0-9]{9}$", x)
}

required_fields = ['ecl', 'hcl', 'hgt', 'pid', 'byr', 'eyr', 'iyr']

n_valid = 0
for passport in passports:
    full_passport = " ".join(passport) + " "

    passport_data = re.findall(r"\b([a-z]{3}):(.*?)\s", full_passport)
    dict_data = dict(passport_data)
    print(dict_data)

    present_fields = [x[0] for x in passport_data]
    intersection = [field in present_fields for field in required_fields]

    if sum(intersection) == 7:
        rules_valid = [bool(rules[field](dict_data[field])) for field in required_fields]
        print(rules_valid)
        if sum(rules_valid) == 7:
            n_valid += 1


print(n_valid)