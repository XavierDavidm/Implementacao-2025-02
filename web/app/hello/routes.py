from flask import Blueprint

hello_bp = Blueprint('hello',__name__)


@hello_bp.route('/')
def index1():
    return "Olá, Mundo!"
@hello_bp.route('/sobre')
def index2():
    return "Olá, David"
