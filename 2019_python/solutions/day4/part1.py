count = 0
for password_int in range(138307, 654504+1):
    password = str(password_int)
    prev = 0
    hasDouble = False
    increases = True
    for char in password:
        if int(char) == prev:
            hasDouble = True
        if int(char) < prev:
            increases = False

        prev = int(char)

    if hasDouble and increases:
        count += 1

print(count)