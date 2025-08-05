from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates')  # Ensure double underscores
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    CORS(app)
    
    # Register blueprints
    from app.routes import main_routes, business_routes, content_routes, facebook_routes
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(business_routes.bp)
    app.register_blueprint(content_routes.bp)
    app.register_blueprint(facebook_routes.bp)
    
    return app  # <- Make sure this line is properly indented