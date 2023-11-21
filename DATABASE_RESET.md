# Delete and Recreate the Database
open the mysql shell
```mysql
DROP DATABASE testDB;
CREATE DATABASE testDB;
```


Open the flask interactive shell with `flask shell`
```shell
from app import db
db.create_all()
```

Shell is now reset