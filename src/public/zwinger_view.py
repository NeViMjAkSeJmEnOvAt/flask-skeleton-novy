"""
Logic for dashboard related routes
"""

from flask import Blueprint, render_template
from .forms import LogUserForm, secti,masoform,fomrmularTest
from ..data.database import db
from ..data.models import LogUser
from .views import blueprint

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


@blueprint.route("/simple_chart")
def chart():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('public/graph_template.tmpl', values=values, labels=labels, legend=legend)

#@blueprint.route("/vloz_radek"):
#def vloz_radek():
#   text = "Bla BlaBla"
#  Stock