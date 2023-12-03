# test customer
INSERT INTO customer (username, password, email, street, city, state, zipcode) VALUES
('s', 's', 'john.doe@email.com', '123 Oak St', 'Cityville', 'Stateville', 54321);


# SELLER
INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Beedle', 's', 'email@email.com', 'street', 'city', 'state', 12345);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Link', 's', 'email@email.com', 'street', 'city', 'state', 12345);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Mario', 's', 'email@email.com', 'street', 'city', 'state', 12345);


# PRODUCT
# Beedle
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Heart Potion', 'Heals 8 hearts when consumed', 19.99, 1, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/0/07/SS_Heart_Potion_Model.png/revision/latest/scale-to-width-down/183?cb=20210815143730&format=original');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Bundle of Arrows', 'A bundle of 10 arrows', 7.99, 10, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/9/97/OoT3D_Bundle_of_Arrows_Model_2.png/revision/latest?cb=20200902122040&format=original');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Quiver', 'Increases the amount of arrows you can carry', 39.99, 1, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/2/24/TWWHD_Quiver_Upgrade_1_Artwork.png/revision/latest/scale-to-width-down/320?cb=20130911215147&format=original');

# Link
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Hookshot', 'Can be shot and pull you at high speeds', 149.99, 1, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/f/f8/TWWHD_Hookshot_Artwork.png/revision/latest/scale-to-width-down/312?cb=20130911220003&format=original');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Bow', 'Can be used to shoot arrows', 74.99, 1, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/b/bb/TWWHD_Hero%27s_Bow_Artwork.png/revision/latest/scale-to-width-down/320?cb=20130914155019&format=original');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Fairy in a Bottle', 'The fairy will heal you and save you from dying', 99.99, 1, 'https://static.wikia.nocookie.net/zelda_gamepedia_en/images/6/67/SSHD_Fairy_Render.png/revision/latest/scale-to-width-down/178?cb=20220308175755&format=original');

# Mario
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Mushroom', 'Increases your size, strength, and life', 14.99, 1, 'https://static.wikia.nocookie.net/nintendo/images/5/5b/Mushroom1.jpg/revision/latest?cb=20111104224030&path-prefix=en');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Fire Flower', 'Increases size, strength, and life aswell as providing a fireball', 29.99, 1, 'https://static.wikia.nocookie.net/nintendo/images/5/55/MK8_Fire_Flower.png/revision/latest/scale-to-width-down/1000?cb=20170206125257&path-prefix=en');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Starman', 'Grants you temporary invincibility', 49.99, 1, 'https://static.wikia.nocookie.net/nintendo/images/2/2e/Star.png/revision/latest?cb=20150501195537&path-prefix=en');
