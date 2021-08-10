-- MySQL dump 10.13  Distrib 5.7.35, for Linux (x86_64)
--
-- Host: localhost    Database: streetcube
-- ------------------------------------------------------
-- Server version	5.7.35-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `streetcube`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `streetcube` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `streetcube`;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(300) DEFAULT NULL,
  `msg` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'Mohit','mohit@gmail.com','Issue For Slot Booking','Sometime not working slot system');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_style_details`
--

DROP TABLE IF EXISTS `food_style_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_style_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cuisine_name` varchar(255) NOT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=419 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_style_details`
--

LOCK TABLES `food_style_details` WRITE;
/*!40000 ALTER TABLE `food_style_details` DISABLE KEYS */;
INSERT INTO `food_style_details` VALUES (1,'Ackee & Saltfish','2018-04-14 01:57:34',1),(2,'African Cuisine','2018-04-14 01:57:34',1),(3,'Alcohol','2018-04-14 01:57:34',1),(4,'Ale /Beer /Lager','2018-04-14 01:57:34',1),(5,'American BBQ /Smoking','2018-04-14 01:57:34',1),(6,'American Cuisine','2018-04-14 01:57:34',1),(7,'Anti Pasti','2018-04-14 01:57:34',1),(8,'Arabic Cuisine','2018-04-14 01:57:34',1),(9,'Arancini Balls','2018-04-14 01:57:34',1),(10,'Arepas','2018-04-14 01:57:34',1),(11,'Argentine Cuisine','2018-04-14 01:57:34',1),(12,'Asian Cuisine','2018-04-14 01:57:34',1),(13,'Asian Soups/Noodle Soup','2018-04-14 01:57:34',1),(14,'Australian Cuisine','2018-04-14 01:57:34',1),(15,'Austrian Sausages','2018-04-14 01:57:34',1),(16,'Baby Food','2018-04-14 01:57:34',1),(17,'Bacon','2018-04-14 01:57:34',1),(18,'Bagels','2018-04-14 01:57:34',1),(19,'Bahn Mi Sandwiches','2018-04-14 01:57:34',1),(20,'Baked/ Jacket Potatoes','2018-04-14 01:57:34',1),(21,'Baked beans','2018-04-14 01:57:34',1),(22,'Baked Cheese/Camembert','2018-04-14 01:57:34',1),(23,'Beef','0000-00-00 00:00:00',1),(24,'Bakery/Boulangerie','0000-00-00 00:00:00',1),(25,'Baklava','0000-00-00 00:00:00',1),(26,'Balti','0000-00-00 00:00:00',1),(27,'Bananas','0000-00-00 00:00:00',1),(28,'Bao/Steamed Buns','0000-00-00 00:00:00',1),(29,'Barm Cakes','0000-00-00 00:00:00',1),(30,'Basque Cuisine','0000-00-00 00:00:00',1),(31,'BBQ/Hog Roast/Rotisserie','0000-00-00 00:00:00',1),(32,'Beans & Pulses','0000-00-00 00:00:00',1),(33,'Butterscotch','0000-00-00 00:00:00',1),(34,'Belginum Chocolate','0000-00-00 00:00:00',1),(35,'Beverage Fountain','0000-00-00 00:00:00',1),(36,'Bistro Style Food','0000-00-00 00:00:00',1),(37,'Black Pudding/Blood Sausage','0000-00-00 00:00:00',1),(38,'Bobotie (South African curry)','0000-00-00 00:00:00',1),(39,'Boerwors/Sausage','0000-00-00 00:00:00',1),(40,'Brazilian Cuisine','0000-00-00 00:00:00',1),(41,'Bread','0000-00-00 00:00:00',1),(42,'Breakfast','0000-00-00 00:00:00',1),(43,'Breakfast Muffin','0000-00-00 00:00:00',1),(44,'Brisket','0000-00-00 00:00:00',1),(45,'Brownies','0000-00-00 00:00:00',1),(46,'Bubble & Squeak','0000-00-00 00:00:00',1),(47,'Bubble Tea','0000-00-00 00:00:00',1),(48,'Buffalo','0000-00-00 00:00:00',1),(49,'Bunny Chow','0000-00-00 00:00:00',1),(50,'Burek (shallow fried filo parcel)','0000-00-00 00:00:00',1),(51,'Burgers','0000-00-00 00:00:00',1),(52,'Burritos','0000-00-00 00:00:00',1),(53,'Cheesecakes','0000-00-00 00:00:00',1),(54,'cafe','0000-00-00 00:00:00',1),(55,'cajun/Creole Cuisine','0000-00-00 00:00:00',1),(56,'Cakes/Pastreis/Bisuits','0000-00-00 00:00:00',1),(57,'Calimari','0000-00-00 00:00:00',1),(58,'Calzone','0000-00-00 00:00:00',1),(59,'Canapes','0000-00-00 00:00:00',1),(60,'Candy Floss/Popcorn/Toffee Apples','0000-00-00 00:00:00',1),(61,'Cannoli','0000-00-00 00:00:00',1),(62,'Caribbean Cuisine','0000-00-00 00:00:00',1),(63,'Carvery','0000-00-00 00:00:00',1),(64,'Cassava','0000-00-00 00:00:00',1),(65,'Casseroles/Stews/One Pot','0000-00-00 00:00:00',1),(66,'Ceviche','0000-00-00 00:00:00',1),(67,'Chaat','0000-00-00 00:00:00',1),(68,'Chai','0000-00-00 00:00:00',1),(69,'Champagne/Prosecco','0000-00-00 00:00:00',1),(70,'Chapatis','0000-00-00 00:00:00',1),(71,'Cheese','0000-00-00 00:00:00',1),(72,'Cheese Croquettes','0000-00-00 00:00:00',1),(73,'Cocktails','0000-00-00 00:00:00',1),(74,'Cheesy Chips','0000-00-00 00:00:00',1),(75,'Chestnuts (Roast)','0000-00-00 00:00:00',1),(76,'Chicken','0000-00-00 00:00:00',1),(77,'Chillean Cuisine','0000-00-00 00:00:00',1),(78,'Chilli','0000-00-00 00:00:00',1),(79,'Chimney Cakes','0000-00-00 00:00:00',1),(80,'Chinese Cuisine','0000-00-00 00:00:00',1),(81,'Chips/Fries','0000-00-00 00:00:00',1),(82,'Chips on a stick','0000-00-00 00:00:00',1),(83,'Chocolate','0000-00-00 00:00:00',1),(84,'Chocolate Fountain','0000-00-00 00:00:00',1),(85,'Chocolate Sauce & Nutella','0000-00-00 00:00:00',1),(86,'Chocolate Specialist','0000-00-00 00:00:00',1),(87,'Chorizo','0000-00-00 00:00:00',1),(88,'Churros','0000-00-00 00:00:00',1),(89,'Ciabatta','0000-00-00 00:00:00',1),(90,'Cider','0000-00-00 00:00:00',1),(91,'Clam Chowder','0000-00-00 00:00:00',1),(92,'Cockles','0000-00-00 00:00:00',1),(93,'Coconuts','2018-08-14 11:08:11',1),(95,'Coffee','2018-08-14 11:10:16',1),(96,'Coffee Specialist','2018-08-14 11:10:38',1),(97,'Coleslaw','2018-08-14 11:10:55',1),(98,'Colombian Cuisine','2018-08-14 11:11:08',1),(99,'Continental Breakfast','2018-08-14 11:11:32',1),(100,'Cookies','2018-08-14 11:11:39',1),(101,'Coq au Vin','2018-08-14 11:11:48',1),(102,'Corn Dogs','2018-08-14 11:12:03',1),(103,'Corn in a Cup','2018-08-14 11:12:13',1),(104,'Corn on the Cob','2018-08-14 11:12:23',1),(105,'Corn Tortilla','2018-08-14 11:12:33',1),(106,'Cornbread','2018-08-14 11:12:39',1),(107,'Cous Cous','2018-08-14 11:13:01',1),(108,'Crab','2018-08-14 11:13:08',1),(109,'Crab feet','2018-08-14 11:13:15',1),(110,'Crab sticks','2018-08-14 11:13:21',1),(111,'Crawfish Bisque','2018-08-14 11:13:30',1),(112,'Crasfish Pie','2018-08-14 11:18:24',1),(113,'Cream','2018-08-14 11:25:20',1),(114,'Crepes/Pancakes','2018-08-14 11:25:57',1),(115,'Crew Catering','2018-08-14 11:49:33',1),(117,'Croissants','2018-08-14 11:50:13',1),(118,'Crostini','2018-08-14 11:50:33',1),(119,'Crumpets','2018-08-14 11:50:57',1),(120,'Crustaceans','2018-08-14 11:51:20',1),(121,'Cuban Cusine','2018-08-14 11:51:35',1),(122,'Cupcakes','2018-08-14 11:52:03',1),(123,'Curly Fries','2018-08-14 11:52:15',1),(124,'Curry','2018-08-14 11:52:23',1),(125,'Curry Wurst','2018-08-14 11:57:03',1),(126,'Dairy','2018-08-18 18:02:37',1),(127,'Dairy free','2018-08-18 18:02:50',1),(128,'Deep Fried Pickles','2018-08-18 18:03:10',1),(129,'Dessert Specialist','2018-08-18 18:03:29',1),(130,'Deviled Kidneys','2018-08-18 18:03:45',1),(131,'Dosas','2018-08-18 18:03:58',1),(132,'Doughunts/ Donuts','2018-08-18 18:04:24',1),(133,'Duck','2018-08-18 18:05:00',1),(134,'Dumplings','2018-08-18 18:05:09',1),(135,'Dutch Cuisine','2018-08-18 18:05:17',1),(136,'Eggs Benedict / Royale','2018-08-18 18:05:37',1),(137,'Elote','2018-08-18 18:05:55',1),(138,'Empanadas','2018-08-18 18:06:42',1),(139,'Enchiladas','2018-08-18 18:09:13',1),(140,'Ethiopian Food','2018-08-18 18:10:09',1),(141,'Exotic / Wild game /Rare Breed','2018-08-18 18:10:45',1),(142,'Fajitas','2018-08-18 18:10:52',1),(143,'Falafel','2018-08-18 18:11:03',1),(144,'Festivals','2018-08-18 18:11:09',1),(145,'Fish & Chips','2018-08-18 18:11:24',1),(146,'Fish Cakes','2018-08-18 18:11:29',1),(147,'Fish Finger Sandwiches','2018-08-18 18:11:39',1),(148,'Fish Fingers','2018-08-18 18:11:58',1),(149,'Flapjacks','2018-08-18 18:12:07',1),(150,'Fondu','2018-08-18 18:12:13',1),(152,'Foraged Produce','2018-08-18 18:13:20',1),(153,'Frankfurter','2018-08-18 18:13:44',1),(154,'French Cuisine','2018-08-18 18:13:57',1),(155,'Fried Chicken','2018-08-18 18:14:32',1),(156,'Fritters','2018-08-18 18:14:38',1),(157,'Fritters (deep Fried)','2018-08-18 18:15:00',1),(159,'Fritters (pan fried)','2018-08-18 18:16:02',1),(160,'Frozen Youghurt','2018-08-18 18:16:14',1),(162,'Fruit Pies','2018-08-18 18:16:38',1),(163,'Fruit Puree','2018-08-18 18:16:50',1),(164,'Fruits / Nuts / Vegetables','2018-08-18 18:17:00',1),(165,'Full English Breakfast','2018-08-18 18:17:28',1),(166,'Funnel Cakes','2018-08-18 18:18:11',1),(167,'Gammon','2018-08-18 18:18:16',1),(168,'Garlic Bread','2018-08-18 18:18:35',1),(169,'Gelato','2018-08-18 18:18:54',1),(170,'General Purpose (Traditional Bacon, Burgers, Hotdogs, chips etc)','2018-08-18 18:19:51',1),(171,'Geogian/ Caucasian Cuisine','2018-08-18 18:20:18',1),(172,'German Cuisine','2018-08-18 18:20:25',1),(173,'German Sausage','2018-08-18 18:20:32',1),(174,'Ghanaian Cuisine','2018-08-18 18:20:56',1),(175,'Gin','2018-08-18 18:20:59',1),(176,'Gluten Free','2018-08-18 18:21:10',1),(177,'Goat Curry','2018-08-18 18:21:18',1),(178,'Gourmet Sausages','2018-08-18 18:21:42',1),(179,'Granita','2018-08-18 18:21:49',1),(180,'Italian Cuisine','2018-08-18 18:22:38',1),(181,'Jambalaya','2018-08-18 18:22:43',1),(182,'Japanese Cuisine','2018-08-18 18:22:51',1),(185,'Jerk','2018-08-18 18:24:07',1),(184,'Jellied Eels, Mash & Liquor','2018-08-18 18:23:43',1),(186,'Jollof Rice','2018-08-18 18:24:14',1),(187,'Juicess / Smoothies','2018-08-18 18:24:27',1),(188,'Kebabs','2018-08-18 18:24:35',1),(189,'Kedgeree','2018-08-18 18:24:54',1),(190,'Korean Cuisine','2018-08-18 18:25:21',1),(191,'Kosher Food/ Cuisine','2018-08-18 18:25:33',1),(192,'Lahmacun','2018-08-18 18:25:40',1),(193,'Lamb','2018-08-18 18:25:50',1),(194,'Lasagna','2018-08-18 18:25:57',1),(195,'Latin American','2018-08-18 18:26:32',1),(196,'Laver breed / seaweed','2018-08-18 18:26:59',1),(197,'Lebanese Cuisine','2018-08-18 18:27:30',1),(198,'Lamonade / Root Beer / Ginger Beer','2018-08-18 18:27:58',1),(199,'Licquorice','2018-08-18 18:28:17',1),(200,'Line Caught / Sustainable Fish','2018-08-18 18:29:03',1),(201,'Lobster','2018-08-18 18:29:15',1),(202,'Mac n Cheese','2018-08-18 18:29:21',1),(203,'Malaysian Cuisine','2018-08-18 18:29:43',1),(204,'Maple Syrup / golden Syrup','2018-08-18 18:30:02',1),(205,'Marshmallows','2018-08-18 18:30:15',1),(206,'Mashed Potato','2018-08-18 18:30:29',1),(207,'Mauritian Cuisine','2018-08-18 18:30:38',1),(208,'Meatballs','2018-08-18 18:30:46',1),(209,'Mediterranean Cuisine','2018-08-18 18:31:06',1),(210,'Mexican Cuisine','2018-08-18 18:31:20',1),(211,'Mezze','2018-08-18 18:31:27',1),(212,'Middle Eastern Cuisine','2018-08-18 18:31:45',1),(213,'Milkshakes','2018-08-18 18:31:52',1),(214,'Mobile Bar','2018-08-18 18:31:57',1),(215,'Mocktails','2018-08-18 18:32:15',1),(216,'Modern British Fusion','2018-08-18 18:32:31',1),(217,'Moroccan Cuisine','2018-08-18 18:32:42',1),(218,'Muesli','2018-08-18 18:32:56',1),(219,'Muffins','2018-08-18 18:33:01',1),(220,'Mulled Wine','2018-08-18 18:33:07',1),(221,'Mushrooms','2018-08-18 18:33:15',1),(222,'Mushy Peas','2018-08-18 18:33:21',1),(223,'Mussels / Moules','2018-08-18 18:33:32',1),(224,'Naan Bread','2018-08-18 18:33:52',1),(225,'Nachos','2018-08-18 18:34:41',1),(226,'Native American Cuisine','2018-08-18 18:34:55',1),(227,'Nepalese','2018-08-18 18:36:32',1),(228,'Noodles','2018-08-18 18:36:40',1),(229,'Nuggets','2018-08-18 18:36:44',1),(230,'Nuts (Gourment)','2018-08-18 18:36:55',1),(231,'Oatcakes','2018-08-18 18:37:18',1),(232,'Octopus','2018-08-18 18:37:29',1),(233,'Omelettes / Galettes','2018-08-18 18:38:01',1),(234,'Organic','2018-08-18 18:38:23',1),(235,'Ostritch','2018-08-18 18:38:44',1),(236,'Ox Roast','2018-08-18 18:46:43',1),(237,'Oysters','2018-08-18 18:47:04',1),(238,'Paella','2018-08-18 18:47:10',1),(239,'Pakora','2018-08-18 18:47:14',1),(240,'Paleo','2018-08-18 18:47:25',1),(241,'Paratha','2018-08-18 18:47:33',1),(242,'Parmo','2018-08-18 18:47:44',1),(243,'Partridge/ Pheasant','2018-08-18 18:48:03',1),(244,'Pasta','2018-08-18 18:48:08',1),(245,'Pasties / Pies','2018-08-18 18:48:22',1),(246,'Pastrami','2018-08-18 18:48:29',1),(247,'Patates Bravas','2018-08-18 18:48:37',1),(248,'Pate','2018-08-18 18:48:54',1),(249,'Patties (Jamaican)','2018-08-18 18:49:07',1),(251,'Pea & Ham Soup','2018-08-18 18:49:34',1),(252,'Persian Cuisine','2018-08-18 18:49:44',1),(253,'Peruvian Cuisine','2018-08-18 18:49:51',1),(254,'Phillipino Cuisine','2018-08-18 18:50:26',1),(255,'Pho','2018-08-18 18:50:31',1),(256,'Pie Specialist','2018-08-18 18:50:41',1),(257,'Pie, Mash, Liquor','2018-08-18 18:50:50',1),(258,'Pimms','2018-08-18 18:51:11',1),(259,'Pintxos','2018-08-18 18:51:31',1),(260,'Piri Piri','2018-08-18 18:51:39',1),(261,'Pitta Bread','2018-08-18 18:51:46',1),(262,'Pizza','2018-08-18 18:51:51',1),(263,'Plaintain','2018-08-18 18:51:56',1),(264,'Po\' Boys','2018-08-18 18:52:11',1),(265,'Poffertjes (dutch pancakes)','2018-08-18 18:54:07',1),(266,'Polenta','2018-08-18 18:54:15',1),(267,'Polish Cuisine','2018-08-18 18:54:24',1),(268,'Popcorn','2018-08-18 18:54:32',1),(269,'Popcorn (artisan)','2018-08-18 18:54:47',1),(270,'Pork','2018-08-18 18:54:52',1),(271,'Pork Rolls / Crackling','2018-08-18 18:55:21',1),(272,'Porridge','2018-08-18 18:55:32',1),(273,'Portuguese Cuisine','2018-08-18 18:55:47',1),(274,'Potato Croquettes','2018-08-18 18:56:02',1),(275,'Potato Croquettes','2018-08-18 18:56:27',1),(276,'Potato Pancakes','2018-08-18 18:56:41',1),(277,'Poutine','2018-08-18 18:56:50',1),(278,'Prawns / Shrimp','2018-08-18 18:57:00',1),(279,'Pretzels','2018-08-18 18:57:18',1),(280,'Private parties','2018-08-18 18:57:33',1),(281,'Pulled Pork','2018-08-18 18:57:43',1),(282,'Pyclet','2018-08-18 18:57:50',1),(283,'Quiche','2018-08-18 18:58:00',1),(284,'Quinoa','2018-08-18 18:58:04',1),(285,'Rabbit / Hare','2018-08-18 18:58:13',1),(286,'Raclette','2018-08-18 18:58:30',1),(287,'Ratatouille','2018-08-18 18:58:48',1),(288,'Ribs','2018-08-18 18:58:52',1),(289,'Rice','2018-08-18 18:58:54',1),(290,'Rice & Peas','2018-08-18 18:59:02',1),(291,'Risotto','2018-08-18 18:59:08',1),(292,'Roast Beef','2018-08-18 18:59:14',1),(293,'Roast Lamb','2018-08-18 18:59:18',1),(294,'Roast Pork','2018-08-18 18:59:27',1),(295,'Roast Potatoes','2018-08-18 18:59:44',1),(296,'Roast Turkey','2018-08-18 18:59:51',1),(297,'Romanian Cuisine','2018-08-18 19:00:04',1),(298,'Roti','2018-08-18 19:00:11',1),(299,'Salad (Speciallist)','2018-08-18 19:00:54',1),(300,'Salads','2018-08-18 19:01:06',1),(301,'Salt Beef','2018-08-18 19:01:11',1),(302,'Samosas / Bhajis','2018-08-18 19:01:36',1),(303,'Sandwiches / Baguettes / Bagels / Wraps','2018-08-18 19:02:27',1),(304,'Satay','2018-08-18 19:03:02',1),(305,'Sausage & Mash','2018-08-18 19:03:11',1),(306,'Sausage in batter','2018-08-18 19:03:19',1),(307,'Sausage Rolls','2018-08-18 19:03:34',1),(308,'Sausage/Egg/Bacon Butties','2018-08-18 19:04:33',1),(309,'Scallops','2018-08-18 19:04:43',1),(310,'Scampi','2018-08-18 19:04:52',1),(311,'Scandinavian Cuisine','2018-08-18 19:05:26',1),(312,'Schnitzel','2018-08-18 19:05:37',1),(313,'Scotch Eggs','2018-08-18 19:05:45',1),(314,'Scottish Cuisine','2018-08-18 19:05:54',1),(315,'Seafood','2018-08-18 19:05:57',1),(316,'Seasonal / Local Produce','2018-08-18 19:06:08',1),(317,'Senegalese Cusine','2018-08-18 19:06:17',1),(318,'Shami Kebab','2018-08-18 19:06:31',1),(319,'Shawarma','2018-08-18 19:06:43',1),(320,'Shellfish','2018-08-18 19:06:49',1),(321,'Shish/Sheesh Kebab','2018-08-18 19:07:09',1),(322,'Skewers','2018-08-18 19:07:14',1),(323,'Slush','2018-08-18 19:07:22',1),(324,'Smoked Salmon','2018-08-18 19:07:31',1),(325,'Snow Cones','2018-08-18 19:07:37',1),(326,'Soft Drinks','2018-08-18 19:07:46',1),(327,'Soft Tacos','2018-08-18 19:07:54',1),(328,'Sopaipillas','2018-08-18 19:08:02',1),(329,'Sorbet','2018-08-18 19:08:06',1),(330,'Soup','2018-08-18 19:08:11',1),(331,'South African Cuisine','2018-08-18 19:08:21',1),(332,'South Indian / Goan','2018-08-18 19:08:36',1),(333,'Souvlaki','2018-08-18 19:08:43',1),(334,'Soya','2018-08-18 19:10:07',1),(335,'Spaetzle (noodles)','2018-08-18 19:10:25',1),(336,'Spanish Cuisine','2018-08-18 19:11:11',1),(337,'Spring Roll','2018-08-18 19:11:23',1),(338,'Sri Lankan / Tamil Cuisine','2018-08-18 19:11:42',1),(339,'Steaks','2018-08-18 19:11:47',1),(340,'Stir Fry','2018-08-18 19:11:57',1),(341,'Stovies','2018-08-18 19:12:04',1),(342,'Strawberries & Cream','2018-08-18 19:12:22',1),(343,'Strawberry Sauce','2018-08-18 19:12:34',1),(344,'Suger free','2018-08-18 19:12:43',1),(345,'Surimi','2018-08-18 19:12:50',1),(346,'Surinamese Cuisine','2018-08-18 19:13:26',1),(347,'Sushi','2018-08-18 19:13:32',1),(348,'Sushi Burger','2018-08-18 19:13:44',1),(349,'Sweet Rice','2018-08-18 19:13:54',1),(350,'Sweets/ Confectionery/Fudge','2018-08-18 19:14:25',1),(351,'Tabbouleh/Tabouleh','2018-08-20 11:26:41',1),(352,'Tagine','2018-08-20 11:27:36',1),(353,'Taiwanese Cuisine','2018-08-20 11:27:46',1),(354,'Tandoori','2018-08-20 11:27:51',1),(355,'Tapas','2018-08-20 11:27:55',1),(356,'Tea Specialist','2018-08-20 11:28:03',1),(357,'Tempura','2018-08-20 11:28:22',1),(358,'Teriyaki','2018-08-20 11:28:29',1),(359,'Thai cuisine','2018-08-20 11:28:37',1),(360,'Tikka','2018-08-20 11:28:40',1),(361,'Toast','2018-08-20 11:28:45',1),(362,'Toasted Sandwiches/ Paninis / Paninos','2018-08-20 11:29:04',1),(363,'Tofu','2018-08-20 11:29:08',1),(364,'Tofta Fritta','2018-08-20 11:29:15',1),(365,'Tortilla','2018-08-20 11:29:24',1),(366,'Traditional British','2018-08-20 11:29:34',1),(367,'Tuna / Swordfish','2018-08-20 11:30:01',1),(368,'Turkish Cuisine','2018-08-20 11:30:10',1),(369,'Vegetarian / Vegan','2018-08-20 11:30:29',1),(370,'Venezuelan Cuisine','2018-08-20 11:30:44',1),(371,'Venison','2018-08-20 11:30:56',1),(372,'Victorian Cuisine','2018-08-20 11:31:06',1),(373,'Vietnamese Cuisine','2018-08-20 11:31:44',1),(374,'Waffles (American)','2018-08-20 11:31:59',1),(375,'Waffles (Belgian)','2018-08-20 11:32:39',1),(376,'Waffles (Dutch)','2018-08-20 11:33:35',1),(377,'Wedding Caterer','2018-08-20 11:33:45',1),(378,'Wedges','2018-08-20 11:34:05',1),(379,'West African Cuisine','2018-08-20 11:54:54',1),(380,'Whelks','2018-08-20 11:55:03',1),(381,'Wild Boar','2018-08-20 11:56:00',1),(382,'Wine','2018-08-20 11:56:05',1),(383,'Wings','2018-08-20 11:56:16',1),(384,'Wood Fired Pizza','2018-08-20 11:58:40',1),(385,'Yoghurt','2018-08-20 11:58:44',1),(386,'Yorkshire PUddings','2018-08-20 11:58:55',1),(387,'Granola','2018-08-20 12:01:10',1),(388,'Greek Food','2018-08-20 12:01:20',1),(390,'Grilled Cheese Sandwich','2018-08-20 12:01:55',1),(391,'Grilled Fish','2018-08-20 12:02:14',1),(392,'Gumbo','2018-08-20 12:02:23',1),(393,'Gyoza','2018-08-20 12:02:34',1),(394,'Haggis','2018-08-20 12:02:39',1),(395,'Halal','2018-08-20 12:02:44',1),(396,'Halloumi','2018-08-20 12:02:50',1),(397,'Ham Hock','2018-08-20 12:02:57',1),(398,'Hawaiian Ice','2018-08-20 12:03:07',1),(399,'Herbal Teas & Drinks','2018-08-20 12:03:26',1),(401,'Home Made Sauces & Marinades','2018-08-20 12:06:45',1),(402,'Homemade Chutney','2018-08-20 12:06:54',1),(403,'Hot Beef Rous','2018-08-20 12:07:06',1),(404,'Hot Chocolate','2018-08-20 12:07:16',1),(405,'Hot Dogs','2018-08-20 12:07:30',1),(406,'Hummus','2018-08-20 12:07:34',1),(407,'Hungarian Cuisine','2018-08-20 12:07:47',1),(408,'Ice Cream','2018-08-20 12:07:56',1),(409,'Ice Lollies (artisan / gourmet)','2018-08-20 12:08:44',1),(410,'Iced Coffee','2018-08-20 12:08:55',1),(411,'Iced Tea','2018-08-20 12:09:00',1),(412,'Indian Cuisine','2018-08-20 12:09:13',1),(413,'Indian Desserts','2018-08-20 12:09:20',1),(414,'Indonesian','2018-08-20 12:09:54',1),(415,'Insect Canape\'s','2018-08-20 12:10:12',1),(416,'Iraqi Cuisine','2018-08-20 12:10:27',1),(417,'Irish Cuisine','2018-08-20 12:10:40',1),(418,'Israeli Cuisine','2018-08-20 12:10:50',1);
/*!40000 ALTER TABLE `food_style_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_10th`
--

DROP TABLE IF EXISTS `gazebo_process_10th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_10th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `daily_rental` varchar(255) DEFAULT NULL,
  `clients_need` varchar(255) DEFAULT NULL,
  `turnover` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_10th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_10th`
--

LOCK TABLES `gazebo_process_10th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_10th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_10th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_11th`
--

DROP TABLE IF EXISTS `gazebo_process_11th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_11th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `specific_location` varchar(255) DEFAULT NULL,
  `land_owner` varchar(255) DEFAULT NULL,
  `jurisdict_authority` varchar(255) DEFAULT NULL,
  `is_storage_req` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_11th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_11th`
--

LOCK TABLES `gazebo_process_11th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_11th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_11th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_12th`
--

DROP TABLE IF EXISTS `gazebo_process_12th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_12th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `signature` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_12th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_12th`
--

LOCK TABLES `gazebo_process_12th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_12th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_12th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_3rd`
--

DROP TABLE IF EXISTS `gazebo_process_3rd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_3rd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `nationality` varchar(150) DEFAULT NULL,
  `passport_no` varchar(150) DEFAULT NULL,
  `national_insurance_no` varchar(150) DEFAULT NULL,
  `known_medical_conditions` varchar(150) DEFAULT NULL,
  `next_of_kin_name` varchar(150) DEFAULT NULL,
  `next_of_kin_contact` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_3rd_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_3rd`
--

LOCK TABLES `gazebo_process_3rd` WRITE;
/*!40000 ALTER TABLE `gazebo_process_3rd` DISABLE KEYS */;
INSERT INTO `gazebo_process_3rd` VALUES (13,109,'Text-1','852963','456123','NA','Dyna','King'),(14,110,'Text-1','43554wtgre','dfghdfj','hgdhd','hghghg','dfghfh'),(15,111,'Text-1','43554wtgre','qwew','qewqew','aqew','qwe');
/*!40000 ALTER TABLE `gazebo_process_3rd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_4th`
--

DROP TABLE IF EXISTS `gazebo_process_4th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_4th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `food_style` varchar(150) DEFAULT NULL,
  `describe_food_style` varchar(150) DEFAULT NULL,
  `suplier_list` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_4th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_4th`
--

LOCK TABLES `gazebo_process_4th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_4th` DISABLE KEYS */;
INSERT INTO `gazebo_process_4th` VALUES (9,NULL,'American BBQ /Smoking','trewr','rtew,trew,trwe,twre'),(16,109,'Alcohol','Alcohol is one of the drinks today','one,two,three,forth'),(17,110,'Ackee & Saltfish','hsfdxbxdfgd','ghfdhfgh,,,');
/*!40000 ALTER TABLE `gazebo_process_4th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_5th`
--

DROP TABLE IF EXISTS `gazebo_process_5th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_5th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `is_new_project` tinyint(1) DEFAULT NULL,
  `menu_type` varchar(150) DEFAULT NULL,
  `business_operate` varchar(150) DEFAULT NULL,
  `operate_yrs` varchar(150) DEFAULT NULL,
  `street_loc` varchar(150) DEFAULT NULL,
  `pop_sel_item` varchar(150) DEFAULT NULL,
  `avg_spent_client` int(11) DEFAULT NULL,
  `staff_need` int(11) DEFAULT NULL,
  `day_hour_operate` varchar(150) DEFAULT NULL,
  `is_formal_cat_quali` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_5th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_5th`
--

LOCK TABLES `gazebo_process_5th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_5th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_5th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_6th`
--

DROP TABLE IF EXISTS `gazebo_process_6th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_6th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `proof_of_ncass_doc` varchar(255) DEFAULT NULL,
  `cv_doc` varchar(255) DEFAULT NULL,
  `level_2_hygiene_doc` varchar(255) DEFAULT NULL,
  `covid_19_safety_doc` varchar(255) DEFAULT NULL,
  `health_safety_doc` varchar(255) DEFAULT NULL,
  `first_aid_doc` varchar(255) DEFAULT NULL,
  `fire_extinguisher_doc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_6th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_6th`
--

LOCK TABLES `gazebo_process_6th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_6th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_6th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_7th`
--

DROP TABLE IF EXISTS `gazebo_process_7th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_7th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `sustain_training_doc` varchar(255) DEFAULT NULL,
  `haccp_training_doc` varchar(255) DEFAULT NULL,
  `lpg_gas_safe_doc` varchar(255) DEFAULT NULL,
  `copy_of_pass_doc` varchar(255) DEFAULT NULL,
  `proof_of_insu_doc` varchar(255) DEFAULT NULL,
  `about_exp` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_7th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_7th`
--

LOCK TABLES `gazebo_process_7th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_7th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_7th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_8th`
--

DROP TABLE IF EXISTS `gazebo_process_8th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_8th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `company_brand_name` varchar(255) DEFAULT NULL,
  `reg_company_name` varchar(255) DEFAULT NULL,
  `reg_company_no` varchar(255) DEFAULT NULL,
  `reg_company_address` varchar(255) DEFAULT NULL,
  `reg_trading_name` varchar(255) DEFAULT NULL,
  `name_of_your_operation` varchar(255) DEFAULT NULL,
  `retail_price` varchar(255) DEFAULT NULL,
  `kitchen_uses` varchar(255) DEFAULT NULL,
  `serving_methods` varchar(255) DEFAULT NULL,
  `other_kitchen_items` varchar(255) DEFAULT NULL,
  `all_the_equip_uses` varchar(255) DEFAULT NULL,
  `drinks_serve` varchar(255) DEFAULT NULL,
  `cooking_method` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_8th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_8th`
--

LOCK TABLES `gazebo_process_8th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_8th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_8th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gazebo_process_9th`
--

DROP TABLE IF EXISTS `gazebo_process_9th`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gazebo_process_9th` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `have_company_name` varchar(255) DEFAULT NULL,
  `vat_reg` varchar(255) DEFAULT NULL,
  `delivery_agents` varchar(255) DEFAULT NULL,
  `about_your_business` varchar(255) DEFAULT NULL,
  `length_of_trading` varchar(255) DEFAULT NULL,
  `desired_commence` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `gazebo_process_9th_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gazebo_process_9th`
--

LOCK TABLES `gazebo_process_9th` WRITE;
/*!40000 ALTER TABLE `gazebo_process_9th` DISABLE KEYS */;
/*!40000 ALTER TABLE `gazebo_process_9th` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_order`
--

DROP TABLE IF EXISTS `member_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `slot_book_id` int(11) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `txn_id` varchar(100) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `payment_response` varchar(20) NOT NULL,
  `create_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  KEY `slot_book_id` (`slot_book_id`),
  CONSTRAINT `member_order_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `member_order_ibfk_2` FOREIGN KEY (`slot_book_id`) REFERENCES `slot_booking_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_order`
--

LOCK TABLES `member_order` WRITE;
/*!40000 ALTER TABLE `member_order` DISABLE KEYS */;
INSERT INTO `member_order` VALUES (13,3,46,'4','pending','paid','success','2020-11-28 12:41:40');
/*!40000 ALTER TABLE `member_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_list`
--

DROP TABLE IF EXISTS `product_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `products` varchar(100) DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_list`
--

LOCK TABLES `product_list` WRITE;
/*!40000 ALTER TABLE `product_list` DISABLE KEYS */;
INSERT INTO `product_list` VALUES (1,'Choose Product','2021-05-11 12:11:41',1),(2,'Vegan BBQ Black burger','2021-05-11 12:12:32',1),(3,'Vegan Peri Peri burger','2021-05-11 12:12:59',1),(4,'Vegan mountain burger','2021-05-11 12:13:39',1),(5,'Chicken burger','2021-05-11 12:14:05',1),(6,'Beef burger','2021-05-11 12:14:33',1),(7,'Classic burger','2021-05-11 12:27:56',1),(8,'Vegan Smart Hot dog','2021-05-11 12:28:26',1),(9,'German Hot dog','2021-05-11 12:28:50',1),(10,'Organic Fries','2021-05-11 12:29:27',1),(11,'Mix Salad','2021-05-11 12:30:06',1),(12,'Cesar Salad','2021-05-11 12:30:32',1),(13,'Drinks','2021-05-11 12:30:58',1);
/*!40000 ALTER TABLE `product_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_check_data`
--

DROP TABLE IF EXISTS `sample_check_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_check_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `choose_product` varchar(100) DEFAULT NULL,
  `organic_produce` float DEFAULT NULL,
  `seasonal_produce` float DEFAULT NULL,
  `locally_grown` float DEFAULT NULL,
  `zero_plastic` float DEFAULT NULL,
  `zero_waste_to_landfill` float DEFAULT NULL,
  `vegetable_meat_ratio` float DEFAULT NULL,
  `nutritional_content` float DEFAULT NULL,
  `non_sugar_drinks` float DEFAULT NULL,
  `allergy_rating` float DEFAULT NULL,
  `non_diary_drinks` float DEFAULT NULL,
  `total_sus_score` float DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `sample_check_data_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_check_data`
--

LOCK TABLES `sample_check_data` WRITE;
/*!40000 ALTER TABLE `sample_check_data` DISABLE KEYS */;
INSERT INTO `sample_check_data` VALUES (61,109,'German Hot dog',80,80,80,80,80,90,80,80,90,90,83,'2021-05-13 07:26:36',0);
/*!40000 ALTER TABLE `sample_check_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `show_book_date`
--

DROP TABLE IF EXISTS `show_book_date`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `show_book_date` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `book_date` date DEFAULT NULL,
  `slot` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `show_book_date_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `slot_booking_details` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `show_book_date`
--

LOCK TABLES `show_book_date` WRITE;
/*!40000 ALTER TABLE `show_book_date` DISABLE KEYS */;
INSERT INTO `show_book_date` VALUES (54,46,'2020-11-22',NULL),(55,47,'2021-04-23',NULL);
/*!40000 ALTER TABLE `show_book_date` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slot_booking_details`
--

DROP TABLE IF EXISTS `slot_booking_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slot_booking_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `book_by` int(11) DEFAULT NULL,
  `choose_slot` varchar(50) DEFAULT NULL,
  `select_date` varchar(50) DEFAULT NULL,
  `booking_cost` varchar(50) DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  `is_expired` tinyint(1) DEFAULT NULL,
  `hash_code` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `slot_booking_details_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slot_booking_details`
--

LOCK TABLES `slot_booking_details` WRITE;
/*!40000 ALTER TABLE `slot_booking_details` DISABLE KEYS */;
INSERT INTO `slot_booking_details` VALUES (46,3,1,'1','2020-11-22, 2020-11-29','4','2020-11-19 05:37:24',0,''),(47,4,1,'1','2021-04-23, 2021-04-30','4','2021-04-15 06:14:21',0,'GTCVUK54TKCAA4HUQMNDXAYYT');
/*!40000 ALTER TABLE `slot_booking_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slots`
--

DROP TABLE IF EXISTS `slots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slots` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slots`
--

LOCK TABLES `slots` WRITE;
/*!40000 ALTER TABLE `slots` DISABLE KEYS */;
INSERT INTO `slots` VALUES (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11'),(12,'12'),(13,'13'),(14,'14');
/*!40000 ALTER TABLE `slots` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `slots_info`
--

DROP TABLE IF EXISTS `slots_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `slots_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slot` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `slot_register` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `slots_info`
--

LOCK TABLES `slots_info` WRITE;
/*!40000 ALTER TABLE `slots_info` DISABLE KEYS */;
INSERT INTO `slots_info` VALUES (1,'1','2','2020-11-12 05:04:59'),(2,'2','3','2020-11-12 05:05:13'),(3,'3','4','2020-11-12 05:05:47');
/*!40000 ALTER TABLE `slots_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trader_details`
--

DROP TABLE IF EXISTS `trader_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trader_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `mobile` bigint(20) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `c_name` varchar(150) DEFAULT NULL,
  `b_name` varchar(150) DEFAULT NULL,
  `descrip_of_service` varchar(1000) DEFAULT NULL,
  `story` varchar(1000) DEFAULT NULL,
  `pub_lib_insu` varchar(1000) DEFAULT NULL,
  `c_19risk_asses` varchar(1000) DEFAULT NULL,
  `food_certi` varchar(1000) DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `trader_details_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trader_details`
--

LOCK TABLES `trader_details` WRITE;
/*!40000 ALTER TABLE `trader_details` DISABLE KEYS */;
INSERT INTO `trader_details` VALUES (1,2,'Banglore',8252259506,'shyam4kmr@gmail.com','NIIT','NIIT TECH','Awesome Food','Great','fh9nf69gzokvnk5hj4frkr3cj.doc','q4it1qgxwshqmjidl9mz098cj.doc','yzcg5mv0tsjb7vsgy1qorx7le.doc','2020-11-11 15:19:05'),(2,3,'Ranchi Gaya',8580307220,'shyam4niit@gmail.com','HCL','HCL TECH','Great','Awesome','utmi6x8wsphtyvkwgthkh1iur.png','uoonqz5wzyoyhgy27eke6xc4t.docx','d16ln3b2mjlbsvne9eedpychm.docx','2020-11-11 16:15:23'),(6,4,'Hazaribag',8210352394,'janmejayniit@gmail.com','Tech India','Tech','Awesome','Good','teexrwnhkj4kmxvurks4wisgu.jpg','zqial5yzbuhlcyqqu0fjlqi8g.png','mz1qhtoululkbyiyhcx99grzt.jpg','2020-11-12 06:27:19'),(7,9,'Hazaribag',7033110595,'hypemax@gmail.com','Jetsoftech','Jetsoftech','Good','Awesome','zvsjpyfxr8ibuxtxyhs8gjlri.pdf','z9y5cuuki5zezknipvdpcmwn5.jpg','5ehamh05oovbkyop7jvzx49s8.jpg','2020-11-16 11:02:55'),(8,10,'Keredari',7004956982,'sachudubey143@gmail.com','Keredari Tech','Tech India','That\'s Great','Awesome','am1r8axvqbryjo0cmtzgmv18z.jpg','7dpglks3w0ljaloa5vzrqvukz.docx','0','2020-11-17 05:25:23'),(9,11,'Banglore',8252259506,'mohit@gmail.com','Banglore Tech','India Tech','Goods','Awesome','vv6thsjpwknqi3j0ej1whc6pl.jpg','snvb48wnmc5izpxb57lqw6dbu.docx','jweqimsoska0myluyj2j7fj9p.jpg','2020-11-17 05:43:13'),(10,12,'Oddisa',7713242948,'hypemaxhbz@gmail.com','Jetsofttech','Tech','That\'s Great','Awesome','t9hxj685ol4jkdlpwl31tz69k.jpg','ecg8kkrytvvykvrc5psxh37jr.docx','ywigeb45h9abigzwlnvkhokdy.jpg','2020-11-17 07:01:28');
/*!40000 ALTER TABLE `trader_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_access`
--

DROP TABLE IF EXISTS `user_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_access` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `authenticate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `user_access_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `user_info` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_access`
--

LOCK TABLES `user_access` WRITE;
/*!40000 ALTER TABLE `user_access` DISABLE KEYS */;
INSERT INTO `user_access` VALUES (1,1,'1,2,3,4,5,6,7'),(2,2,'2,3,4'),(3,4,'2,3,4');
/*!40000 ALTER TABLE `user_access` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(150) DEFAULT NULL,
  `first_name` varchar(150) DEFAULT NULL,
  `last_name` varchar(150) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `name_prfx` varchar(250) DEFAULT NULL,
  `dob` varchar(250) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `mobile` bigint(20) DEFAULT NULL,
  `home_phone` bigint(20) DEFAULT NULL,
  `city` varchar(150) DEFAULT NULL,
  `town` varchar(150) DEFAULT NULL,
  `is_show_mobile` tinyint(1) DEFAULT NULL,
  `password` varchar(250) NOT NULL,
  `user_role` int(11) DEFAULT NULL,
  `profile_pic` varchar(100) DEFAULT NULL,
  `zipcode` varchar(250) DEFAULT NULL,
  `address` varchar(1000) DEFAULT NULL,
  `register_date` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `is_mobile_verified` tinyint(1) DEFAULT NULL,
  `is_email_verified` tinyint(1) DEFAULT NULL,
  `forget_password_key` varchar(150) DEFAULT NULL,
  `referral_code` varchar(250) DEFAULT NULL,
  `session_token` varchar(250) DEFAULT NULL,
  `trm_condition` tinyint(1) DEFAULT NULL,
  `no_of_logins` int(11) DEFAULT NULL,
  `cano_url` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_role` (`user_role`),
  CONSTRAINT `user_info_ibfk_1` FOREIGN KEY (`user_role`) REFERENCES `user_roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'admin',NULL,'0',NULL,NULL,NULL,'admin@gmail.com',7004956982,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$0ohzEckp$fe9ebd942eaea2b0d02aebb981d445577af705f128d33f4fd32664584463e09d',1,NULL,NULL,'0','2020-11-11 15:03:05',1,0,0,NULL,NULL,NULL,1,36,NULL),(2,'shyam',NULL,'0',NULL,NULL,NULL,'vivek@gmail.com',8252259506,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$SBSSZsfs$5714962c3f1a1e9b14bfe9ddd74a1a9669048872ed8d6a82029afd18e57c32ce',2,NULL,NULL,'Banglore','2020-11-11 15:19:05',1,1,1,NULL,NULL,NULL,1,6,NULL),(3,'Kishan',NULL,'Raj','Male',NULL,NULL,'shyam4niit@gmail.com',8580307220,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$r6KAl2aZ$34d2e6e0c187d91695d0b786531236b6aadcc2af66c7172bd954a0119cc8536f',3,NULL,NULL,'Ranchi Gaya','2020-11-11 16:14:28',1,1,0,NULL,NULL,NULL,1,54,NULL),(4,'Janmejay',NULL,'Kumar',NULL,NULL,NULL,'janmejayniit@gmail.com',8210352394,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$x8ue9Jkr$82e28366db3077cff7ed93dab6ef2704c10468601a14799450ef0f9bdba576cf',3,NULL,NULL,'0','2020-11-12 06:25:56',1,1,1,NULL,NULL,NULL,1,3,NULL),(9,'Hypemax',NULL,'Soft',NULL,NULL,NULL,'hypemax@gmail.com',7033110595,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$UskghZn1$8d5d7aa5a50d5fb82996e5d21684c4cf6ccca852b6d48b430c11155790a3bc99',3,NULL,NULL,'0','2020-11-16 11:01:24',1,1,0,NULL,NULL,NULL,1,1,NULL),(10,'Sachin',NULL,'Dubey',NULL,NULL,NULL,'sachudubey143@gmail.com',9031159576,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$2uEViQtI$71087d8221eab14ecf60da26632965350de54f6e42dedbd9b6dc2e8818997b56',3,NULL,NULL,'0','2020-11-17 05:24:24',1,1,0,NULL,NULL,NULL,1,0,NULL),(11,'Mohit',NULL,'Srivastav',NULL,NULL,NULL,'mohit@gmail.com',8252259506,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$yug9kjdG$7963f1dd70caf7277adade18b710a22e0b4ab86a1a9ab022731d45e50418188b',3,NULL,NULL,'0','2020-11-17 05:42:15',1,1,0,NULL,NULL,NULL,1,1,NULL),(12,'Pascal',NULL,'Tech',NULL,NULL,NULL,'hypemaxhbz@gmail.com',7713242948,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$8NToMwUR$5859fbf5c613a9fcb9afd4421d243da2872a7bf10eaf2371f006ce85ce5369e3',3,NULL,NULL,'0','2020-11-17 07:00:10',1,1,0,NULL,NULL,NULL,1,2,NULL),(13,'Pascal',NULL,'Gerrard ',NULL,NULL,NULL,'pascal@pascalphoto.co.uk',7713242948,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$9lDcdHTO$e740dff72b785be51170a26b4bb47d01ebdd45d26aae47938484095a12158a5c',3,NULL,NULL,'0','2020-12-16 08:36:28',1,1,0,NULL,NULL,NULL,1,0,NULL),(28,'John',NULL,'Doe',NULL,NULL,NULL,'johndoe@streetcube.org',7740174955,NULL,NULL,NULL,1,'pbkdf2:sha256:150000$LXbbujHh$a3e1621ababf6278ef75f0ea4782e3533c5c02d1089df3b04a554756e147f9b2',3,NULL,NULL,'0','2021-01-20 11:20:54',1,1,0,NULL,NULL,NULL,1,0,'gazebo'),(48,'Shubham',NULL,'Saurav',NULL,NULL,NULL,'shubhamsaurav291@icloud.com',7033110595,NULL,NULL,NULL,1,'0',3,NULL,NULL,'0','2021-01-27 10:46:01',1,1,0,NULL,NULL,NULL,1,0,'streetcube'),(109,'Kishan',NULL,'Saini',NULL,'mr','08/25/1989','kishan@gmail.com',8252259506,7482096346,'Hazaribag','Hazaribag',1,'pbkdf2:sha256:150000$ZkilXM7c$f69f8ea21b1018bfac497974e36fb0f4ff17155eddf63190d61e35489e9d3e8d',3,NULL,'825301','At Mandai Khurd Hazaribag','2021-05-12 04:39:49',1,1,0,NULL,NULL,NULL,1,0,'streetcube'),(110,'Parth',NULL,'Patel',NULL,'mr','01/07/1997','parth.saubhagyam@gmail.com',7046893486,4554543534,'London','London',1,'pbkdf2:sha256:150000$g0dykEhE$2387114567ebb720349a617da4a3f0fa68ed80bc4819487a6f3dc592b9d095a3',3,NULL,'380026','Home street ','2021-07-28 09:21:21',1,1,0,NULL,NULL,NULL,1,1,'streetcube'),(111,'Riddhi',NULL,'Surani',NULL,'ms','05/20/1997','riddhi.saubhagyam@gmail.com',9408523750,2131231321,'London','London',1,'pbkdf2:sha256:150000$R1wOg5f1$fd1b07b4cfb52acb9e025c67f97fbd72db086586eec5b73be735dbb8974c6b78',3,NULL,'380052','Home street ','2021-07-28 10:58:13',1,1,0,NULL,NULL,NULL,1,0,'streetcube');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_title` varchar(150) NOT NULL,
  `privileges` text,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_titile` (`role_title`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,'super admin',NULL,1),(2,'admin',NULL,1),(3,'trader',NULL,1);
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-28 12:28:41
