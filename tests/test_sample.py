# tests/test_sample.py
import sys
from pathlib import Path

# Add the path to the root directory of your project
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app  # Import the Flask app here
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test the index page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Student Exam Performance Indicator' in response.data
