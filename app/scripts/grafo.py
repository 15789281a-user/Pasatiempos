sol = [0]*9
used = [False]*10
connect = [
    [0, 1, 2],
    [0, 2, 3, 5],
    [1, 2, 4, 6],
    [2, 5, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 6, 7, 8],
]
cont = 0


def check(data):
    for i in range(0, 7):
        filled = True
        value = 0
        for j in range(0, len(connect[i])):
            if sol[connect[i][j]] == 0: filled = False
            value += sol[connect[i][j]]
        if filled and value != data[i]: return False
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
            if (check(data)): solve(i + 1, data)
            sol[i] = 0
            used[j] = False


def main(data):
    open('app/tmp/sol_file.txt', 'w').close()
    solve(0, data)
