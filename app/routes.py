from app import app
from flask import render_template
from flask import request
import json
import requests
link = "https://flaskti18n-4afd9-default-rtdb.firebaseio.com/"

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

@app.route('/cadastro', methods=['POST'])
def cadastro():
    try:
        email        = request.form.get("email")
        senha        = request.form.get("senha")
        dados      = {"email":email,"senha":senha}
        requisicao = requests.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n + {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #SolicitaDadosDoBanco
        dicionario = requisicao.json()
        return dicionario

    except Exception as e:
        return f'Ocorreu um erro!\n\n + {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            usuario = dicionario[codigo]['email']
            if usuario == "allan@ad":
                idCadastro = codigo
        return idCadastro
    except Exception as e:
        return f'Algo deu errado!\n\n + {e}'

# -NySQnFYhcqZa52HjaK1

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome":"Gabriela"}#Parâmetro para atualização
        requisicao = requests.patch(f'{link}/cadastrar/--NySQnFYhcqZa52HjaK1/.json', data=json.dumps(dados))
        return "Atualizado com sucesso!"

    except Exception as e:
        return f'Houve um erro!\n\n + {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/-NySQnFYhcqZa52HjaK1/.json')
        return "Excluído com sucesso!"
    except Exception as e:
        return f'Houve um erro\n\n + {e}'









