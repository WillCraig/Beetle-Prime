# test customer
INSERT INTO customer (username, password, email, street, city, state, zipcode) VALUES
('John Doe', 's', 'john.doe@email.com', '123 Oak St', 'Cityville', 'Stateville', 54321);


# SELLER
INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Beedle', 's', 'beedle@email.com', 'Hyrule Castle Town Rd', 'Hyrule Castle Town', 'Central Hyrule', 12300);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Link', 's', 'Link@email.com', 'Hateno Rd', 'Hateno Village', 'East Neculda', 24341);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Mario', 's', 'Mario@email.com', 'Mushroom Kingdom Drive', 'Broklyn', 'New York', 12345);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('Anime', 's', 'Anime@email.com', 'Anime World', 'Kent', 'Ohio', 12345);

INSERT INTO seller (name, password, email, street, city, state, zipcode) VALUES ('NFT', 's', 'nft@email.com', 'NFT str', 'Kent', 'Ohio', 12345);


# PRODUCT
# Beedle
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'GreenLand', 'Literary Greenland', 500000.00, 1, 'https://www.climate.gov/sites/default/files/styles/full_width_620_alternate_image/public/MODISalbedo_greenland2011_610.jpg?itok=l0K2ADs9');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Arrows', 'Use These Handy Things With a Bow', 1.00, 200, 'https://cdn1.iconfinder.com/data/icons/arrows-409/64/Arrow_Up_Arrow-12-512.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Rugged Rhino Beetle', 'My Precious', 79999.99, 1, 'https://cdn.wikimg.net/en/zeldawiki/images/a/a0/TotK_Rugged_Rhino_Beetle_Model.png');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (1, 'Sony Walkman', 'The Mp3 player Before it was cool', 69.99, 126, 'https://images.reverb.com/image/upload/s--UHPwFyIy--/a_0/f_auto,t_large/v1672033355/lifevpkokxxlamllyne5.jpg');


# Link
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Jar of Dirt', 'This Jar will Capture your Heart', 47.25, 58, 'https://i.kym-cdn.com/entries/icons/facebook/000/002/914/jar-of-dirt.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Havoc in Hyrule', 'Vintage Legend of Zelda DVD.', 20.99, 30, 'https://m.media-amazon.com/images/I/51TKYxnXFYL._AC_UF894,1000_QL80_.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (2, 'Fanny Pack', 'A tool Belt for your needs', 12.50, 89, 'https://chromeindustries.com/cdn/shop/products/1_BG-288-BK.jpg?v=1701459692&width=2048');

# Mario
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Super Mario bros. Movie', 'The Orignal 1993 Movie now on DVD', 20.00, 50, 'https://upload.wikimedia.org/wikipedia/en/thumb/9/94/SMB_Movie_Poster.jpg/220px-SMB_Movie_Poster.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Mario Cap', 'From it\'s a Me! Please Ingnore the Eyes', 199.99, 4, 'https://m.media-amazon.com/images/I/8127FzX1QxS._AC_UY1000_.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Pac-Man Lunch Box', 'Vintage Pac-man themed Lunch box.', 9.99, 23, 'https://i.ebayimg.com/images/g/E~gAAOSw6jdjdnoa/s-l1600.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Shaq Fu!', 'Easily the greatest game of All time', 102.34, 11, 'https://i.ebayimg.com/images/g/KYQAAMXQya1Q5ySQ/s-l600.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (3, 'Garfield Plush', 'Chris Pratt in marketible Plushie Form', 300.15, 7, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfDHspOS6n6xlDIWlBqLu4JTyDKC_T_765-A&usqp=CAU'); 

# Anime
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (4, 'Charizard VSTART', 'Pokemon Card Secret Rare', 87.81, 20, 'https://m.media-amazon.com/images/I/610EPTmOT5L._AC_.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (4, 'Arceus VMAX', 'Golden Pokemon Gifts For Kids', 8.99, 10, 'https://i.ebayimg.com/images/g/4HMAAOSwSx9kRKlW/s-l1600.jpg');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (4, 'Naruto Keychain', 'Naruto Uzumaki With Ramen Bowl', 10.98, 15, 'https://target.scene7.com/is/image/Target/GUEST_aba351e8-c054-400c-80a1-a5ca588ebfe2?wid=1200&hei=1200&qlt=80&fmt=webp');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (4, 'Nezuko Kamado', 'Demon Slayer: Bandai Spirits Souvenir', 18.99, 10, 'https://m.media-amazon.com/images/I/51ZrvX4QTwL._AC_SX679_.jpg');

# NFT
INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (5, 'NFT', 'Steady Stack Legends #151', 1150.20, 8, 'https://i.seadn.io/gcs/files/3a0c198554385093613bd2f8abb289c8.gif?w=500&auto=format');

INSERT INTO product (seller_id, name, description, price, product_quantity, img_link)
VALUES (5, 'NFT', 'Steady Stack Legends #133', 5500, 8, 'https://i.seadn.io/s/raw/files/40d21cb3b1e16df54e284a39fe25c030.gif?auto=format&dpr=1&w=1000');