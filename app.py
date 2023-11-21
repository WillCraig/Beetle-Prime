import re, os
from modules.globals import app, db
from flask import Flask, redirect, render_template, request, url_for, session
from modules.schema import Customer, Seller, Product
@app.context_processor
def handle_context():
    return dict(os=os)


# Login page
@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        account = Customer.query.filter_by(username=username, password=password).first()
        # If Customer account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account.customer_id
            session['username'] = account.username
            session['usertype'] = "customer"
            # Redirect to home page
            return redirect(url_for('home'))
        
        account = Seller.query.filter_by(name=username, password=password).first()
        # If Seller account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account.seller_id
            session['username'] = account.name
            session['usertype'] = "seller"
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesn't exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)

# Logout Page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('usertype', None)
    # Redirect to login page
    return redirect(url_for('login'))

# Customer Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if (request.method == 'POST' and 'username' in request.form and 'password' in
            request.form and 'email' in request.form and 'street' in request.form and 'city' in request.form and 'state' in request.form and 'zipcode' in request.form):
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']

        account = Customer.query.filter_by(username=username).first()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not street or not city or not state or not zipcode:
            msg = 'Please fill out the form!'
        else:
            # account doesn't exist, add to db
            account = Customer(username=username, password=password, email=email, street=street, city=city, state = state, zipcode=zipcode)

            db.session.add(account)
            db.session.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# Seller Register
@app.route('/sellerregister', methods=['GET', 'POST'])
def sellerregister():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if (request.method == 'POST' and 'name' in request.form and 'password' in
            request.form and 'email' in request.form and 'street' in request.form and 'city' in request.form and 'state' in request.form and 'zipcode' in request.form):
        # Create variables for easy access
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']

        account = Seller.query.filter_by(name=name).first()

        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'Username must contain only characters and numbers!'
        elif not name or not password or not email or not street or not city or not state or not zipcode:
            msg = 'Please fill out the form!'
        else:
            # account doesn't exist, add to db
            account = Seller(name=name, password=password, email=email, street=street, city=city, state = state, zipcode=zipcode)

            db.session.add(account)
            db.session.commit()
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('sellerregister.html', msg=msg)

# Home page
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        if session['usertype'] == "customer":
            return render_template('home.html', username=session['username'])
        if session['usertype'] == "seller":
            results = Product.query.filter_by(seller_id=session['id']).all()
            return render_template('sellerhome.html', username=session['username'], data=results)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# profile Page
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        if session['usertype'] == "customer":
            account = Customer.query.filter_by(customer_id=session['id']).first()
            return render_template('profile.html', customer=account)

        elif session['usertype'] == "seller":
            account = Seller.query.filter_by(seller_id=session['id']).first()
            return render_template('profile.html', seller=account)
        

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# Search Products Page
@app.route('/searchproductform')
def searchproductform():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    elif 'usertype' == 'seller':
        return redirect(url_for('home'))
    else:
        return render_template('form.html', username=session['username'])
    
# Search Results Page
@app.route('/search', methods=['POST', 'GET'])
def search():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    if request.method == 'GET':
        return "Fill out the Search Form"

    if request.method == 'POST':
        msg = ''
        name = request.form['name']
        product_id = request.form['product_id']
        seller_id = request.form['seller_id']

        results = None

        if name:
            results = Product.query.filter_by(name=name).all()
        elif product_id:
            results = Product.query.filter_by(product_id=product_id).all()
        elif seller_id:
            results = Product.query.filter_by(seller_id=seller_id).all()
        
        data = results
        if not results:
            msg = 'No Results Found'

        for i in data:
            print(i)
        return render_template('results.html', data=data, msg=msg)

# Add Product Page
@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    elif 'usertype' == 'customer':
        return redirect(url_for('home'))
    else:
        msg = ''
        if (request.method == 'POST' and 'name' in request.form and 'description' in
            request.form and 'price' in request.form and 'quantity' in request.form):
            # Create variables for easy access
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            quantity = request.form['quantity']

            account = Product.query.filter_by(name=name).first()

            # If account exists show error and validation checks
            if account:
                msg = 'Product already exists!'
            elif not re.match(r'[A-Za-z0-9]+', name):
                msg = 'Product name must contain only characters and numbers!'
            elif not name or not description or not price or not quantity:
                msg = 'Please fill out the Product form!'
            else:
                # product doesn't exist, add to db
                product = Product(seller_id = session['id'], name=name, description=description, price=price, product_quantity=quantity)

                db.session.add(product)
                db.session.commit()
                msg = 'You have successfully added a Product!'

        elif request.method == 'POST':
            # Form is empty... (no POST data)
            msg = 'Please fill out the form!'
        # Show registration form with message (if any)
        return render_template('addproduct.html', msg=msg)






@app.route('/product_details/<p_id>', methods=['GET', 'POST'])
def product_details(p_id):
    product = Product.query.get(p_id)
    if product:
        return render_template('product_details.html', product=product)
    else:
        # Handle product not found, redirect to an error page, or return an error message.
        return render_template('home.html', username=session['username'])





if __name__ == '__main__':
    app.run(debug=True)
