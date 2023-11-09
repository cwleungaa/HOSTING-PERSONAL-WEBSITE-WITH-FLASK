from flask import Flask, render_template

import cs50
import cs50ai
import math_section

app = Flask(__name__)

app.register_blueprint(cs50.blueprint_cs50)
app.register_blueprint(cs50ai.blueprint_cs50ai)
app.register_blueprint(math_section.blueprint_math)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/menu')
# def menu():
#     return render_template('menu.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')


# @app.route('/about_me2')
# def about_me2():
#     return render_template('about_me2.html')


# @app.route('/cs50')
# def cs50():
#     return render_template('cs50.html')


# @app.route('/c')
# def c():
#     return render_template('c.html')


# @app.route('/python')
# def python():
#     return render_template('python.html')


# @app.route('/sql')
# def sql():
#     return render_template('sql.html')
#
#
# @app.route('/games')
# def games():
#     return render_template('games.html')
#
#
# @app.route('/pong')
# def pong():
#     return render_template('pong.html')
#
#
# @app.route('/mario')
# def mario():
#     return render_template('mario.html')
#
#
# @app.route('/webmain')
# def webmain():
#     return render_template('webmain.html')
#
#
# @app.route('/web')
# def web():
#     return render_template('web.html')
#
#
# @app.route('/finance')
# def finance():
#     return render_template('finance.html')
#
#
# @app.route('/final_project')
# def final_project():
#     return render_template('final_project.html')


# @app.route('/cs50ai')
# def cs50ai():
#     return render_template('cs50ai.html')
#
#
# @app.route('/search')
# def search():
#     return render_template('search.html')
#
#
# @app.route('/knowledge')
# def knowledge():
#     return render_template('knowledge.html')
#
#
# @app.route('/uncertainty')
# def uncertainty():
#     return render_template('uncertainty.html')
#
#
# @app.route('/optimization')
# def optimization():
#     return render_template('optimization.html')
#
#
# @app.route('/learning')
# def learning():
#     return render_template('learning.html')
#
#
# @app.route('/neural_networks')
# def neural_networks():
#     return render_template('neural_networks.html')
#
#
# @app.route('/language')
# def language():
#     return render_template('language.html')


# @app.route('/math101')
# def math101():
#     return render_template('math_mainpage.html')
#
#
# @app.route('/calculus')
# def calculus():
#     return render_template('calculus.html')
#
#
# @app.route('/analysis')
# def analysis():
#     return render_template('analysis.html')
#
#
# @app.route('/real_analysis')
# def real_analysis():
#     return render_template('real_analysis.html')
#
#
# @app.route('/complex_analysis')
# def complex_analysis():
#     return render_template('complex_analysis.html')
#
#
# @app.route('/algebra')
# def algebra():
#     return render_template('algebra.html')
#
#
# @app.route('/number_theory')
# def number_theory():
#     return render_template('number_theory.html')
#
#
# @app.route('/geometry')
# def geometry():
#     return render_template('geometry.html')


@app.route('/financial_analysis')
def financial_analysis():
    return render_template('financial_analysis.html')


# @app.route('/financial_analysis2')
# def financial_analysis2():
#     return render_template('financial_analysis2.html')


@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True, port=5000)


