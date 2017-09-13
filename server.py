from flask import Flask, render_template, redirect, request, url_for, flash, Markup
from keys import CONF
import common

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/mentors', methods=['GET'])
def mentors():
    table = common.show_mentors()
    return render_template('table.html', table=table, keys=CONF["q1_2_keys"])


@app.route('/all-school', methods=['GET'])
def all_sch():
    table = common.all_school()
    return render_template('table.html', table=table, keys=CONF["q1_2_keys"])


@app.route('/mentors-by-country', methods=['GET'])
def ment_by_country():
    table = common.mentors_by_country()
    return render_template('table.html', table=table, keys=CONF["q3_keys"])


@app.route('/contacts', methods=['GET'])
def contacts():
    table = common.contacts()
    return render_template('table.html', table=table, keys=CONF["q4_keys"])


@app.route('/applicants', methods=['GET'])
def applicants():
    table = common.applicants()
    return render_template('table.html', table=table, keys=CONF["q5_keys"])


if __name__ == "__main__":
    app.secret_key = 'magic'
    app.run(debug=True, port=5000)