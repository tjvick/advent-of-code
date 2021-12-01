a = [-2, -3, 4, -1, -2, 1, 5, -3]

a.sort()

counter = 0
for ix, el in enumerate(a[1:]):
    if a[ix-1] + 1 == el:
        counter += 1

print(counter)
