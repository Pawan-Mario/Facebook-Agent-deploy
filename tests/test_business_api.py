import pytest
from app import create_app
from app.utils.mock_data import SAMPLE_BUSINESSES

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

# def test_business_profile(client):
#     # Test with known mock business URL
#     test_url = 'https://fitlifegym.com/about'
#     response = client.post('/api/business-profile', json={'website_url': test_url})
    
#     assert response.status_code == 200
#     data = response.get_json()
#     assert data['name'] == 'FitLife Gym'
#     assert 'Fitness' in data['industry']
#     assert len(data['services']) > 0


def test_business_profile(client):
    test_url = 'https://fitlifegym.com/about'
    response = client.post('/api/business-profile', json={'website_url': test_url})
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'name' in data
    assert 'industry' in data
    assert 'services' in data
    assert isinstance(data['services'], list)

    
def test_invalid_url(client):
    response = client.post('/api/business-profile', json={'website_url': ''})
    assert response.status_code == 400