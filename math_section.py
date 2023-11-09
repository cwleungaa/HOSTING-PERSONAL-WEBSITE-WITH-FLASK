from flask import Flask, render_template, Blueprint

blueprint_math = Blueprint('mathematics', __name__, url_prefix='/mathematics')


@blueprint_math.route('/')
@blueprint_math.route('/index')
def index():
    return render_template('math_mainpage.html')


@blueprint_math.route('/calculus')
def calculus():
    return render_template('calculus.html')


@blueprint_math.route('/analysis')
def analysis():
    return render_template('analysis.html')


@blueprint_math.route('/analysis/real_analysis')
def real_analysis():
    return render_template('real_analysis.html')


@blueprint_math.route('/analysis/complex_analysis')
def complex_analysis():
    return render_template('complex_analysis.html')


@blueprint_math.route('/algebra')
def algebra():
    return render_template('algebra.html')


@blueprint_math.route('/number_theory')
def number_theory():
    return render_template('number_theory.html')


@blueprint_math.route('/geometry')
def geometry():
    return render_template('geometry.html')

