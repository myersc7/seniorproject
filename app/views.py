from flask import render_template, request, flash, redirect, url_for
from app import app, db
from app.models import User


@app.route('/')
def index():
    user = User.query.all()
    return render_template('index.html', user=user)

@app.route(/adduser, methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        user = User(request.form['email'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('New user was successfully added')
    return render_template('add.html')
