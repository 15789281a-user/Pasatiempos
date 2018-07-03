from flask import render_template, request
from app import app
from app.scripts import grafo as gr


@app.route('/')
@app.route('/index')
@app.route('/grafo')
def grafo():
    return render_template('grafo.html')


@app.route('/sol', methods = ['POST'])
def sol():
    data = []
    for i in range(0, 7):
        aux = 'i' + str(i)        
        data_i = request.form[aux]
        data.append(int(data_i))

    gr.main(data)
    sol_file = open('app/tmp/sol_file.txt', 'r')
    sols_str = str(sol_file.readlines())
    
    aux = []
    cont = 0
    for i in range(0, len(sols_str)):
        c = sols_str[i]
        print(c)
        if c != '[' and c != ' ' and c != ']' and c != ',' and c != "'":
            aux.append(int(c))
            cont += 1

    sols = []
    for i in range(0, int(cont/9)):
        sols.append([])
        for j in range(0, 9):
            sols[i].append(aux[9*i + j])
        
    print(sols)
    
    n = len(sols)
    
    return render_template('sol.html', n = n, sol = sols, data = data)


@app.route('/comp', methods = ['POST'])
def comp():
    data = []
    for i in range(0, 7):
        aux = 'i' + str(i)        
        data_i = request.form[aux]
        data.append(data_i)
        
    sol = []
    for i in range(0, 9):
        aux = 's' + str(i)
        sol_i = request.form[aux]
        sol.append(sol_i)

    return render_template('comp.html')
