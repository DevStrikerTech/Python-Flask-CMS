# Python-Flask-CMS
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
Install latest version of Python3

Install pip 
```bash
pip install pipenv
```
Clone repository and open projet folder finally execute cmd from search panel 
```bash
pipenv shell
pipenv install flask
pipenv install flask-mysqldb
pipenv install flask-WTF
pipenv install passlib
```
Run app.py

## MySQL Setup
```sql
CREATE DATABASE myflaskapp;
USE myflaskapp;
CREATE TABLE users(id INT(11));
```

## Documentation
http://flask.palletsprojects.com/en/1.1.x/

https://wtforms.readthedocs.io/en/stable/
