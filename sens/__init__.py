"""Initialize Flask app."""
from flask import Flask
from flask_bootstrap import Bootstrap
import os

def create_app():
    """Create Flask application."""
    
    app = Flask(__name__, template_folder='templates')
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    bootstrap = Bootstrap(app)
    #app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        import sens.home.routes
        import sens.cadastro.routes

        app.register_blueprint(sens.home.routes.home_bp)
        app.register_blueprint(sens.cadastro.routes.cadastro_bp)

        return app