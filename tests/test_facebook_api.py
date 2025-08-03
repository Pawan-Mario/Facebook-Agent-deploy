import pytest
from app import create_app
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app  # Now this should work
from app.utils.mock_data import SAMPLE_BUSINESSES
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_facebook_connection(client):
    response = client.post('/api/connect-facebook', json={'page_id': '12345'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'fb_mock_token' in data['token']

def test_publish_post(client):
    test_post = {
        'post_content': 'Test post content',
        'page_id': '12345'
    }
    response = client.post('/api/publish-post', json=test_post)
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'facebook.com' in data['post_url']