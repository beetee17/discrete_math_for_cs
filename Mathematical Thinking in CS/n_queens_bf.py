import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True

num_solutions = 0
for perm in it.permutations(range(8)):
    if is_solution(perm):
        num_solutions += 1
        print(perm)

print(num_solutions)

        