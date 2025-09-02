from flask import Blueprint, render_template
hello_bp = Blueprint('hello',__name__)


@hello_bp.route('/')
def index():
    usuarios=['David','Raphael','Isaac']
    return render_template('index.html', usuarios=usuarios) #retorna o html da file index.html

@hello_bp.route('/sobre')
def index2():
    return "Olá, David"
