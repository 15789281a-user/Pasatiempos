sol = [0]*9
data = [18, 16, 23, 10, 13, 14, 16]
used = [False]*10
cont = 0
connect = [
    [0, 1, 2],
    [0, 2, 3, 5],
    [1, 2, 4, 6],
    [2, 5, 6],
    [3, 5, 7],
    [4, 6, 8],
    [5, 6, 7, 8],
]


def check():
    for i in range(0, 7):
        filled = True
        value = 0
        for j in range(0, len(connect[i])):
            if sol[connect[i][j]] == 0: filled = False
            value += sol[connect[i][j]]
        if filled and value != data[i]: return False
    return True


def solve(i):
    if i == 9:
        # cont += 1
        return print(sol)

    for j in range(1, 10):
        if not used[j]:
            sol[i] = j
            used[j] = True
            if (check()): solve(i + 1)
            sol[i] = 0
            used[j] = False

            
solve(0)
if cont == 0:
    print('No se ha encontrado ninguna solución.')
