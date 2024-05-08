from app import app
from flask import render_template
from flask import request

@app.route('/') #Configurando um rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Davids")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Davids")

@app.route('/Dani Alves')
def tres():
    return render_template('tres.html', titulo="Dani Alves", nome="Davids")



