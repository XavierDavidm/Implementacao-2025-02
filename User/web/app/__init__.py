from flask import Flask
from .hello.routes import hello_bp
from .models import db
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    #app.secret_key='584c7d374dfc3d821349fdf26457f513352578700614798f'
    #banco
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    app.register_blueprint(hello_bp)
    return app


