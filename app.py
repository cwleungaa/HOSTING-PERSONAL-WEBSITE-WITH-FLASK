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


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/about_me')
def about_me():
    return render_template('about_me.html')


@app.route('/financial_analysis')
def financial_analysis():
    return render_template('financial_analysis.html')


@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')


if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True, port=5000)


