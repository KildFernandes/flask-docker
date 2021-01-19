from flask import Blueprint, request, render_template, make_response
from flask import current_app as app
from flask import request
from flask import url_for
from flask_pymongo import PyMongo
from sens.cadastro.form import CadastroForm
import logging

# Blueprint Configuration
cadastro_bp = Blueprint(
    'cadastro_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

mongo = PyMongo(app)

@cadastro_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        doc = mongo.db.Usuario.insert({'name':name, 'email':email})
        logging.warning('foi!')
        return 'insert'
            
    return render_template('cadastro.html',form=form)
