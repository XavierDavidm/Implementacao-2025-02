from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 
class Tarefa(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.String(80), unique=True, nullable=False)