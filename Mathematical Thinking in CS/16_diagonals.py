def can_be_extended_to_solution(perm, n, num_diagonals):
    # check if the recently updated cell is vaild 
    # 0 if cell has no diagonal
    # 1 if cell has diagonal \
    # 2 if cell has diagonal /
    
    i = len(perm) - 1

    if perm[i] == 0: return True

    BOTTOM = i-5
    LEFT = i-1

    if BOTTOM >= 0:
        # check bottom for opposite diagonal
        if perm[i] == 1 and perm[BOTTOM] == 2: return False
        if perm[i] == 2 and perm[BOTTOM] == 1: return False

    if LEFT >= 0:
        # check left for opposite diagonal
        if perm[i] == 1 and perm[LEFT] == 2: return False
        if perm[i] == 2 and perm[LEFT] == 1: return False
    
    if i % 5 != 4 and perm[i] == 1 and BOTTOM >= 0:
        # ensure cell is not in rightmost column
        # check bottom right for \
        if perm[BOTTOM+1] == 1: return False

    if i % 5 > 0 and perm[i] == 2 and BOTTOM >= 1:
        # ensure cell is not in leftmost column
        # check bottom left for /
        if perm[BOTTOM-1] == 2: return False
    
    return True
    

def extend(perm, n):
    # -1 if undecided cell
    # 0 if cell has no diagonal
    # 1 if cell has diagonal \
    # 2 if cell has diagonal /

    num_diagonals = perm.count(1) + perm.count(2)
    num_undecided = 25 - len(perm)
    diagonals_needed = n - num_diagonals
    
    if num_diagonals >= n:
        print(perm, num_diagonals, len(perm))
        
    # iterate through possible solutions (0, 1, 2)
    for k in range(3):
        
        if len(perm) < 25:

            perm.append(k)

            # check if permutation is still valid
            if can_be_extended_to_solution(perm, n, num_diagonals) and diagonals_needed <= num_undecided:
                extend(perm, n)

            perm.pop()

extend(perm = [], n = 16)

