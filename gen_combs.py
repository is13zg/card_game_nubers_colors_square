from itertools import permutations

perms = list(permutations("1234", 4))
main_set = set()
for x in perms:
    t_set = set()
    tx = list(x)
    t_set.add(x)
    for ii in range(3):
        tx = tx[1:] + tx[:1]
        t_set.add(tuple(tx))
    if len(main_set.intersection(t_set)) == 0:
       main_set.add(x)
print(main_set)