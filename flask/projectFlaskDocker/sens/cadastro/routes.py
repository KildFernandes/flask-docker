from flask import Blueprint
from flask import current_app as app
from flask import render_template

# Blueprint Configuration
cadastro_bp = Blueprint(
    'cadastro_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@cadastro_bp.route('/cadastro', methods=['GET'])
def cadastro():
    return render_template('cadastro.html')