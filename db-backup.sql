-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: wcraig4.mysql.pythonanywhere-services.com    Database: wcraig4$BPLive
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipcode` int NOT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'John Doe','s','john.doe@email.com','123 Oak St','Cityville','Stateville',54321),(2,'Tram','tr','tr@gmail.com','123','Kent','Ohio',44240),(3,'neko','n','neko@gmail.com','str','kent','ohio',44240),(4,'b','b','b@b.com','b','b','b',0),(5,'lsimps14','iDltSUfRs','lsimps14@kent.edu','123 Orange Dr.','Fruitopia','Ohio',11111),(6,'LaneMMII','a','lanesimpson14@gmail.com','123 Orange Dr.','Fruitopia','Ohio',11111),(7,'Brady','bbdboyz','brady@gmail.com','123 summit street','kent ','Ohio',44240);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES (5,4,'2023-12-06 20:15:14'),(10,6,'2023-12-07 15:53:21'),(11,1,'2023-12-07 15:53:21'),(13,7,'2023-12-07 15:53:21');
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_product`
--

DROP TABLE IF EXISTS `order_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_product_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`),
  CONSTRAINT `order_product_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_product`
--

LOCK TABLES `order_product` WRITE;
/*!40000 ALTER TABLE `order_product` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `seller_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  `product_quantity` int NOT NULL,
  `img_link` varchar(255) NOT NULL,
  PRIMARY KEY (`product_id`),
  KEY `seller_id` (`seller_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`seller_id`) REFERENCES `seller` (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,'GreenLand','Literary Greenland',500000.00,1,'https://www.climate.gov/sites/default/files/styles/full_width_620_alternate_image/public/MODISalbedo_greenland2011_610.jpg?itok=l0K2ADs9'),(2,1,'Arrows','Use These Handy Things With a Bow',1.00,196,'https://cdn1.iconfinder.com/data/icons/arrows-409/64/Arrow_Up_Arrow-12-512.png'),(3,1,'Rugged Rhino Beetle','My Precious',79999.99,1,'https://cdn.wikimg.net/en/zeldawiki/images/a/a0/TotK_Rugged_Rhino_Beetle_Model.png'),(4,1,'Sony Walkman','The Mp3 player Before it was cool',69.99,119,'https://images.reverb.com/image/upload/s--UHPwFyIy--/a_0/f_auto,t_large/v1672033355/lifevpkokxxlamllyne5.jpg'),(5,2,'Jar of Dirt','This Jar will Capture your Heart',47.25,58,'https://i.kym-cdn.com/entries/icons/facebook/000/002/914/jar-of-dirt.jpg'),(6,2,'Havoc in Hyrule','Vintage Legend of Zelda DVD.',20.99,30,'https://m.media-amazon.com/images/I/51TKYxnXFYL._AC_UF894,1000_QL80_.jpg'),(7,2,'Fanny Pack','A tool Belt for your needs',12.50,86,'https://chromeindustries.com/cdn/shop/products/1_BG-288-BK.jpg?v=1701459692&width=2048'),(8,3,'Super Mario bros. Movie','The Orignal 1993 Movie now on DVD',20.00,43,'https://upload.wikimedia.org/wikipedia/en/thumb/9/94/SMB_Movie_Poster.jpg/220px-SMB_Movie_Poster.jpg'),(9,3,'Mario Cap','From it\'s a Me! Please Ingnore the Eyes',199.99,4,'https://m.media-amazon.com/images/I/8127FzX1QxS._AC_UY1000_.jpg'),(10,3,'Pac-Man Lunch Box','Vintage Pac-man themed Lunch box.',9.99,23,'https://i.ebayimg.com/images/g/E~gAAOSw6jdjdnoa/s-l1600.jpg'),(11,3,'Shaq Fu!','Easily the greatest game of All time',102.34,11,'https://i.ebayimg.com/images/g/KYQAAMXQya1Q5ySQ/s-l600.jpg'),(12,3,'Garfield Plush','Chris Pratt in marketible Plushie Form',300.15,6,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfDHspOS6n6xlDIWlBqLu4JTyDKC_T_765-A&usqp=CAU'),(13,4,'Charizard VSTART','Pokemon Card Secret Rare',87.81,20,'https://m.media-amazon.com/images/I/610EPTmOT5L._AC_.jpg'),(14,4,'Arceus VMAX','Golden Pokemon Gifts For Kids',8.99,7,'https://i.ebayimg.com/images/g/4HMAAOSwSx9kRKlW/s-l1600.jpg'),(15,4,'Naruto Keychain','Naruto Uzumaki With Ramen Bowl',10.98,14,'https://target.scene7.com/is/image/Target/GUEST_aba351e8-c054-400c-80a1-a5ca588ebfe2?wid=1200&hei=1200&qlt=80&fmt=webp'),(16,4,'Nezuko Kamado','Demon Slayer: Bandai Spirits Souvenir',18.99,10,'https://m.media-amazon.com/images/I/51ZrvX4QTwL._AC_SX679_.jpg'),(17,5,'NFT','Steady Stack Legends #151',1150.20,8,'https://i.seadn.io/gcs/files/3a0c198554385093613bd2f8abb289c8.gif?w=500&auto=format'),(18,5,'NFT','Steady Stack Legends #133',5500.00,8,'https://i.seadn.io/s/raw/files/40d21cb3b1e16df54e284a39fe25c030.gif?auto=format&dpr=1&w=1000'),(19,4,'Wallet','Jujutsu Kaisen Year One Class',40.99,4,'https://m.media-amazon.com/images/I/71YYA+GelML._AC_SX679_.jpg'),(20,6,'test2','this is an updated test',11.99,3,'https://imgs.search.brave.com/BXqVlGT6ZcxrL7cUnYyjTy6eR7Qzbk2iriVVV22JjKE/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuZnJlZWltYWdl/cy5jb20vaW1hZ2Vz/L2xhcmdlLXByZXZp/ZXdzLzEzNC90ZXN0/LW1lLTE0MjAxNTku/anBnP2ZtdD13ZWJw/Jnc9MzUw'),(21,1,'Suprise','A Mystery gift',5.00,20,'https://qph.cf2.quoracdn.net/main-qimg-654617264f9192ec976abe6e53356240-lq'),(22,6,'test3','this is test 3',1.99,1,'https://qph.cf2.quoracdn.net/main-qimg-654617264f9192ec976abe6e53356240-lq'),(23,6,'updated product','update',20.99,5,'https://qph.cf2.quoracdn.net/main-qimg-654617264f9192ec976abe6e53356240-lq'),(24,8,'Kent State University','It\'s for sale',999999.99,0,'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBUVFBcUFRUYGBcXGhoZGRcZGxoaGhgaGhkcGhoaGhkaICwjICApHRoZJTUkKC0vMjIyGSI4PTgxPCwxMi8BCwsLDw4PHRERHTMpIig0MTIxMzEzMTExMTExMTEzMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMf/AABEIAI4BYwMBIgACEQEDEQH/');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase`
--

DROP TABLE IF EXISTS `purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase` (
  `purchase_id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `order_date` datetime NOT NULL,
  `purchase_date` datetime NOT NULL,
  PRIMARY KEY (`purchase_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase`
--

LOCK TABLES `purchase` WRITE;
/*!40000 ALTER TABLE `purchase` DISABLE KEYS */;
INSERT INTO `purchase` VALUES (1,2,'2023-12-06 02:54:16','2023-12-06 02:54:16'),(2,1,'2023-12-06 02:54:16','2023-12-06 02:54:16'),(3,1,'2023-12-06 02:54:16','2023-12-07 12:19:28'),(4,1,'2023-12-07 12:19:28','2023-12-07 12:19:28'),(5,1,'2023-12-07 12:19:28','2023-12-07 12:19:28'),(6,3,'2023-12-06 20:15:14','2023-12-07 12:19:28'),(7,1,'2023-12-07 15:53:21','2023-12-07 15:53:21'),(8,6,'2023-12-07 15:53:21','2023-12-07 15:53:21'),(9,7,'2023-12-07 15:53:21','2023-12-07 15:53:21');
/*!40000 ALTER TABLE `purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_products`
--

DROP TABLE IF EXISTS `purchase_products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `purchase_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_id` (`purchase_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `purchase_products_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `purchase` (`purchase_id`),
  CONSTRAINT `purchase_products_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_products`
--

LOCK TABLES `purchase_products` WRITE;
/*!40000 ALTER TABLE `purchase_products` DISABLE KEYS */;
INSERT INTO `purchase_products` VALUES (1,1,7,1),(2,2,4,2),(3,3,7,1),(4,3,4,1),(5,3,1,1),(6,3,14,1),(7,3,2,3),(8,3,1,1),(9,3,15,1),(10,3,2,1),(11,4,12,1),(12,4,8,3),(13,5,14,2),(14,5,1,1),(15,6,20,1),(16,7,8,4),(17,8,1,1),(18,9,4,4),(19,9,24,1),(20,9,7,1);
/*!40000 ALTER TABLE `purchase_products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `seller_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(50) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zipcode` int NOT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES (1,'Beedle','s','beedle@email.com','Hyrule Castle Town Rd','Hyrule Castle Town','Central Hyrule',12300),(2,'Link','s','Link@email.com','Hateno Rd','Hateno Village','East Neculda',24341),(3,'Mario','s','Mario@email.com','Mushroom Kingdom Drive','Broklyn','New York',12345),(4,'Anime','s','Anime@email.com','Anime World','Kent','Ohio',12345),(5,'NFT','s','nft@email.com','NFT str','Kent','Ohio',12345),(6,'A','A','a@a.com','A','A','A',0),(7,'test','test','test@gmail.com','street','city','state',11111),(8,'Prof Bill Reed','goflashes','wreed6@kent.edu','800 E. Summit St.','Kent','OH',44242),(9,'LaneMMII','a','lanesimpson14@gmail.com','123 Orange Dr.','Fruitopia','Ohio',11111);
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-07 19:57:58
