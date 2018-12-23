from .. import app
import pytest
from ..models import db


@pytest.fixture
def client():
    """This sets up a fixture that allows a database session to be created and
    added to then rolled back at the end of testing.
    """
    def do_nothing():
        pass
    db.session.commit = do_nothing
    yield app.test_client()
    db.session.rollback()


def test_home_route_get():
    """ This tests the get request and assert the response code is 200
    The request has succeeded
    """
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert b'<h1>Welcome to the site</h1>' in rv.data


def test_home_route_delete():
    """ This checks to make sure a request that is not allowed returns a 405
    """
    rv = app.test_client().delete('/')
    assert rv.status_code == 405


def test_home_route_post():
    """ home has no post functionality this should return back 405
    """
    rv = app.test_client().delete('/')
    assert rv.status_code == 405


def test_search_route_get():
    """
    """
    rv = app.test_client().get('/search')
    assert rv.status_code == 200


def test_portfolio_route_get():
    """This checks to see if a request to the endpoint /
    portfolio has response of 200 The request has succeeded
    """
    rv = app.test_client().get('/portfolio')
    assert rv.status_code == 200
    # assert b'<h2>Welcome to the Portfolio Portal</h2>' in rv.data


def test_search_route_get():
    """"
    This is another test checking if the response is 200 for the endpoint /search.  The request has succeeded
    """
    rv = app.test_client().get('/search')
    assert rv.status_code == 200
    assert b'<h2>Search for stocks</h2>' in rv.data


def test_search_route_delete():
    """ This checks to make sure a request that is not allowed returns a 405 in search
    """
    rv = app.test_client().delete('/search')
    assert rv.status_code == 405


def test_search_post_pre_redirect(client):
    """This test attempts a company a second time within the fixture and then rolls back the session.
    """
    rv = client.post('/search', data={'symbol': 'amzn'})
    assert rv.status_code == 200


def test_search_post(client):
    """  test checking if the response is 200 for the endpoint /search.post.
    This uses the fixture client to check if 2nd time trips the redirect
    """
    rv = client.post('/search', data={'symbol': 'amzn'})
    assert rv.status_code == 200


