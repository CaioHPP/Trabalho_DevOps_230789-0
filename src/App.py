# Importação dos módulos necessários
import time
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_appbuilder import AppBuilder, SQLA, ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy.exc import OperationalError
from prometheus_flask_exporter import PrometheusMetrics

# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do Prometheus para métricas
metrics = PrometheusMetrics(app)

# Configurações essenciais do app
app.config['SECRET_KEY'] = 'minha_chave_secreta_super_secreta'  # Substitua por uma chave segura
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root_password@mariadb/school_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados e o AppBuilder
db = SQLAlchemy(app)
appbuilder = AppBuilder(app, db.session)

# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AppLogger")

# Modelo representando os alunos
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    class_name = db.Column(db.String(50), nullable=False)
    subjects = db.Column(db.String(200), nullable=False)
    registration = db.Column(db.String(200), nullable=False)
