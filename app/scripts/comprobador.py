used = [False]*10
connect1 = [
    [0, 1, 2],
    [0, 2, 3, 5],
    [1, 2, 4, 6],
    [2, 5, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 6, 7, 8],
]
connect2 = [
    [0, 1],
    [0, 2],
    [0, 1, 2, 3],
    [1, 4],
    [2, 5],
    [1, 3, 4, 6],
    [2, 3, 5, 6],
    [4, 6],
    [5, 6],
]


def check(data, sol):
    for i in range(0, 9):
        if sol[i] <= 9 and sol[i] >= 1:
            used[sol[i]] = True
        else: return False
    if used != [False] + [True]*9: return False
        
    for k in range(0, 7):
        filled = True
        value = 0
        for l in range(0, len(connect1[k])):
            if sol[connect1[k][l]] == 0: filled = False
            value += sol[connect1[k][l]]
        if filled and value != data[k]: return False
    return True
