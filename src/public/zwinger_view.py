"""
Logic for dashboard related routes
"""

from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform,fomrmularTest
from ..data.database import db
from ..data.models import LogUser
blueprint = Blueprint('public', __name__)

# ----------------------------------------------------------------------------------------------------------------------
from views import blueprint
@blueprint.route('/vypis_ales',methods=['GET'])
def Vypis_ales():
    pole=[[0,1],[2,3]]
    pole[0][1]=[0][1]+1
    return render_template("public/vypis_ales.tmpl",data = pole)
# ----------------------------------------------------------------------------------------------------------------------
@blueprint.route('/formularTest',methods=['GET','POST'])
def formularTestZwinger():
    form=fomrmularTest()
    if form.is_submitted():
        return form.a.data * form.b.data
    return render_template("public/formuarZwingerTest.tmpl",form=form)