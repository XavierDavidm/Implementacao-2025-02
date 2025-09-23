from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
class UsuarioForm(FlaskForm):
    nome_usuario = StringField('Nome de Usuario', validators=[DataRequired(message="O Nome do usuário é obrigatório.")])
    submit = SubmitField('Salvar')
    

