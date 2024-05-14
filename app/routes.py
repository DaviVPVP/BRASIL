from app import app
from flask import render_template
from flask import request

@app.route('/') #Configurando um rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Início", nome="Davids")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Dani Alves", nome="Davids")

@app.route('/tres')
def tres():
    return render_template('tres.html', titulo="Thiago Silva", nome="Davids")

@app.route('/four')
def four():
    return render_template('four.html', titulo="Marcelo", nome="Davids")

@app.route('/cassio')
def cassio():
    return render_template('cassio.html', titulo="Cassio", nome="Davids")

@app.route('/case')
def case():
    return render_template('case.html', titulo="Casemiro", nome="Davids")







