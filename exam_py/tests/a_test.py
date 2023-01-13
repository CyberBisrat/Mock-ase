import pytest

from exam_py.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

def test_base(app):
    client = app.test_client()
    r = client.get('/mulstring?a=Hello&n=3')
    assert r.status_code == 200
    assert r.json == {'s': 'HelloHelloHello'}

def test_negative(app):
    client = app.test_client()
    r = client.get('/mulstring?a=Hello&n=-3')
    assert r.status_code == 400

def test_zero(app):
    client = app.test_client()
    r = client.get('/mulstring?a=Hello&n=0')
    assert r.status_code == 200
    assert r.json == {'s': ''}

def test_empty(app):
    client = app.test_client()
    r = client.get('/mulstring?a=&n=1')
    assert r.status_code == 200
    assert r.json == {'s': ''}

def test_missing(app):
    client = app.test_client()
    r = client.get('/mulstring')
    assert r.status_code == 400