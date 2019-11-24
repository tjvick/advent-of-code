box_id_set = set()

with open('input', 'r') as f:
    for line in f:
        id1 = line.strip('\n')
        for id2 in box_id_set:
            n_chars_diff = 0
            for (a, b) in zip(id1, id2):
                if a != b:
                    n_chars_diff += 1

            if n_chars_diff == 1:
                print(id1)
                print(id2)

        box_id_set.add(id1)
