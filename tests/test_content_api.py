import pytest
from app import create_app
from app.utils.mock_data import SAMPLE_BUSINESSES, INDUSTRY_NEWS
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

def test_content_generation(client):
    test_data = {
        'business_profile': SAMPLE_BUSINESSES[0],
        'news_items': INDUSTRY_NEWS['Fitness'],
        'preferences': {
            'tone': 'motivational',
            'post_type': 'tip'
        }
    }
    
    response = client.post('/api/generate-content', json=test_data)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['posts']) > 0
    assert 'FitLife' in data['posts'][0] or 'Fitness' in data['posts'][0]

def test_schedule_posts(client):
    test_posts = [
        "Post 1 content",
        "Post 2 content",
        "Post 3 content"
    ]
    response = client.post('/api/schedule-posts', json={
        'posts': test_posts,
        'frequency': 3
    })
    
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['schedule']) == 3

def test_industry_news(client):
    # Test with valid industry
    response = client.post('/api/industry-news', json={'industry': 'Fitness'})
    assert response.status_code == 200
    assert len(response.json['news']) > 0
    
    # Test missing industry field
    response = client.post('/api/industry-news', json={})
    assert response.status_code == 400