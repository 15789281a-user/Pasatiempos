from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
@app.route('/grafo')
def grafo():
    return render_template('grafo.html')


@app.route('/sol', methods = ['POST'])
def sol():
    data = []
    for i in range(0, 6):
        aux = 'i' + str(i)        
        data_i = request.form[aux]
        data.append(data_i)
