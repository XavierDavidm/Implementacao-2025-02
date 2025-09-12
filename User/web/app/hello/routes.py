from flask import Blueprint, render_template, request, Response, redirect, url_for
from ..models import User, Tarefa, db
#from web.app.models import User, db


hello_bp = Blueprint('hello',__name__)

#decorator
@hello_bp.route('/')
def index():
    usuarios=User.query.all()
    tarefas=Tarefa.query.all()
    return render_template('index.html', usuarios=usuarios,tarefas=tarefas) #retorna o html da file index.html

#faz a request do form do index.html
@hello_bp.route('/novoUsuario', methods=['POST'])
def novoUsuario():
    nome_usuario = request.form['nome_usuario']

    novo_usuario = User(username = nome_usuario)
    db.session.add(novo_usuario)
    db.session.commit()
    return redirect('/')

#remover usuario usando id
@hello_bp.route ('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    #incluir url_for direto no redirect
    return redirect(url_for('hello.index'))

#editar
@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get(usuario_id)
    if usuario:
        usuario.username = request.form['nome_usuario']
        db.session.commit()
    return redirect(url_for('hello.index'))

#tarefa criação e leitura
@hello_bp.route('/novaTarefa', methods=['POST'])
def novaTarefa():
    descricao_tarefa = request.form['desc_tarefa']
    nova_tarefa = Tarefa(descricao = descricao_tarefa)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect('/')

@hello_bp.route('/removerTarefa/<int:tarefa_id>', methods=['POST'])
def removerTarefa(tarefa_id):
    tarefa=Tarefa.query.get(tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('hello.index'))

@hello_bp.route('/editarTarefa/<int:tarefa_id>', methods=['POST'])
def editarTarefa(tarefa_id):
    tarefa=Tarefa.query.get(tarefa_id)
    if tarefa:
        tarefa.descricao = request.form['desc_tarefa']
        db.session.commit()
    return redirect(url_for('hello.index'))


