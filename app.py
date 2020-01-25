from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Route for home.html served as index page
@app.route('/')
def home():
    return render_template('home.html')

# Register form using WTForms
class RegisterForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Route for Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

if __name__ == '__main__':
    app.run()
