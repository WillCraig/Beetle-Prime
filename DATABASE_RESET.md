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

-- Inserting test data into the Product table with random realistic data and food images

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Laptop', 'High-performance laptop with SSD', 899.99, 50, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Smartphone', 'Latest smartphone with dual camera', 699.99, 80, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Headphones', 'Noise-canceling headphones with Bluetooth', 149.99, 30, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Coffee Maker', 'Stainless steel coffee maker with timer', 79.99, 20, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Fitness Tracker', 'Waterproof fitness tracker with heart rate monitor', 49.99, 60, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Wireless Mouse', 'Ergonomic wireless mouse for comfortable use', 29.99, 40, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Backpack', 'Durable backpack with multiple compartments', 39.99, 25, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Gaming Keyboard', 'Mechanical gaming keyboard with RGB lighting', 89.99, 15, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Bluetooth Speaker', 'Portable Bluetooth speaker with long battery life', 59.99, 35, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'External Hard Drive', '1TB external hard drive for extra storage', 129.99, 10, 'https://cdn.vox-cdn.com/thumbor/Vu29oQjMk6yyUy9PmGNeWQqznHI=/39x94:1887x974/1200x800/filters:focal(934x381:1240x687)/cdn.vox-cdn.com/uploads/chorus_image/image/72845570/The_Legend_of_Zelda._Skyward_Sword_Screen_Shot_7_19_21__5.58_PM.0.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Princess Peach', 'Mario Game', 19.99, 2, 'https://mario.nintendo.com/static/6731ec87c8e4fe2ab7b191292f9df949/13fb2/peach-unstack-open.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Walulgi', 'Mario Game', 15.99, 3, 'https://mario.nintendo.com/static/d468a32c7ab971cce7b3e89ae48560a0/13fb2/waluigi-unstack-open.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Bowser', 'Mario Game', 18.99, 2, 'https://mario.nintendo.com/static/233682a28cdb7b3cc0232a81a0b6c4e7/13fb2/bowser-unstack-open.png');


```