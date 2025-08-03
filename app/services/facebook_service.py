import time
from random import randint

def connect_facebook_page(page_id):
    # Simulate Facebook connection
    if not page_id:
        return {
            'status': 'error',
            'message': 'Page ID is required'
        }
    
    return {
        'status': 'success',
        'message': 'Page connected successfully',
        'token': f"fb_mock_token_{randint(1000, 9999)}",
        'page_id': page_id
    }

def publish_post(post_content, page_id, schedule_time=None):
    # Simulate Facebook post
    if not post_content:
        return {
            'status': 'error',
            'message': 'Post content is required'
        }
    
    return {
        'status': 'success',
        'message': 'Post published successfully',
        'post_url': f"https://facebook.com/{page_id}/posts/mock_{int(time.time())}",
        'content': post_content,
        'published_at': schedule_time or 'immediately'
    }