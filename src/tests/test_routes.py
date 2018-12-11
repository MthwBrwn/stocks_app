from .. import app


def test_home_route_get():
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'<h1>Welcome to the site</h1>' in rv.data


def test_home_route_delete():
    rv = app.test_client().delete('/')
    assert rv.status_code == 405
