import os
import re

from flask import redirect, render_template, request, url_for, session
from sqlalchemy import func

from modules.globals import app, db
from modules.schema import Customer, Seller, Product, Order, OrderProduct, Purchase, PurchaseProduct


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
            existing_order = Order.query.filter_by(customer_id=session['id']).first()

            if not existing_order:
                # If there's no existing order, create a new one
                new_order = Order(customer_id=session['id'])
                db.session.add(new_order)
                db.session.commit()

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
            request.form and 'email' in request.form and 'street' in request.form and 'city' in request.form
            and 'state' in request.form and 'zipcode' in request.form):
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
            account = Customer(username=username, password=password, email=email, street=street, city=city, state=state,
                               zipcode=zipcode)

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
            request.form and 'email' in request.form and 'street' in request.form and 'city' in request.form
            and 'state' in request.form and 'zipcode' in request.form):
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
            account = Seller(name=name, password=password, email=email, street=street, city=city, state=state,
                             zipcode=zipcode)

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
            # get 3 random products
            results = Product.query.filter(Product.product_quantity > 0).order_by(func.random()).limit(3).all()
            return render_template('home.html', username=session['username'], c_id=session['id'], data=results)
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
        # We need all the account info for the user, so we can display it on the profile page
        if session['usertype'] == "customer":
            account = Customer.query.filter_by(customer_id=session['id']).first()

            # purchases = PurchaseProduct.query.join(Purchase).filter_by(customer_id=session['id']).all()
            purchases = Purchase.query.filter_by(customer_id=session['id']).all()

            return render_template('profile.html', customer=account, purchases=purchases)

        elif session['usertype'] == "seller":
            account = Seller.query.filter_by(seller_id=session['id']).first()
            return render_template('profile.html', seller=account)

    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


# Search bar
@app.route('/searchbar', methods=['POST', 'GET'])
def searchbar():
    # Check if user is loggedin, return redirect to login page if not
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    if request.method == 'GET':
        return "Fill out the Search bar"
    if request.method == 'POST':
        msg = ''
        name = request.form['name']

        results = None

        # Search by Product Name
        if name:
            results = Product.query.filter_by(name=name).all()

        # Search by Seller Name
        if not results:
            results = Product.query.join(Seller).filter_by(name=name).all()

        data = results
        if not results:
            msg = 'No Results Found'

        for i in data:
            print(i)
        return render_template('results.html', data=data, msg=msg, name=name)


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

            product = Product.query.filter_by(name=name).first()

            # If product exists show error and validation checks
            if product:
                msg = 'Product already exists!'
            elif not re.match(r'[A-Za-z0-9]+', name):
                msg = 'Product name must contain only characters and numbers!'
            elif not name or not description or not price or not quantity:
                msg = 'Please fill out the Product form!'
            else:
                # product doesn't exist, add to db

                if 'img_link' in request.form:
                    img_link = request.form['img_link']
                    product = Product(seller_id=session['id'], name=name, description=description, price=price,
                                      product_quantity=quantity, img_link=img_link)
                else:
                    product = Product(seller_id=session['id'], name=name, description=description, price=price,
                                      product_quantity=quantity,
                                      img_link='https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3AIcon-round-Question_mark.jpg&psig=AOvVaw3salWVD2MijoBnckBIispR&ust=1701966534581000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCMD4gMid-4IDFQAAAAAdAAAAABAk')

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


@app.route('/product_updates/<p_id>', methods=['GET', 'POST'])
def product_updates(p_id):
    product = Product.query.get(p_id)
    if product:
        if 'loggedin' not in session:
            return redirect(url_for('login'))
        elif 'usertype' == 'customer':
            return redirect(url_for('home'))
        else:
            msg = ''
            if request.method == 'POST' and 'name' in request.form:
                name = request.form['name']
                if name != '':
                    item = Product.query.filter_by(name=name).first()

                    # If product exists show error and validation checks
                    if item:
                        msg = 'Product already Has That Name!'
                    elif not re.match(r'[A-Za-z0-9]+', name):
                        msg = 'Product name must contain only characters and numbers!'
                    else:
                        Product.query.filter_by(product_id=p_id).update({'name': name})
                        db.session.commit()
                        msg = 'You have successfully Updated Your Product!!'

            if request.method == 'POST' and 'description' in request.form:
                description = request.form['description']
                if description != '':
                    item = Product.query.filter_by(product_id=p_id, description=description).first()

                    # If product exists show error and validation checks
                    if item:
                        msg = 'Product already Has That Description!'
                    else:
                        Product.query.filter_by(product_id=p_id).update({'description': description})
                        db.session.commit()
                        msg = 'You have successfully Updated Your Product!!'

            if request.method == 'POST' and 'price' in request.form:
                price = request.form['price']
                if price != '':
                    item = Product.query.filter_by(product_id=p_id, price=price).first()

                    # If product exists show error and validation checks
                    if item:
                        msg = 'Product already Has That price!'
                    else:
                        Product.query.filter_by(product_id=p_id).update({'price': price})
                        db.session.commit()
                        msg = 'You have successfully Updated Your Product!!'

            if request.method == 'POST' and 'quantity' in request.form:
                quantity = request.form['quantity']
                if quantity != '':
                    item = Product.query.filter_by(product_id=p_id, product_quantity=quantity).first()

                    # If product exists show error and validation checks
                    if item:
                        msg = 'Product already Has That Quantity!'
                    else:
                        Product.query.filter_by(product_id=p_id).update({'product_quantity': quantity})
                        db.session.commit()
                        msg = 'You have successfully Updated Your Product!!'

            if request.method == 'POST' and 'img_link' in request.form:
                img_link = request.form['img_link']
                if img_link != '':
                    item = Product.query.filter_by(product_id=p_id, img_link=img_link).first()

                    # If product exists show error and validation checks
                    if item:
                        msg = 'Product already Has That Image!'
                    else:
                        Product.query.filter_by(product_id=p_id).update({'img_link': img_link})
                        db.session.commit()
                        msg = 'You have successfully Updated Your Product!!'

            return render_template('product_updates.html', product=product, msg=msg)
    else:
        # Handle product not found, redirect to an error page, or return an error message.
        return render_template('home.html', username=session['username'])


