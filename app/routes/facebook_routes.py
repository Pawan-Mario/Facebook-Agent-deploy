from flask import Blueprint, request, jsonify
from app.services.facebook_service import connect_facebook_page, publish_post

bp = Blueprint('facebook', __name__, url_prefix='/api')

@bp.route('/connect-facebook', methods=['POST'])
def connect_facebook():
    data = request.get_json()
    page_id = data.get('page_id')
    result = connect_facebook_page(page_id)
    return jsonify(result)

@bp.route('/publish-post', methods=['POST'])
def publish_to_facebook():
    data = request.get_json()
    result = publish_post(
        data.get('post_content'),
        data.get('page_id'),
        data.get('schedule_time')
    )
    return jsonify(result)