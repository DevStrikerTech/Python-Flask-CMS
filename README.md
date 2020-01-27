# Python-Flask-CMS&#127798;
<p align="center">
  <b>--Dashboard--</b><br>
  <img src="https://raw.githubusercontent.com/KingCobra2018/Python-Flask-CMS/master/static/dashboard.png">
</p>
<p align="center">
  <b>--Index--</b><br>
  <img src="https://raw.githubusercontent.com/KingCobra2018/Python-Flask-CMS/master/static/index.png">
</p>
<p align="center">
  <b>--Register--</b><br>
  <img src="https://raw.githubusercontent.com/KingCobra2018/Python-Flask-CMS/master/static/register.png">
</p>

## Installation
=> Install latest version of Python3

=> Install pip 
```bash
pip install pipenv
```
=> Clone repository and open projet folder finally execute cmd from search panel 
```bash
pipenv shell
pipenv install flask
pipenv install flask-mysqldb
pipenv install flask-WTF
pipenv install passlib
```

## MySQL Setup
=> Execute following sql commands/statements to have required database
```sql
CREATE DATABASE myflaskapp;
USE myflaskapp;
CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, email VARCHAR(100), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
SHOW TABLES;
DESCRIBE users;
```

## Usage
=> From project folder open app.py and configure MySQL
```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
```
Note: Don't forget to change MySQL host, username, password and database name

TO-DO: Run app.py and copy localhost url to your web browser

## Documentation
http://flask.palletsprojects.com/en/1.1.x/

https://wtforms.readthedocs.io/en/stable/
