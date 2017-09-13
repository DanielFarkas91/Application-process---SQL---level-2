from flask import Flask, render_template, redirect, request, url_for, flash, Markup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')


@app.route('/mentors', methods=['GET'])
def show_mentors():
    return render_template('table.html')


@app.route('/all-school', methods=['GET'])
def show_all_school():
    pass
    return render_template('table.html')


if __name__ == "__main__":
    app.secret_key = 'magic'
    app.run(debug=True, port=5000)