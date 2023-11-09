from flask import Flask, render_template, Blueprint

blueprint_cs50 = Blueprint('cs50', __name__, url_prefix='/cs50')


@blueprint_cs50.route('/')
@blueprint_cs50.route('/index')
def index():
    return render_template('cs50.html')


@blueprint_cs50.route('/c')
def c():
    return render_template('c.html')


@blueprint_cs50.route('/python')
def python():
    return render_template('python.html')


@blueprint_cs50.route('/sql')
def sql():
    return render_template('sql.html')


@blueprint_cs50.route('/games')
def games():
    return render_template('games.html')


@blueprint_cs50.route('/games/pong')
def pong():
    return render_template('pong.html')


@blueprint_cs50.route('/games/mario')
def mario():
    return render_template('mario.html')


@blueprint_cs50.route('/webmain')
def webmain():
    return render_template('webmain.html')


@blueprint_cs50.route('/webmain/web')
def web():
    return render_template('web.html')


@blueprint_cs50.route('/webmain/finance')
def finance():
    return render_template('finance.html')


@blueprint_cs50.route('/final_project')
def final_project():
    return render_template('final_project.html')
