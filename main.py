from flask import Flask
from app.routes import init_routes
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__,
                template_folder='app/templates',
                static_folder='app/static')
    
    # Configure app
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'app', 'uploads')
    
    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Initialize routes
    init_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=True, port=5000)