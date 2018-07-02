from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
@app.route('/grafo')
def grafo():
    return render_template('grafo.html')
