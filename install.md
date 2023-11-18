create mysql database with a database titled "hostDB"

install python packages:
```shell
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install mysql-connector-python
pip3 install python-dotenv
```

```shell
flask shell #(enter interactive shell)
from app import db
db.create_all()

#(exit interactive shell)
exit()
```


create a file in the same directory as app.py ".env" no name just the .env extension
add the following to the .env file:
```
USERNAME=root
PASSWORD=w
HOSTNAME=localhost
DATABASENAME=testDB
```