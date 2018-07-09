from flask import Flask
from flask import render_template, request

app = Flask(__name__)


from Pasatiempos.scripts import grafo_solucionador as gr_solu
from Pasatiempos.scripts import grafo_generador as gr_gen
from Pasatiempos.scripts import grafo_comprobador as gr_comp
from Pasatiempos.scripts import sudoku_solucionador as su_solu


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/grafo')
def grafo():
    return render_template('grafo.html')


@app.route('/grafo/solucionador', methods = ['POST'])
def grafo_solucionador():
    data = []
    for i in range(0, 7):
        aux = 'i' + str(i)        
        data_i = request.form[aux]
        data.append(int(data_i))

    # gr_solu.main(data)
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
    sols = gr_solu.main(data)
    n = len(sols)
    
    return render_template('grafo_solucionador.html', n = n, sol = sols, data = data)


@app.route('/grafo/comprobador', methods = ['POST'])
def grafo_comprobador():
    data = []
    for i in range(0, 7):
        aux = 'i' + str(i)        
        data_i = int(request.form[aux])
        data.append(data_i)
        
    sol = []
    for i in range(0, 9):
        aux = 's' + str(i)
        sol_i = int(request.form[aux])
        sol.append(sol_i)

    check = gr_comp.check(data, sol)

    return render_template('grafo_comprobador.html', check = check)


@app.route('/grafo/generador')
def grafo_generador():
    grafos = gr_gen.generador_main(1)
    # grafos = [
    #     [17, 25, 16, 17, 14, 14, 21]
    # ]
    n = len(grafos)
    print(grafos)
    
    return render_template('grafo_generador.html', n = n, grafos = grafos)


@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html')


@app.route('/sudoku/solucionador', methods = ['POST'])
def sudoku_solucionador():
    data = []
    for i in range(0, 9):
        aux = []        
        for j in range(0, 9):
            aux_s = str(i) + str(j)  
            data_ij = request.form[aux_s]
            if data_ij == '': data_ij = 0
            aux.append(int(data_ij))
        data.append(aux)

    grid = []
    for i in range(0, 9):
        aux = []
        for j in range(0, 9):
            aux.append(data[i][j])
        grid.append(aux)

    sols = su_solu.main(grid)
    # sol_file = open('Pasatiempos/tmp/su_sol_file.txt', 'r')
    # sols_str = str(sol_file.readlines())

    # aux = []
    # cont = 0
    # for i in range(0, len(sols_str)):
    #     c = sols_str[i]
    #     if c != '[' and c != ' ' and c != ']' and c != ',' and c != "'":
    #         aux.append(int(c))
    #         cont += 1

    # sols = []
    # for k in range(0, int(cont/81)):
    #     sols.append([])
    #     for i in range(0, 9):
    #         fil = []
    #         for j in range(0, 9):
    #             fil.append(aux[81*k + 9*i + j])
    #         sols[k].append(fil)


    print(sols)    
    n = len(sols)
    
    return render_template('sudoku_solucionador.html', data = data,
                           n = n, sols = sols)


@app.route('/sudoku/comprobador', methods = ['POST'])
def sudoku_comprobador():
    return render_template('sudoku_comprobador.html')


@app.route('/sudoku/generador', methods = ['POST'])
def sudoku_generador():
    return render_template('sudoku_generador.html')
