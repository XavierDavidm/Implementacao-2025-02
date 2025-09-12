from flask import Blueprint, render_template, request, Response, redirect, url_for
from ..models import Tarefa, db
#from web.app.models import User, db


hello_bp = Blueprint('hello',__name__)

#decorator
@hello_bp.route('/')
def index():
    tarefas=Tarefa.query.all()
    return render_template('index.html',tarefas=tarefas) #retorna o html da file index.html

#tarefa criação e leitura
@hello_bp.route('/novaTarefa', methods=['POST'])
def novaTarefa():
    descricao_tarefa = request.form['desc_tarefa']
    nova_tarefa = Tarefa(descricao = descricao_tarefa) #a linha está soblinhada em Tarefa(descricao) mas está rodando corretamente
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


