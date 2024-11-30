import pytest
from flask import Flask
from flask.testing import FlaskClient

# Importar a aplicação Flask
from app import app  # Assumindo que seu arquivo principal é app.py

@pytest.fixture
def client():
    """Fixture para configurar o cliente de teste Flask."""
    with app.test_client() as client:
        yield client

def test_get_students(client: FlaskClient):
    """Testa a rota GET /students"""
    response = client.get('/students')
    assert response.status_code == 200
    assert isinstance(response.json, list), "A resposta deveria ser uma lista de estudantes."

def test_add_student(client: FlaskClient):
    """Testa a rota POST /students"""
    new_student = {
        "first_name": "Caio",
        "last_name": "Henrique",
        "class_name": "8 período",
        "subjects": "TADS",
        "registration": "2307890"
    }
    response = client.post('/students', json=new_student)
    assert response.status_code == 201
    assert response.json['message'] == 'Aluno cadastrado com sucesso!', "Mensagem de sucesso esperada não corresponde."
