from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/', methods=['GET'])
def home():
        return render_template('home.html')