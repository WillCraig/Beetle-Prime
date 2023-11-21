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
INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('john_doe', 'pass123', 'john.doe@email.com', '123 Oak St', 'Cityville', 'Stateville', 54321);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('jane_smith', 'password456', 'jane.smith@email.com', '456 Maple St', 'Townsville', 'Stateland', 12345);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('mike_jones', 'securepass', 'mike.jones@email.com', '789 Birch St', 'Villagetown', 'Countryland', 67890);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('sara_miller', 'myp@ssword', 'sara.miller@email.com', '101 Pine St', 'Metropolis', 'Provinceville', 98765);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('david_white', 'davidpass', 'david.white@email.com', '202 Cedar St', 'Hamletsville', 'Territoryland', 13579);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('emily_brown', 'browneyes', 'emily.brown@email.com', '303 Redwood St', 'Cityburg', 'Districtland', 24680);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('ryan_clark', 'ryan123', 'ryan.clark@email.com', '404 Walnut St', 'Villagetropolis', 'Regionville', 87654);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('olivia_green', 'greenpass', 'olivia.green@email.com', '505 Elm St', 'Townsburg', 'Sectorland', 11223);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('alex_turner', 'turnerpass', 'alex.turner@email.com', '606 Sycamore St', 'Citytown', 'Zoneland', 33445);

INSERT INTO Customer (username, password, email, street, city, state, zipcode) VALUES
('emma_hall', 'hallpass', 'emma.hall@email.com', '707 Poplar St', 'Villagesburg', 'Precinctville', 55667);
```