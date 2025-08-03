import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('FLASK_ENV') == 'development'
    
    # Facebook API mock credentials
    FB_APP_ID = 'mock_app_id_123'
    FB_APP_SECRET = 'mock_app_secret_456'