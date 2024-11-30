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


# Tentativa de conexão ao banco de dados
connection_attempts = 5
for attempt in range(connection_attempts):
    try:
        with app.app_context():
            db.create_all()  # Configurando o banco de dados
            if not appbuilder.sm.find_user(username='admin'):
                appbuilder.sm.add_user(
                    username='admin',
                    first_name='Admin',
                    last_name='User',
                    email='admin@admin.com',
                    role=appbuilder.sm.find_role(appbuilder.sm.auth_role_admin),
                    password='admin'
                )
        logger.info("Banco de dados configurado com sucesso.")
        break
    except OperationalError:
        if attempt < connection_attempts - 1:
            logger.warning("Falha ao conectar ao banco de dados. Retentando em 5 segundos...")
            time.sleep(5)
        else:
            logger.error("Excesso de falhas ao conectar ao banco de dados.")
            raise
