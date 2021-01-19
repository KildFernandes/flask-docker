"""Initialize Flask app."""
from flask import Flask
from flask_bootstrap import Bootstrap  
from flask_pymongo import pymongo

from sens.config.config import DevConfig

 
def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    config = DevConfig()
    app.config.from_object(config)
    bootstrap = Bootstrap(app)
    
    
    
    with app.app_context():
        #Import parts of our application
        import sens.home.routes
        import sens.cadastro.routes
        import sens.errorhandlers.erros

        app.register_blueprint(sens.home.routes.home_bp)
        app.register_blueprint(sens.cadastro.routes.cadastro_bp)
        app.register_blueprint(sens.errorhandlers.erros.errors_bp)

        return app