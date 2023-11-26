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

Sample Data:
```mysql
INSERT INTO customer (username, password, email, street, city, state, zipcode) VALUES
('s', 's', 'john.doe@email.com', '123 Oak St', 'Cityville', 'Stateville', 54321);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('sell', 's', 'email@email.com', 'street', 'city', 'state', 12345);

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link) VALUES (1, 'test', 'test', 1.99, 1, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');


```