from flask import Blueprint, request, jsonify
from app.services.content_service import generate_posts, schedule_posts
from app.models.post_model import ScheduledPost
from app.services.news_service import get_industry_news

bp = Blueprint('content', __name__, url_prefix='/api')

@bp.route('/generate-content', methods=['POST'])
def generate_content():
    data = request.get_json()
    posts = generate_posts(
        data.get('business_profile'),
        data.get('news_items'),
        data.get('preferences', {})
    )
    return jsonify({'posts': posts})

@bp.route('/schedule-posts', methods=['POST'])
def create_schedule():
    data = request.get_json()
    schedule = schedule_posts(
        data.get('posts'),
        data.get('frequency', 3),
        data.get('preferred_days', [])
    )
    return jsonify({'schedule': schedule})

@bp.route('/industry-news', methods=['POST'])
def industry_news():
    """
    Get industry news for a specific industry
    Example request body:
    {
        "industry": "Fitness"
    }
    """
    data = request.get_json()
    industry = data.get('industry')
    
    if not industry:
        return jsonify({'error': 'Industry field is required'}), 400
    
    news_items = get_industry_news(industry)
    return jsonify({'news': news_items})