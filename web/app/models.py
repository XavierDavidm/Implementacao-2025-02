from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #banco

class User(db.Model): #modelo da tabela 
    #campos(tipo,chaves etc)
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)


