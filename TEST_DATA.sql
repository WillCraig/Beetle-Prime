# test customer
INSERT INTO customer (username, password, email, street, city, state, zipcode) VALUES
('s', 's', 'john.doe@email.com', '123 Oak St', 'Cityville', 'Stateville', 54321);



# SELLER
INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('John-Moneybags', 's', 'email@email.com', 'street', 'city', 'state', 12345);
# TODO... make more seller accounts.


# PRODUCT
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Princess Peach', 'Mario Game', 19.99, 2, 'https://mario.nintendo.com/static/6731ec87c8e4fe2ab7b191292f9df949/13fb2/peach-unstack-open.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Walulgi', 'Mario Game', 15.99, 3, 'https://mario.nintendo.com/static/d468a32c7ab971cce7b3e89ae48560a0/13fb2/waluigi-unstack-open.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Bowser', 'Mario Game', 18.99, 2, 'https://mario.nintendo.com/static/233682a28cdb7b3cc0232a81a0b6c4e7/13fb2/bowser-unstack-open.png');
# TODO... make more products
