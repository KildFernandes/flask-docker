from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask import make_response

# Blueprint Configuration
errors_bp = Blueprint(
    'errors_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@errors_bp.app_errorhandler(404)
def not_found(e):
    """Page not found."""
    return make_response(render_template("404.html"),404)


