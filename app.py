import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialise MySQL
mysql = MySQL(app)

# Route for home.html served as index page
# Provides user login capabilities
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form fields
        email = request.form['email']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by email
        result = cur.execute("SELECT * FROM users WHERE email = %s", [email])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare password
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['email'] = email
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('home.html', error=error)
            # Close Connection
            cur.close()
        else:
            error = 'Email is not registered'
            return render_template('home.html', error=error)

    return render_template('home.html')

# Register Form using WTForms RegisterForm Class
class RegisterForm(Form):
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Regexp('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', message="Enter valid email address")
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Route for register.html
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Create Cursor
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("INSERT INTO users(email, password) VALUES(%s, %s)", (email, password))
        # Commit to DB
        mysql.connection.commit()
        # Close Connection
        cur.close

        flash('you are now register and can now log in', 'success')

        return redirect(url_for('home'))
    return render_template('register.html', form=form)

# Route to dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
