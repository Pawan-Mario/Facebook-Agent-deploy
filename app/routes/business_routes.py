from flask import Blueprint, request, jsonify
from app.services.scraper_service import scrape_business_profile
from app.models.business_model import BusinessProfile

bp = Blueprint('business', __name__, url_prefix='/api')

@bp.route('/business-profile', methods=['POST'])
def get_business_profile():
    data = request.get_json()
    website_url = data.get('website_url')
    
    if not website_url:
        return jsonify({'error': 'Website URL is required'}), 400
    
    try:
        profile_data = scrape_business_profile(website_url)
        business_profile = BusinessProfile(**profile_data)
        return jsonify(business_profile.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500