@app.route('/cart/<c_id>', methods=['GET', 'POST'])
def cart():
    order = Order.query.filter_by(customer_id=session['id']).first()

    if order:
        items = OrderProduct.query.filter_by(order_id=order.order_id).all()

        cart_items = OrderProduct.query.join(Product).all()
        ttl = 0

        for i in items:
            ttl += i.quantity * Product.query.get(i.product_id).price
            # temptable.append(i.quantity)
            # temptable.append(OrderProduct.query.get(i.product_id))
            # cart_items.append(Product.query.get(i.product_id))

        return render_template('cart.html', order=order, order_id=order.order_id, cart_items=cart_items, total=ttl)
    else:
        if session['usertype'] == "customer":
            results = Product.query.order_by(func.random()).limit(3).all()
            return render_template('home.html', username=session['username'], c_id=session['id'], data=results)
        elif session['usertype'] == "seller":
            results = Product.query.filter_by(seller_id=session['id']).all()
            return render_template('sellerhome.html', username=session['username'], data=results)


@app.route('/add_to_order/<int:product_id>', methods=['POST'])
def add_to_order(product_id):
    user_id = session['id']  # FIXME: make sure this is right.
    order = Order.query.filter_by(customer_id=user_id).first()

    if order:
        quantity = int(request.form.get('quantity', 1))
        OrderProduct.add_product_to_order(order_id=order.order_id, product_id=product_id, quantity=quantity)

    return redirect(url_for('home'))


@app.route('/remove_from_order/<int:product_id>', methods=['GET', 'POST'])
def remove_from_order(product_id):
    user_id = session['id']  # FIXME: make sure this is right.
    order = Order.query.filter_by(customer_id=user_id).first()

    if order:
        OrderProduct.query.filter_by(product_id=product_id).delete()
        db.session.commit()

    return redirect(url_for('cart', c_id=session['id']))


@app.route('/purchase/<ord_id>', methods=['GET', 'POST'])
def purchase(ord_id):
    order = Order.query.filter_by(order_id=ord_id).first()

    # ... (existing code)

    if order:
        # Retrieve all products associated with the order
        order_products = OrderProduct.query.filter_by(order_id=ord_id).all()

        # Create a new purchase
        new_purchase = Purchase(order=order)
        db.session.add(new_purchase)
        db.session.commit()

        # Create entries in PurchaseProducts for each product associated with the order
        for op in order_products:
            purchase_product = PurchaseProduct(purchase_id=new_purchase.purchase_id, product_id=op.product_id,
                                               quantity=op.quantity)
            # Update Product Quantity
            Product.query.filter_by(product_id=op.product_id).update(
                {'product_quantity': Product.product_quantity - op.quantity})
            db.session.add(purchase_product)

        db.session.commit()

        # Remove all items with associated order ID from order_products table
        OrderProduct.query.filter_by(order_id=ord_id).delete()
        db.session.delete(order)
        db.session.commit()

        # Redirect to the purchase details page
        return redirect(url_for('purchase_details', pur_id=new_purchase.purchase_id))
    else:
        return render_template('home.html', username=session['username'])


@app.route('/purchase_details/<pur_id>', methods=['GET', 'POST'])
def purchase_details(pur_id):
    purchase_existence = Purchase.query.get(pur_id)

    if purchase_existence:

        purchase_items = PurchaseProduct.query.filter_by(purchase_id=pur_id).all()
        # get list of products based on the purchase_id data from purchase_items
        products = PurchaseProduct.query.filter_by(purchase_id=pur_id).join(Product)

        total_price = 0

        # products = []
        for item in purchase_items:
            # product = Product.query.get(item.product_id)
            # products.append(product)
            total_price += Product.query.get(item.product_id).price * item.quantity

        return render_template('purchase_details.html', pur_id=pur_id, purchase=purchase, purchase_items=products,
                               purcahse_total_price=total_price)
    else:
        # Handle product not found, redirect to an error page, or return an error message.
        return render_template('home.html', username=session['username'])


@app.route('/all_products', methods=['GET'])
def all_products():
    products = Product.query.all()
    return render_template('all_products.html', all_products=products)


if __name__ == '__main__':
    app.run(debug=True)
