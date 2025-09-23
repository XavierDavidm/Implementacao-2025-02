from flask import Blueprint, render_template, request, Response, redirect, url_for, flash
from ..models import User, db
from .forms import UsuarioForm


hello_bp = Blueprint('hello',__name__)

#decorator
@hello_bp.route('/')
def index():
    usuarios=User.query.all()
    form=UsuarioForm()
    return render_template('index.html', usuarios=usuarios, form=form) #retorna o html da file index.html

#faz a request do form do index.html
@hello_bp.route('/novoUsuario', methods=['POST'])
def novoUsuario():
    form=UsuarioForm()
    if form.validate_on_submit():
        nome_usuario = form.nome_usuario.data
        novo_usuario = User(username = nome_usuario)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuario Criado com sucesso!','sucess')
    else:
        for field, errors in form.errors.items():
            flash(F"Erro no campo '{getattr(form,field).label.text}': {error}", 'danger')
    return redirect(url_for('hello.index'))

#remover usuario usando id
@hello_bp.route ('/removerUsuario/<int:usuario_id>', methods=['POST'])
def removerUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário removido com sucesso','sucess')
    #incluir url_for direto no redirect
    return redirect(url_for('hello.index'))

#editar
@hello_bp.route('/editarUsuario/<int:usuario_id>', methods=['POST'])
def editarUsuario(usuario_id):
    usuario = User.query.get_or_404(usuario_id)
    form = UsuarioForm(obj=usuario)
    if form.validate_on_submit():
        usuario.username=form.nome_usuario.data
        db.session.commit()
        flash('Usuário editado com sucesso!','sucess')
    return redirect(url_for('hello.index'))



