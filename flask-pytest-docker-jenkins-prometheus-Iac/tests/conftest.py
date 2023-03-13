import pytest
from app import create_app
from app.models import db

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='session')
def client(app):
    with app.test_client() as client:
        yield client
