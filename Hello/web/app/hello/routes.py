from flask import Blueprint, render_template, request, Response, redirect, url_for

hello_bp = Blueprint('hello',__name__)

#decorator
@hello_bp.route('/')
def index1():
        return "Olá, Mundo!"
@hello_bp.route('/sobre')
def index2():
        return "Olá, [Seu Nome]!"


