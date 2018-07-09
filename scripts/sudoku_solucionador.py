fil = [[False]*10 for i in range(10)]
col = [[False]*10 for i in range(10)]
cuad = [[[False]*10 for i in range(10)] for j in range(10)]
grid = [[False]*9 for i in range(9)]
sols = []
finished = False


# def check(i, j, k, grid):
#     for l in range(0, 9):
#         if grid[i][l] == k and l != j:
#             return False
#     for l in range(0, 9):
#         if grid[l][j] == k and l != i:
#             return False
#     for l in range(3*int(i/3), 3*int(i/3) + 3):
#         for m in range(3*int(j/3), 3*int(j/3) + 3):
#             if (l !=  i or m != j) and grid[l][m] == k:
#                 return False
#     return True


def actualiza(i, j, k, to):
    if to == True:
        fil[i][k] = True
        col[j][k] = True
        cuad[int(i/3)][int(j/3)][k] = True
    else:
        fil[i][k] = False
        col[j][k] = False
        cuad[int(i/3)][int(j/3)][k] = False


def check(i, j, k):
    if not fil[i][k] and not col[j][k] and not cuad[int(i/3)][int(j/3)][k]:
        return True
    return False


def solve(i, j):
    if i == 9:
        sols.append([])
        for ip in range(0, 9):
            sols[len(sols) - 1].append([])
            aux = [0]*9
            for jp in range(0, 9):
                sols[len(sols) - 1][ip].append(grid[ip][jp])
        return

    if j == 9:
        solve(i + 1, 0)
        return

    if grid[i][j] != 0:
        solve(i, j + 1)
        return

    for k in range(1, 10):
        if check(i, j, k):
            grid[i][j] = k
            actualiza(i, j, k, True)
            solve(i, j + 1)
            grid[i][j] = 0            
            actualiza(i, j, k, False)
            

def main(grid_input):
    open('Pasatiempos/tmp/su_sol_file.txt', 'w').close()

    for i in range(0, 9):
        for j in range(0, 9):
            grid[i][j] = grid_input[i][j]
            a = grid[i][j]
            if a > 9 or a <= 0: return
            if fil[i][a] == True:
                return
            else:
                fil[i][a] = True
            if col[j][a] == True:
                return
            else:
                col[j][a] = True
            if cuad[int(i/3)][int(j/3)][a] == True:
                return
            else:
                cuad[int(i/3)][int(j/3)][a] = True

    solve(0, 0)

    return sols
