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

required_fields = ['ecl', 'hcl', 'hgt', 'pid', 'byr', 'eyr', 'iyr']

n_valid = 0
for passport in passports:
    full_passport = " ".join(passport)
    print(full_passport)

    present_fields = re.findall(r"\b([a-z]{3}):", full_passport)
    print(present_fields)

    intersection = [field in present_fields for field in required_fields]
    print(intersection)

    print(sum(intersection) == 7)
    if sum(intersection) == 7:
        n_valid += 1


print(n_valid)
