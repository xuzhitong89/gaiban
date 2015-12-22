#coding=utf-8
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import os
from db_models import app
from data_models import login_in
from functools import wraps
d = {}
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if'username'not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_in(username, password) == 1:
            session['username'] = username
            print session['username']
            flash('You were logged in')
            return redirect(url_for('index'))
        elif login_in(username, password) == 0:
            session['username'] = username
            flash('You were logged in')
            return redirect(url_for('index'))
        elif login_in(username, password) == -1:
            d['error'] = u"账号或密码错误"
            return render_template('login.html', error=d['error'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    print session
    return redirect(url_for('login'))

@app.route("/index", methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')