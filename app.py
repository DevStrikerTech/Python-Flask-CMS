from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, PasswordField, validators
from wtforms.fields.html5 import EmailField
from passlib.hash import sha256_crypt

app = Flask(__name__)

# Route for home.html served as index page
@app.route('/')
def home():
    return render_template('home.html')

# Register form using WTForms(RegisterForm Class)
class RegisterForm(Form):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Route for Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
