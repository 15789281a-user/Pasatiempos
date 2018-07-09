import random
from Pasatiempos.scripts import grafo_solucionador as gr_sol


def generador_main(n):
    cont = 0
    grafos = []

    while cont < n:
        data = []
        for i in range(0, 7):
            aux = random.randrange(6, 31)
            data.append(aux)

        # gr_sol.main(data)            
        # sol_file = open('Pasatiempos/tmp/gr_sol_file.txt', 'r')
        # sols_str = str(sol_file.readlines())

        # aux = []
        # cont = 0
        # for i in range(0, len(sols_str)):
        #     c = sols_str[i]
        #     if c != '[' and c != ' ' and c != ']' and c != ',' and c != "'":
        #         aux.append(int(c))
        #         cont += 1

        # sols = []
        # for i in range(0, int(cont/9)):
        #     sols.append([])
        #     for j in range(0, 9):
        #         sols[i].append(aux[9*i + j])
        # n_sol = len(sols)

        sols = gr_sol.main(data)
        n_sol = len(sols)

        if n_sol > 0:
            grafos.append(data)
            cont += 1

    return grafos
