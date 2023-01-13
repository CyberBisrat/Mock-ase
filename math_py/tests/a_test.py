import pytest

from math_py.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

def test_base(app):
    client = app.test_client()
    r = client.get('/add?a=2&b=3')
    assert r.status_code == 200
    assert r.json == {'s': 5}
