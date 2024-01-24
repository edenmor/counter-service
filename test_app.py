# test_payoneer.py
import pytest
from payoneer import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_counter_initial(client):
    """Test the GET / route for initial counter value."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Total POST Requests: 0" in response.data

def test_post_increment(client):
    """Test the POST / route to increment the counter."""
    client.post("/")
    response = client.get("/")
    assert response.status_code == 200
    assert b"Total POST Requests: 1" in response.data
