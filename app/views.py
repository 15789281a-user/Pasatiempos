from flask import render_template, request
from app import app
from app.scripts import solucionador as solu
from app.scripts import generador as gen
from app.scripts import comprobador as comp


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/grafo')
def grafo():
    return render_template('grafo.html')


@app.route('/solucionador', methods = ['POST'])
def solucionador():
    data = []
    for i in range(0, 7):
        aux = 'i' + str(i)        
        data_i = request.form[aux]
        data.append(int(data_i))

    solu.main(data)
    sol_file = open('app/tmp/sol_file.txt', 'r')
    sols_str = str(sol_file.readlines())
    
    aux = []
    cont = 0
    for i in range(0, len(sols_str)):
        c = sols_str[i]
        if c != '[' and c != ' ' and c != ']' and c != ',' and c != "'":
            aux.append(int(c))
            cont += 1

    sols = []
    for i in range(0, int(cont/9)):
        sols.append([])
        for j in range(0, 9):
            sols[i].append(aux[9*i + j])
    n = len(sols)
    
    return render_template('solucionador.html', n = n, sol = sols, data = data)


@app.route('/comprobador', methods = ['POST'])
def comprobador():
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

    check = comp.check(data, sol)

    return render_template('comprobador.html', check = check)


@app.route('/generador')
def generador():
    grafos = gen.generador_main(1)
    # grafos = [
    #     [3, 4, 5, 2, 1, 6, 1],
    #     [3, 4, 5, 2, 1, 6, 2],
    #     [3, 4, 5, 2, 1, 6, 3],
    #     [3, 4, 5, 2, 1, 6, 4]        
    # ]
    n = len(grafos)
    print(grafos)
    
    return render_template('generador.html', n = n, grafos = grafos)


@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html')
