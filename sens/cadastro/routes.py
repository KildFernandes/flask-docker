from flask import Blueprint
from flask import current_app as app
from flask import render_template
from .form import CadastroForm 

# Blueprint Configuration
cadastro_bp = Blueprint(
    'cadastro_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@cadastro_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('cadastro.html',form=form)