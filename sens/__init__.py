"""Initialize Flask app."""
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    """Create Flask application."""
    
    app = Flask(__name__, template_folder='templates')
    bootstrap = Bootstrap(app)
    #app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        import sens.home.routes
        import sens.cadastro.routes

        app.register_blueprint(sens.home.routes.home_bp)
        app.register_blueprint(sens.cadastro.routes.cadastro_bp)

        return app