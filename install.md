


Create local mysql database with a database titled "hostDB"

Install python packages:
```shell
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install mysql-connector-python
pip3 install python-dotenv
```

Set up the tables (in the same directory as app.py) one-time to create the tables:
```shell
flask shell #(enter interactive shell)
from app import db
db.create_all()

#(exit interactive shell)
exit()
```


Create a file in the same directory as app.py ".env" no name just the .env extension
add the following to the .env file:
```
SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://root:@localhost/testDB
APP_SECRETKEY=secret
```



## Insert Data Example: 
```python3
username = request.form['username']
password = request.form['password']
email = request.form['email']
street = request.form['street']
city = request.form['city']
zipcode = request.form['zipcode']

        
account = Customer(username=username, password=password, email=email, street=street, city=city, zipcode=zipcode)
db.session.add(account)
db.session.commit()
```


## SELECT Data Example: 
```python3
account = Customer.query.filter_by(username=username).first()
```