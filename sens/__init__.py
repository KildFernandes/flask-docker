"""Initialize Flask app."""
from flask import Flask
from flask_bootstrap import Bootstrap  
from sens.config.config import DevConfig
 
def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    config = DevConfig()
    #SECRET_KEY = os.urandom(32)
    #app.config['SECRET_KEY'] = SECRET_KEY
    app.config.from_object(config)
    bootstrap = Bootstrap(app)
    
    with app.app_context():
        # Import parts of our application
        import sens.home.routes
        import sens.cadastro.routes

        app.register_blueprint(sens.home.routes.home_bp)
        app.register_blueprint(sens.cadastro.routes.cadastro_bp)

        return app