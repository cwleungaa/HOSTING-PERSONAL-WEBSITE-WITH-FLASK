from flask import Flask, render_template, Blueprint

blueprint_cs50ai = Blueprint('cs50ai', __name__, url_prefix='/cs50ai')


@blueprint_cs50ai.route('/')
@blueprint_cs50ai.route('/index')
def index():
    return render_template('cs50ai.html')


@blueprint_cs50ai.route('/search')
def search():
    return render_template('search.html')


@blueprint_cs50ai.route('/knowledge')
def knowledge():
    return render_template('knowledge.html')


@blueprint_cs50ai.route('/uncertainty')
def uncertainty():
    return render_template('uncertainty.html')


@blueprint_cs50ai.route('/optimization')
def optimization():
    return render_template('optimization.html')


@blueprint_cs50ai.route('/learning')
def learning():
    return render_template('learning.html')


@blueprint_cs50ai.route('/neural_networks')
def neural_networks():
    return render_template('neural_networks.html')


@blueprint_cs50ai.route('/language')
def language():
    return render_template('language.html')

