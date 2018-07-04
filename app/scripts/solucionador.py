sol = [0]*9
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


def check(data, i, j):
    for k in connect2[i]:
        filled = True
        value = 0
        for l in range(0, len(connect1[k])):
            if sol[connect1[k][l]] == 0: filled = False
            value += sol[connect1[k][l]]
        if filled and value != data[k]: return False
    return True


def solve(i, data):
    if i == 9:
        sol_file = open('app/tmp/sol_file.txt', 'a')
        sol_file.write(str(sol))
        return

    for j in range(1, 10):
        if not used[j]:
            sol[i] = j
            used[j] = True
            if (check(data, i, j)): solve(i + 1, data)
            sol[i] = 0
            used[j] = False


def main(data):
    open('app/tmp/sol_file.txt', 'w').close()
    solve(0, data)
