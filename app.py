from flask import Flask, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config["DEBUG"] = True

app.secret_key = 'annoying'

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="",
    hostname="localhost",
    databasename="testDB",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']


        account = Account.query.filter_by(username=username, password=password).first()

        #
        # # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # # Fetch one record and return result
        # account = cursor.fetchone()

        print(account)


        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            # session['id'] = account['id']
            # session['username'] = account['username']
            session['id'] = account.id
            session['username'] = account.username
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

    # http://localhost:5000/python/logout - this will be the logout page


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if account exists using MySQL
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        # account = cursor.fetchone()
        account = Account.query.filter_by(username=username).first()



        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:

            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            # cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            # mysql.connection.commit()

            account = Account(username=username, password=password, email=email)
            db.session.add(account)
            db.session.commit()
            msg = 'You have successfully registered!'


    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# http://localhost:5000/pythinlogin/profile - this will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:


        # We need all the account info for the user so we can display it on the profile page
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        # account = cursor.fetchone()

        account = Account.query.filter_by(id=session['id']).first()


        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/searchform')
def searchform():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('form.html', username=session['username'])


@app.route('/search', methods=['POST', 'GET'])
def search():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return "Fill out the Search Form"

    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']

        # cursor = mysql.connection.cursor()
        if name:
            results = Instructor.query.filter_by(name=name).all()
            # cursor.execute("SELECT * from instructor where name = %s", [name])
        if id:
            results = Instructor.query.filter_by(id=id).all()
            # cursor.execute("SELECT * from instructor where ID = %s", [id])
        # mysql.connection.commit()
        # data = cursor.fetchall()
        # cursor.close()

        data = results

        for i in data:
            print(i)
        # return f"Done!! Query Result is {data}"
        return render_template('results.html', data=data)


# run the application
app.run(host='localhost', port=5000)
