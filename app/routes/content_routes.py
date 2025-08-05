from flask import Blueprint, request, jsonify
from app.services.content_service import generate_posts, schedule_posts
from app.models.post_model import ScheduledPost
from app.services.news_service import get_industry_news

bp = Blueprint('content', __name__, url_prefix='/api')

# @bp.route('/generate-content', methods=['POST'])
# def generate_content():
#     data = request.get_json()
#     posts = generate_posts(
#         data.get('business_profile'),
#         data.get('news_items'),
#         data.get('preferences', {})
#     )
#     return jsonify({'posts': posts})

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
    try:
        data = request.get_json()
        industry = data.get('industry')
        
        if not industry:
            return jsonify({
                'error': 'Industry field is required',
                'example': {'industry': 'fitness'}
            }), 400
            
        news_items = get_industry_news(industry)
        
        return jsonify({
            'status': 'success',
            'count': len(news_items),
            'news': news_items
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to fetch industry news',
            'details': str(e)
        }), 500

# @bp.route('/industry-news', methods=['POST'])
# def industry_news():
#     try:
#         data = request.get_json()
#         industry = data.get('industry', '').strip()
        
#         if not industry:
#             return jsonify({
#                 'error': 'Industry field is required',
#                 'example': {'industry': 'technology'}
#             }), 400
            
#         news_items = get_industry_news(industry)
        
#         return jsonify({
#             'status': 'success',
#             'count': len(news_items),
#             'news': news_items
#         })
        
#     except Exception as e:
#         return jsonify({
#             'error': 'Failed to fetch news',
#             'details': str(e)
#         }), 500

# @bp.route('/generate-content', methods=['POST'])
# def generate_content():
#     try:
#         data = request.get_json()
        
#         required_fields = ['business_profile', 'preferences']
#         if not all(field in data for field in required_fields):
#             return jsonify({
#                 'error': 'Missing required fields',
#                 'required': required_fields
#             }), 400
            
#         # Generate with real AI
#         posts = generate_ai_content(
#             data['business_profile'],
#             data.get('news_items', []),
#             data['preferences']
#         )
        
#         return jsonify({
#             'status': 'success',
#             'posts': posts,
#             'generated_at': datetime.utcnow().isoformat()
#         })
        
#     except Exception as e:
#         return jsonify({
#             'error': 'Content generation failed',
#             'details': str(e)
#         }), 500

@bp.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.get_json()
        
        # Required fields
        business_profile = data.get('business_profile')
        if not business_profile:
            return jsonify({
                'error': 'Business profile is required',
                'example': {
                    'business_profile': {
                        'name': 'Example Business',
                        'industry': 'fitness',
                        'services': ['Personal Training', 'Group Classes']
                    },
                    'preferences': {
                        'tone': 'friendly',
                        'post_type': 'tip'
                    }
                }
            }), 400
            
        # Optional fields with defaults
        news_items = data.get('news_items', [])
        preferences = data.get('preferences', {})
        
        posts = generate_posts(business_profile, news_items, preferences)
        
        return jsonify({
            'status': 'success',
            'count': len(posts),
            'posts': posts,
            'metadata': {
                'tone': preferences.get('tone', 'professional'),
                'type': preferences.get('post_type', 'tip')
            }
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to generate content',
            'details': str(e)
        }), 500

