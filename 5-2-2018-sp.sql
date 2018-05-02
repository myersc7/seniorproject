-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: senior_project
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.16.04.1

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
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `proj_name` varchar(45) NOT NULL,
  `total_diff` int(11) DEFAULT NULL,
  `github_link` varchar(100) DEFAULT NULL,
  `Dod` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (3,'ProfBot',0,'https://github.com/myersc7/seniorproject','Complete all PBIs without bugs. Make customer happy!!!'),(4,'Matt\'s project',NULL,NULL,NULL),(5,'Matt\'s project',NULL,NULL,NULL),(6,'Matt\'s project',NULL,NULL,NULL),(7,'Matt\'s project',NULL,NULL,NULL),(9,'Test Project',0,NULL,NULL),(10,'Test Project',0,NULL,NULL),(11,' jk',0,NULL,NULL),(16,'Test',0,NULL,NULL),(17,'Hi',0,NULL,NULL),(18,'Matt proj 2',0,NULL,NULL),(19,'yay',0,NULL,NULL),(24,'test',0,NULL,NULL),(28,'Agility',0,NULL,'Complete Website. Make Baliga happy'),(29,'WebAI',0,NULL,'fdasf'),(31,'balls',0,NULL,NULL),(32,'RowanScrum',0,NULL,NULL),(33,'Prolog',0,NULL,'Working AI'),(42,'Test project 2',0,NULL,'test this one two'),(43,'Test project 3',0,NULL,NULL),(44,'testRole',0,NULL,NULL),(45,'test forever',0,NULL,'check'),(47,'Video Game',0,NULL,'Complete all aspects of the game and remove all bugs'),(48,'Predictive Maintenance',0,NULL,'Provide predictions for maintenance based on data set. GET SOMETHING TO EAT.\r\n\r\n\r\nDefinition of Done WORKS.'),(49,'Machine Learning Project',0,NULL,'Our definition of done will be met when our algorithm works'),(50,'Artificial Intelligence Project',0,NULL,'Create a chess game with an artificial intelligence capable of beating the player. '),(60,'Recipe App',0,NULL,NULL),(64,'fdsa',0,NULL,'fdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsaffdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafssfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafsfdafsfdsafadsaf');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_sprint_table`
--

DROP TABLE IF EXISTS `project_sprint_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_sprint_table` (
  `project_sprint_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `sprint_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`project_sprint_table_id`),
  KEY `idproject_idx` (`project_id`),
  KEY `idsprint_idx` (`sprint_id`),
  CONSTRAINT `idproject` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `idsprint` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_sprint_table`
--

LOCK TABLES `project_sprint_table` WRITE;
/*!40000 ALTER TABLE `project_sprint_table` DISABLE KEYS */;
INSERT INTO `project_sprint_table` VALUES (4,1,3),(5,6,3),(6,7,3),(7,8,28),(8,9,28),(9,10,28),(15,16,3),(16,17,24),(17,18,24),(18,19,42),(19,20,42),(20,21,42),(21,22,42),(22,23,42),(23,24,42),(24,25,42),(25,26,42),(26,27,42),(27,28,42),(28,29,42),(29,30,42),(30,31,42),(31,32,42),(32,33,43),(33,34,3),(34,35,45),(35,36,29),(36,37,32),(37,38,48),(38,39,47),(39,40,47),(40,41,48),(41,42,48),(42,43,42),(43,44,47),(49,50,49),(50,51,50),(51,52,50),(52,53,50),(55,56,44),(58,59,44),(61,62,44),(62,63,44),(63,64,44),(64,65,44),(75,77,43),(78,80,60),(79,81,64),(80,82,33),(81,83,3);
/*!40000 ALTER TABLE `project_sprint_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requirements`
--

DROP TABLE IF EXISTS `requirements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `requirements` (
  `requirements_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `text` varchar(45) NOT NULL,
  `user_stories_id` int(11) NOT NULL,
  PRIMARY KEY (`requirements_id`),
  KEY `idusreq_idx` (`user_stories_id`),
  CONSTRAINT `idusreq` FOREIGN KEY (`user_stories_id`) REFERENCES `user_stories` (`user_stories_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requirements`
--

LOCK TABLES `requirements` WRITE;
/*!40000 ALTER TABLE `requirements` DISABLE KEYS */;
/*!40000 ALTER TABLE `requirements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `role_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE KEY `title_UNIQUE` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (3,'Developer'),(4,'Member'),(2,'Product Owner'),(1,'Scrum Master');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_user_table`
--

DROP TABLE IF EXISTS `role_user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_user_table` (
  `role_user_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`role_user_table_id`),
  KEY `idrole_idx` (`role_id`),
  KEY `iduser_idx` (`user_id`),
  CONSTRAINT `idrole` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iduser` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_user_table`
--

LOCK TABLES `role_user_table` WRITE;
/*!40000 ALTER TABLE `role_user_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_user_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sprint`
--

DROP TABLE IF EXISTS `sprint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sprint` (
  `sprint_id` int(11) NOT NULL AUTO_INCREMENT,
  `end_date` date NOT NULL,
  `start_date` date NOT NULL,
  `sprint_num` int(11) DEFAULT NULL,
  `Retro` varchar(200) DEFAULT NULL,
  `Review` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`sprint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sprint`
--

LOCK TABLES `sprint` WRITE;
/*!40000 ALTER TABLE `sprint` DISABLE KEYS */;
INSERT INTO `sprint` VALUES (1,'2018-03-31','2018-03-04',1,'Work on communication','Sprint went well, customer was happy'),(6,'2018-04-30','2018-03-31',2,'Communication improved but Billy needs to work harder','Sprint went well but we may to spike next sprint, customer was happy'),(7,'2018-05-30','2018-04-30',3,'Billy got a lot done this sprint, Eric slacked off','We were able to skip taking a spike and finsihed a lot'),(8,'2018-03-15','2018-02-15',1,'Communication was really poor','Customer wished we accomplished more, explained that we need a spike, they seemed ok with it'),(9,'2018-04-15','2018-03-15',2,'Communication really improved, we need to make sure Mike doesn\'t do all the work','Customer was happy with progress, made a few good suggestions'),(10,'2018-05-15','2018-04-15',3,'Great sprint, everyone worked hard','Customer was pleased, added some PB items'),(11,'2018-04-17','2018-04-17',1,NULL,NULL),(12,'2018-04-17','2018-04-17',2,NULL,NULL),(13,'2018-04-20','2018-04-17',3,NULL,NULL),(14,'2018-04-20','2018-04-17',4,NULL,NULL),(15,'2018-04-20','2018-04-17',5,NULL,NULL),(16,'2018-05-05','2018-04-05',4,NULL,NULL),(17,'2018-05-05','2018-04-05',1,NULL,NULL),(18,'2018-08-07','2018-06-07',2,NULL,NULL),(19,'2018-08-07','2018-06-05',1,NULL,NULL),(20,'2018-05-05','2018-06-05',2,NULL,NULL),(21,'2018-05-01','2018-04-05',3,NULL,NULL),(22,'2018-07-05','2018-04-06',4,NULL,NULL),(23,'2018-08-07','2018-06-05',5,NULL,NULL),(24,'2018-07-05','2018-04-19',6,NULL,NULL),(25,'2018-02-02','2018-01-01',7,NULL,NULL),(26,'2018-04-04','2018-03-03',8,NULL,NULL),(27,'2018-08-07','2018-06-05',9,NULL,NULL),(28,'2018-11-25','2018-11-20',10,NULL,NULL),(29,'2018-07-05','2018-06-05',11,NULL,NULL),(30,'2018-09-09','2018-04-19',12,NULL,NULL),(31,'2018-05-05','2018-04-05',13,NULL,NULL),(32,'2018-07-05','2018-04-05',14,NULL,NULL),(33,'2018-02-02','2018-04-19',1,NULL,NULL),(34,'2018-05-05','2018-04-05',5,NULL,'this is a sprint review.'),(35,'2018-08-07','2018-04-05',1,NULL,NULL),(36,'2018-01-22','2018-01-12',1,NULL,NULL),(37,'2018-01-22','2018-01-12',1,NULL,NULL),(38,'2018-04-30','2018-04-23',1,NULL,NULL),(39,'2018-05-20','2018-04-20',1,NULL,NULL),(40,'2018-06-20','2018-05-20',2,NULL,NULL),(41,'2018-05-08','2018-05-01',2,NULL,NULL),(42,'1943-02-19','1943-02-12',3,NULL,NULL),(43,'2018-07-05','2018-06-05',15,NULL,NULL),(44,'2018-07-20','2018-06-20',3,NULL,NULL),(45,'2018-05-08','2018-04-24',1,NULL,NULL),(46,'2018-05-22','2018-05-08',2,NULL,NULL),(47,'2018-06-05','2018-05-22',3,NULL,NULL),(48,'2018-06-19','2018-06-05',4,NULL,NULL),(49,'2018-07-03','2018-06-19',5,NULL,NULL),(50,'2018-05-08','2018-04-24',1,NULL,NULL),(51,'2018-05-08','2018-04-24',1,NULL,NULL),(52,'2018-05-22','2018-05-08',2,NULL,NULL),(53,'2018-06-05','2018-05-22',3,NULL,NULL),(54,'2018-07-05','2018-04-05',1,NULL,NULL),(55,'2018-05-05','2018-06-05',2,NULL,NULL),(56,'2018-01-02','2018-01-01',1,NULL,NULL),(57,'2018-02-02','2018-04-19',3,NULL,NULL),(58,'2018-05-05','2018-04-19',4,NULL,NULL),(59,'2018-01-04','2018-01-03',2,NULL,NULL),(60,'2018-05-05','2018-04-05',5,NULL,NULL),(61,'2018-05-05','2018-04-06',6,NULL,'test test'),(62,'2018-01-06','2018-01-05',3,NULL,NULL),(63,'2018-01-08','2018-01-07',4,NULL,NULL),(64,'2018-01-10','2018-01-09',5,NULL,NULL),(65,'2018-01-12','2018-01-11',6,NULL,NULL),(66,'2018-05-01','2018-04-30',1,NULL,NULL),(67,'2018-04-21','2018-04-17',1,'123','fdsafdsafdsaf'),(68,'2018-05-07','2018-04-30',1,'test','test test'),(69,'2018-05-14','2018-05-07',2,NULL,NULL),(70,'2018-05-01','2018-04-17',1,NULL,NULL),(71,'2018-05-01','2018-04-17',1,NULL,NULL),(72,'2018-05-01','2018-04-17',1,'retro','rev'),(73,'2018-05-01','2018-04-17',2,NULL,NULL),(74,'2018-05-05','2018-04-05',1,NULL,NULL),(75,'2018-08-07','2018-06-05',2,NULL,NULL),(76,'2018-05-01','2018-04-05',3,NULL,NULL),(77,'2018-08-07','2018-04-19',2,NULL,NULL),(78,'2018-05-01','2018-04-17',1,NULL,NULL),(79,'2018-05-01','2018-04-17',1,NULL,NULL),(80,'2018-06-01','2018-05-01',1,NULL,NULL),(81,'2018-05-01','2018-04-17',1,'fdsafds','fdsafsd'),(82,'2018-06-19','2018-05-22',1,NULL,NULL),(83,'2018-06-19','2018-05-01',6,NULL,NULL);
/*!40000 ALTER TABLE `sprint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team` (
  `team_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_name` varchar(45) NOT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (1,'Agility Team'),(2,'goobernuggets'),(3,'goobernuggets'),(4,'goobernuggets'),(5,'goobernuggets'),(7,'Test Team'),(8,'Test Team'),(9,'jnjk'),(14,'Test'),(15,'Hi'),(16,'the best team'),(17,'CoolStuff'),(18,'Test Team'),(19,'Test Team'),(20,'Test Team'),(21,'Test Team'),(22,'test'),(23,'test'),(24,'test'),(25,'test'),(26,'Agility'),(27,'Web'),(28,'team'),(29,'bslls'),(30,'RedTeam'),(31,'PLTeam1'),(32,'New Team'),(33,'Panini'),(34,'Rowan scrum'),(35,'Rowan team'),(36,'Team Matt'),(37,'Rowan scrum'),(38,'Rowan scrum'),(39,'Rowan scrum'),(40,'woop'),(41,'Team Matt'),(42,'HighRollers'),(43,'test'),(44,'ScrumMasters'),(45,'Gamers'),(46,'Clams'),(47,'Blue Team'),(48,'Team SkyNet'),(49,'poow'),(50,'uniquenaame12347'),(51,'t4'),(52,'Team test'),(53,'Test team'),(54,'test del team'),(55,'fdsafsd'),(56,'The Bug Squashers'),(57,'tt'),(58,'Coding Cooks'),(59,'Test Team'),(60,'test'),(61,'test'),(62,'fdsa'),(63,'test');
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_project_table`
--

DROP TABLE IF EXISTS `team_project_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_project_table` (
  `team_project_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `team_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`team_project_table_id`),
  KEY `idproject_idx` (`project_id`),
  KEY `idteam_idx` (`team_id`),
  CONSTRAINT `idprojectteam` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  CONSTRAINT `idteamproj` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_project_table`
--

LOCK TABLES `team_project_table` WRITE;
/*!40000 ALTER TABLE `team_project_table` DISABLE KEYS */;
INSERT INTO `team_project_table` VALUES (4,1,3),(5,14,16),(6,15,17),(7,16,18),(13,22,24),(18,27,29),(20,17,28),(21,29,31),(22,30,32),(23,31,33),(32,40,42),(33,41,43),(34,42,44),(35,43,45),(37,45,47),(38,46,48),(39,47,49),(40,48,50),(50,58,60),(54,62,64);
/*!40000 ALTER TABLE `team_project_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_sprint_table`
--

DROP TABLE IF EXISTS `team_sprint_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_sprint_table` (
  `team_sprint_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `sprint_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`team_sprint_table_id`),
  KEY `idteamsprint_idx` (`team_id`),
  KEY `idsprintteam_idx` (`sprint_id`),
  CONSTRAINT `idsprintteam` FOREIGN KEY (`sprint_id`) REFERENCES `sprint` (`sprint_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `idteamsprint` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_sprint_table`
--

LOCK TABLES `team_sprint_table` WRITE;
/*!40000 ALTER TABLE `team_sprint_table` DISABLE KEYS */;
INSERT INTO `team_sprint_table` VALUES (1,1,1),(2,6,1),(3,7,1),(4,8,17),(5,9,17),(6,10,17);
/*!40000 ALTER TABLE `team_sprint_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_user_table`
--

DROP TABLE IF EXISTS `team_user_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_user_table` (
  `team_user_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`team_user_table_id`),
  KEY `idteamuse_idx` (`team_id`),
  KEY `iduserteam_idx` (`user_id`),
  CONSTRAINT `idteamuser` FOREIGN KEY (`team_id`) REFERENCES `team` (`team_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iduserteam` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_user_table`
--

LOCK TABLES `team_user_table` WRITE;
/*!40000 ALTER TABLE `team_user_table` DISABLE KEYS */;
INSERT INTO `team_user_table` VALUES (1,6,1,1),(2,6,14,NULL),(3,6,15,NULL),(4,5,16,NULL),(5,6,17,NULL),(7,4,18,NULL),(8,13,1,2),(9,4,19,NULL),(10,4,20,NULL),(11,4,21,NULL),(12,5,22,NULL),(13,9,23,NULL),(14,4,24,NULL),(15,9,25,1),(16,13,26,NULL),(17,13,27,NULL),(18,4,28,NULL),(19,13,17,NULL),(20,6,29,NULL),(21,13,30,NULL),(22,9,31,3),(23,4,32,NULL),(24,4,33,1),(25,13,34,NULL),(26,13,35,NULL),(27,13,36,NULL),(28,13,37,NULL),(29,13,38,NULL),(30,13,39,NULL),(31,5,40,2),(32,5,41,NULL),(33,5,33,1),(34,9,42,NULL),(35,15,43,NULL),(36,5,43,3),(37,15,28,NULL),(38,16,44,NULL),(39,16,45,NULL),(40,18,46,1),(41,17,47,2),(42,11,45,NULL),(43,15,1,3),(44,11,44,NULL),(45,15,16,1),(46,15,40,NULL),(47,4,44,NULL),(48,12,44,NULL),(49,13,44,NULL),(50,13,46,3),(51,18,47,NULL),(52,17,46,NULL),(53,20,1,3),(54,21,1,3),(55,13,45,NULL),(56,13,47,NULL),(57,17,48,NULL),(58,5,49,NULL),(59,18,48,NULL),(60,8,33,1),(61,9,33,1),(62,7,28,NULL),(63,5,50,NULL),(64,19,48,3),(65,23,49,1),(66,24,49,NULL),(67,22,49,2),(68,19,50,3),(69,4,51,NULL),(70,4,52,NULL),(71,4,53,1),(72,13,25,3),(73,4,54,NULL),(74,4,55,NULL),(75,5,56,1),(76,5,55,NULL),(77,19,56,NULL),(78,4,57,NULL),(79,25,58,1),(80,4,59,NULL),(81,11,58,2),(82,25,60,NULL),(83,25,61,NULL),(84,4,62,NULL),(85,13,31,3),(86,11,63,1),(87,25,63,2),(88,5,62,NULL),(89,25,1,3);
/*!40000 ALTER TABLE `team_user_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `to_do`
--

DROP TABLE IF EXISTS `to_do`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `to_do` (
  `to_do_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NOT NULL,
  `text` varchar(45) NOT NULL,
  `user_stories_id` int(11) NOT NULL,
  PRIMARY KEY (`to_do_id`),
  KEY `idtdus_idx` (`user_stories_id`),
  CONSTRAINT `idtdus` FOREIGN KEY (`user_stories_id`) REFERENCES `user_stories` (`user_stories_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `to_do`
--

LOCK TABLES `to_do` WRITE;
/*!40000 ALTER TABLE `to_do` DISABLE KEYS */;
/*!40000 ALTER TABLE `to_do` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password_hash` varchar(120) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (4,'admin','admin@example.com','pbkdf2:sha256:50000$dyHUV4sN$c6c7b16fada0a1f4f23f864752fc1abcad0d3ccbcff55834c7ee2552c8cbe00d'),(5,'newman22','newman22@students.rowan.edu','pbkdf2:sha256:50000$OkulUppk$369d42a40a9a4ce60a2a1527da5bc27fb63e966ea64ab349efae2e300156fd21'),(6,'Steve-o','canzan40@students.rowan.edu','pbkdf2:sha256:50000$inrDMMVJ$8a3f354d2adf9e5c96f04ca38ae5cacf39f1748df590e87ba92e48f6dc6cd043'),(7,'testmedaddy','Matthew.curwood11@gmail.com','pbkdf2:sha256:50000$JzOfDIPv$fc910898437c75cf0a6478c377316cc4781552f2d163a06c12831ce127d0ac30'),(8,'agile','agile@agility.com','pbkdf2:sha256:50000$9otffU5F$6edd9a65bbeba260b2789644463462e034ef06b7a07a185d9a1944cbdd861e07'),(9,'mpg','gman@fakeemail.test','pbkdf2:sha256:50000$NvLvCuCd$a5e21012d794b79452554ce19943abf50b7f8d9042ed654e77e4e2faf9693051'),(10,'wert','wert@wert.wert','pbkdf2:sha256:50000$kB4iE4L1$92575e9d8dcff8ff8486dc08f19d3c2fbd259a48a549e10eadfc72c5af3a6674'),(11,'canzi','stephen@gmail.com','pbkdf2:sha256:50000$NqCJFchP$da882361de8c9bd7d55046ad857d26970a889e4e9771f69fcb274b7dc27160e5'),(12,'tester','tester@test.com','pbkdf2:sha256:50000$jlutEQ1r$b8f1c28f0434e5d48af1c9bfbffec4f716cbd61ec470be64a2b77a2c514c4a78'),(13,'demo','demo@rowan.edu','pbkdf2:sha256:50000$2y3k7HMS$564901572879feb71dc0b138a911952f61e6bd8526beeb39b57c48d81b6307df'),(14,'test123','test@testes.com','pbkdf2:sha256:50000$6uRjolyf$be05351816d51b6d0c6109cb8098624e4e8e25dd89a02aba79256a74918c49cf'),(15,'test','test@gmail.com','pbkdf2:sha256:50000$UHj8yZDF$3fa9b28734a023610abd127eb13eb6b80d9124edf59bbb0e822d320d4d6baaf8'),(16,'agileuser22','scrummaster@gmail.com','pbkdf2:sha256:50000$lnFDQabs$623c964f281a92d7c5c544ee4b14d1d79655d37d3fe5f5a70c1ec37df30b61be'),(17,'JohnSmith123','Jsmith@students.rowan.edu','pbkdf2:sha256:50000$61mhju2b$e2bdc2c6e8670fe4eb18115903e3d04272be1466957163824117ed85a69ac3f6'),(18,'myersc7','myersc7@students.rowan.edu','pbkdf2:sha256:50000$YmFug8C9$b27a6246b3a889a514c424b9fc86b3850689d77bcd6a14eba9cf4fa02e5b0b15'),(19,'testA','testA@gmail.com','pbkdf2:sha256:50000$6uViISVB$8f83436154f4ffae73f902b9f5c14382ade894d871507b68008f10e42acc43fa'),(20,'testB','testB@gmail.com','pbkdf2:sha256:50000$gkeniayj$ea38c1a4233ad74d533f13a97eb0617d5836b034db986a9e1cdc92091aee68ce'),(21,'testC','testC@gmail.com','pbkdf2:sha256:50000$3FncDVx1$af77eab70571cf6cdaeecd6e48862c8c6e89f91e1965eaf1f2eea22569852b1c'),(22,'testD','testD@gmail.com','pbkdf2:sha256:50000$93zgY0Im$bd4c340f776eca81d08614106e82bb7caa3d2d0090938675bb1394915f559288'),(23,'testE','testE@gmail.com','pbkdf2:sha256:50000$BKaNP5n9$6bdb22da0184329dc0f5cee0ed29b821773bee7eba576d1278066e38f274abc7'),(24,'testF','testF@gmail.com','pbkdf2:sha256:50000$91qORufH$3d09df7bf542826d088ac8efe9623197d47f8c1caf822e706528a2e411da1534'),(25,'scrumlover','scrumlover@gmail.com','pbkdf2:sha256:50000$NBFJiL4m$39978403dcc05ccbc58883d77b007764d5c19f888404511c95ade6c6533566c7');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_stories`
--

DROP TABLE IF EXISTS `user_stories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_stories` (
  `user_stories_id` int(11) NOT NULL AUTO_INCREMENT,
  `difficulty` int(11) NOT NULL,
  `acceptance_criteria` varchar(400) NOT NULL,
  `status` varchar(45) NOT NULL,
  `description` varchar(400) NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`user_stories_id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_stories`
--

LOCK TABLES `user_stories` WRITE;
/*!40000 ALTER TABLE `user_stories` DISABLE KEYS */;
INSERT INTO `user_stories` VALUES (1,5,'Complete Entirely','PBI','This is a test user story','Test User Story 1'),(2,7,'Must have functioning buttons.','Done','The interface needs a submit button to enter the users input','Interface Submit'),(3,3,'Needs to be a functioning and accessible database','Done','Need a database to store Profbot Responses','ProfBot Database'),(4,7,'BurnUp must display total difficulty and difficulty completed for each sprint','Done','Get the burnup chart working','BurnUp Chart'),(5,9,'Clean, easy to read UI','Done','The user needs an interface to use ProfBot','User Interface'),(6,3,'Must be able to handle inputs from user','In Progress','The user needs to be able submit their desired inputs to ProfBot ','User Input to ProfBot'),(7,5,'Must be able to respond to user quickly','In Progress','Once the user inputs a question/statement ProfBot needs to respond in a reasonable amount of time','ProfBot Responses'),(8,11,'ProfBot must generate relevant responses','Done','When a user submits a question/statement Profbot needs to interpret the input and generate a response','ProfBot Response time'),(9,1,'Must be a functioning Database','Done','We need a working database to store all the info from the site','Database'),(10,4,'Needs to be a functioning login page','Done','Users need to be able to login to view their projects','Login Page'),(11,6,'Page needs to display a burnup chart','Done','Users should be able to monitor project progress','Project Page'),(12,2,'Page needs to display a product backlog','Done','Users need to be able view cards and sprints','Sprint Management Page'),(13,10,'Needs to display To Do, In Progress, Done','In Progress','Users need to be manage their sprints','Sprint Page'),(14,7,'Needs to display the information of the team members','Done','Users should be able to view all members of their team','Team Page'),(15,2,'We need models of the database to use for passing information to it','Done','We need to be able to store user information','Database Models'),(16,2,'CSS style sheet must be locally installed and cant rely on CDNs','In Progress','We need a singel css style sheet to style all html files','CSS Style Sheet'),(17,3,'User interface must have a Rowan logo as background','Done','ProfBot needs a logo','Ruwan Logo'),(18,5,'Must be able to add new projects to the user profile','PBI','This site is all about Project management and users need to be able to add new projects','Add Project'),(19,5,'Must be able to add new sprints to the user projects','PBI','This site is all about Project management and users need to be able to add sprints to their projects','Add Sprint'),(20,8,'Must be able to display card info at the click of a button','PBI','Users will need to be able to manage their user stories','View Card button'),(21,1,'- Download Prolog','In Progress','Download prolog','Download Prolog'),(22,10,'Make sure the site is functional by Sunday\r\n','PBI','Make core functional','Finish Senior project'),(23,12,'ajdnsdnsd','To do','fdsa','Test1'),(24,4,'90% done','PBI','some desc','some title'),(25,15,'Only if everything works','Done','Make sure the demo runs smoothly','Test things during'),(26,5,'Make sure there are no errors','To do','Needs updating','Run the project on aws'),(27,5,'Professor is happy','Done','Needs updating','See if card functionality works on website'),(28,15,'with bugs noted','Done','Send in a video','Rowan project demo'),(29,7,'APA format','PBI','A write up pertaining to what we have learned','Final essay'),(30,3,'Mutable','PBI','This should be on the project page','Create Def of done'),(31,15,'needs to be on the team page','PBI','3 different roles woo','Add role'),(32,7,'Gather user input','Done','Using Beta test','Test the project'),(33,7,'Needs to be uploaded to youtube, in a folder with our bugs','Done','Run a demo for the professor','Run the demo'),(34,3,'Testyyy','In Progress','test','Test User Story 1 change'),(35,5,'test 2','Done','test 2','test 2'),(36,1,'sssss','In Progress','sssnjn','Test things during lent mop'),(37,7,'Move from the backlog to test','Done','Right now it gets attached to the sprint that is current but it needs to move with the next sprint','Make sure the pbi moves with the new sprint'),(38,2,'check','PBI','manually put the url in','check delete'),(39,1,'noids','PBI','ndosk','delete me'),(41,1,'1','PBI','1','check1'),(42,21,'test again','PBI','test','Test Test'),(45,1,'delete','PBI','delete','delete'),(50,5,'Must be able to enter username and password ','In Progress','A page for users to log in','Sign In Page'),(51,3,'Must have a unique one for every character','Done','Sprites for each character','Create Sprites'),(52,6,'Must display all options','PBI','Home screen that appears when the game is turned on','Home Screen'),(53,12,'sdfsdf','Done','sdfsdfsdsd33444','sdfsdf'),(54,2,'Must display all teams and records in order by record','To do','Show all teams in the league','League Page'),(56,1,'This card is complete when you are no longer hungry.','Done','EAT FOOD','Get something to eat'),(57,1,'As a user, I should be able to get a working project using the software the scrum team has found.','In Progress','To get our project started, we need to find software we can use.','Identify Machine Learning Software'),(58,20,'LISTEN TO IT','In Progress','MUSIC','Listen to music'),(59,4,'As a user, I need my software running as efficiently as possible while the scrum team\'s code runs.','Done','Look into efficient machine learning algorithms to get a better understanding of how to accomplish our goal. ','Research Machine Learning Algorithms'),(61,8,'As a user, I expect this code to help deliver a finished product to me.','Done','Start writing code that will be the basis for the rest of the project.','Prepare a Test Script'),(62,13,'As a user, this interface should be the only point of contact between the user and the software.','In Progress','Start Building a User Interface so that the user can run our code.','Build GUI'),(63,21,'As a user, this algorithm should help generate the information needed to tell whether a ship needs maintenance or not.','In Progress','Utilize this algorithm so that our project will run more efficiently','Use Nested Trees to Create Algorithm'),(64,1,'As a user, I need steady updates regarding the project.','Done','Make sure the group can talk with each other as well as the Product Owner.','Establish Communication'),(65,1,'As a user, the product being designed to closely adhere to the specifications provided.','Done','Read through the project specifications to ensure we are building what the Product Owner wants.','Read Through Product Specs'),(66,1,'Get phone/email from each group member, get phone/email from product owner','Done','As a user, I expect the team to be in constant contact and I should receive steady updates.','Establish Communication'),(67,4,'Research past projects, look up tutorials on basic AI design, get insight from Professor','Done','As a user, I expect the team to have a firm grasp on designing AI before writing any code.','Research AI Design'),(68,1,'check','PBI','check','check'),(69,13,'As a user, the software should be working correctly before being delivered.','PBI','We should test the algorithm so that it works correctly','Test Project'),(70,1,'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz','PBI','ooimnkk','tfy'),(71,8,'As a user, this prototype should accurately demonstrate how the real software should work','PBI','Create a prototype to test on dataset','Create Working Prototype'),(72,8,'Test should be successful','Done','Test the AI Test Text','Test AI'),(73,1,'check','In Progress','check','check'),(74,1,'check','PBI','check','check'),(75,1,'Download AI related software, Determine which software is the most efficient','Done','As a user, I expect the team to use the necessary tools to complete my product','Find Software to Work With'),(76,1,'Read product specifications','Done','As a user, I expect the AI to be designed to my specifications','Read Product Owner Specs'),(77,4,'Each member design a class, combine work.','Done','As a user, the team should start designing the classes necessary to  build the AI','Design Classes'),(78,8,'Design base of chessboard, design tiles in chessboard','Done','As a user, the the chessboard the AI will be playing on must match my specifications Test text','Create Chessboard'),(79,13,'Modal all basic chess pieces, Program pieces to move according to player/AI input','Done','As a user, the player and the AI must use normal chess pieces to play','Create Pieces'),(80,8,'Program checkmate feature for game','Done','As a user, the game must end by a checkmate','Program Checkmate'),(81,13,'Program hours, program minutes, program seconds','Done','As a user, a clock must be created so that the player knows how long the game has been going on for.','Create Clock'),(82,13,'Ensure board works properly, prevent any glitches that could happen to the player.','Done','As a user, the board must work normally.','Test Board Functionality'),(83,21,'program AI, prevent defeat','Done','As a user, the AI must be programmed to win every game.','Program AI to Win'),(84,21,'Build other AI','Done','As a user, the AI must be able to compete against other AIs','Program AI vs AI Games'),(85,13,'Program menu, add different modes','Done','As a user, I must be able to choose between AI vs AI mode and AI vs Player mode','Add Menu for Different Modes'),(86,21,'Copy program, create backups in case of failure, receive profit','Done','As a user, I should be able to sell this program.','Make Copies of Program'),(87,21,'AI must work, ','Done','As a user, the AI must work','Test AI Again'),(88,15,'Run multiple times','PBI','split the data to 70 percent learning and 30 percent validation','70/30 split to validate machine learning'),(89,10,'Make sure page doesn\'t break','To do','Eliminate remaining bugs','Senior project'),(90,123,'fdsafdsa','PBI','desc','fdsafdsa'),(91,21,'test','In Progress','test','test'),(92,21,'test','Done','wert','test2'),(93,121321321,'fdsafsad','PBI','fdsfsd','fdsafdas'),(95,4,'fdsa','In Progress','fdsafds','fdsafdsa'),(96,3,'This is just filler','PBI','This is just filler ','test the bugs'),(97,1,'bhiub','Done','bjibi','burn up'),(98,55,'fadsffdsa321','PBI','fdsaffdsa321','fdsafdsa213'),(101,321,'fdsa','PBI','fdsa','fdsa'),(102,321,'fdsa','PBI','fdsafdsa','fdsafsa'),(103,321,'fsad','To do','fdsafdsa','fdsa'),(104,321,'fdsafsa','PBI','fdsaf','fdsafdsa'),(105,3212,'fdsa2','Done','fdsa2','fdsafdsa2'),(107,321,'fdsa','In Progress','fdsa','fdsafds'),(109,321,'fdsa','PBI','fdsa','fdsaf'),(110,3,'Must display welcome message and search options for name, ingredients, and culture','Done','Main menu to give search options','Main Menu'),(111,321,'fdsa','To do','fdsafads','fdsafdsa'),(112,3213213,'dsfdsafdsafdasfd','PBI','fdsafdsafasdf','fdsafdsafads'),(113,3,'Must be able to search by ingredient, name, or culture','PBI','Search algorithm','Search functionality'),(114,5,'Must function and represent all the proper relationships','Done','Database to store all recipes','Database'),(115,1,'test','PBI','test','test'),(117,321,'321fdsa','Done','321','fdsa'),(118,2,'We have to show a working project','Done','Live demo','Do a live demo'),(119,21,'test','Done','test','test'),(120,1,'fdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsaffdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafssfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafsfdafsfadsafadsa','PBI','fdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsaffdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafssfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafsfdafsfadsafadsa','fdas'),(121,1,'fdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsaffdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafssfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafsfdafsfadsafadsa','PBI','fdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsaffdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafssfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafdafsfdsafdsafsfdsafdsafsfdsafdsafsfdsafsfdafsfadsafadsa','fdsa');
/*!40000 ALTER TABLE `user_stories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_stories_project_table`
--

DROP TABLE IF EXISTS `user_stories_project_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_stories_project_table` (
  `user_stories_project_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_stories_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`user_stories_project_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_stories_project_table`
--

LOCK TABLES `user_stories_project_table` WRITE;
/*!40000 ALTER TABLE `user_stories_project_table` DISABLE KEYS */;
INSERT INTO `user_stories_project_table` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,1,3),(6,2,3),(7,3,3),(9,5,3),(10,6,3),(11,7,3),(12,8,3),(13,17,3),(14,9,28),(15,10,28),(16,11,28),(17,12,28),(18,13,28),(19,14,28),(20,15,28),(21,16,28),(22,4,28),(23,19,28),(24,18,28),(25,21,33),(27,23,29),(29,25,3),(30,26,3),(31,27,3),(32,28,3),(33,29,3),(34,30,28),(36,32,3),(37,33,3),(38,34,42),(39,35,42),(40,36,43),(41,37,3),(45,41,45),(46,42,32),(54,50,47),(55,51,47),(56,52,47),(57,53,48),(58,54,47),(60,56,48),(61,57,49),(62,58,48),(63,59,49),(65,61,49),(66,62,49),(67,63,49),(68,64,49),(69,65,49),(70,66,50),(71,67,50),(72,68,42),(73,69,49),(74,70,42),(75,71,49),(76,72,50),(79,75,50),(80,76,50),(81,77,50),(82,78,50),(83,79,50),(84,80,50),(85,81,50),(86,82,50),(87,83,50),(88,84,50),(89,85,50),(90,86,50),(91,87,50),(92,88,50),(114,110,60),(117,113,60),(118,114,60),(121,117,64),(122,118,3),(123,119,33),(124,120,64),(125,121,64);
/*!40000 ALTER TABLE `user_stories_project_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_stories_sprint_table`
--

DROP TABLE IF EXISTS `user_stories_sprint_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_stories_sprint_table` (
  `user_stories_sprint_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_stories_id` int(11) NOT NULL,
  `sprint_id` int(11) NOT NULL,
  PRIMARY KEY (`user_stories_sprint_table_id`),
  KEY `user_stories_id_idx` (`user_stories_id`),
  KEY `idsprintus_idx` (`sprint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_stories_sprint_table`
--

LOCK TABLES `user_stories_sprint_table` WRITE;
/*!40000 ALTER TABLE `user_stories_sprint_table` DISABLE KEYS */;
INSERT INTO `user_stories_sprint_table` VALUES (2,2,6),(3,3,6),(5,5,7),(6,17,7),(7,9,8),(8,10,10),(9,11,10),(10,12,9),(11,16,9),(12,4,8),(13,8,7),(14,27,7),(15,28,7),(18,30,16),(20,32,16),(21,33,16),(22,34,20),(23,35,19),(24,36,33),(25,37,34),(38,50,39),(39,51,40),(41,53,38),(42,54,40),(44,56,41),(45,57,45),(46,58,42),(47,59,45),(49,61,45),(50,62,49),(51,63,49),(52,64,50),(53,65,50),(54,66,51),(55,67,51),(60,72,53),(61,73,61),(63,75,51),(64,76,51),(65,77,51),(66,78,52),(67,79,52),(68,80,52),(69,81,52),(70,82,52),(71,83,53),(72,84,53),(73,85,53),(74,86,53),(75,87,53),(77,89,66),(79,91,68),(80,92,68),(85,97,75),(95,107,78),(98,110,80),(99,111,79),(102,114,80),(105,117,81),(106,118,34),(107,119,82);
/*!40000 ALTER TABLE `user_stories_sprint_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user_stories_table`
--

DROP TABLE IF EXISTS `user_user_stories_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_user_stories_table` (
  `user_user_stories_table_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_stories_id` int(11) NOT NULL,
  PRIMARY KEY (`user_user_stories_table_id`),
  KEY `iduserus_idx` (`user_id`),
  KEY `iduser_storiesuser_idx` (`user_stories_id`),
  CONSTRAINT `iduser_storiesuser` FOREIGN KEY (`user_stories_id`) REFERENCES `user_stories` (`user_stories_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `iduserus` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user_stories_table`
--

LOCK TABLES `user_user_stories_table` WRITE;
/*!40000 ALTER TABLE `user_user_stories_table` DISABLE KEYS */;
INSERT INTO `user_user_stories_table` VALUES (1,13,3),(2,13,2),(3,13,1),(4,13,4),(5,13,5),(6,13,6),(7,13,7),(8,13,8),(9,13,9),(10,13,10),(11,13,11),(12,13,12),(13,13,13),(14,13,14),(15,13,15),(16,13,16);
/*!40000 ALTER TABLE `user_user_stories_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `works_on` (
  `works_on_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_stories_id` int(11) NOT NULL,
  PRIMARY KEY (`works_on_id`),
  KEY `iduserustories_idx` (`user_id`),
  KEY `idususer_idx` (`user_stories_id`),
  CONSTRAINT `iduserustories` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `idususer` FOREIGN KEY (`user_stories_id`) REFERENCES `user_stories` (`user_stories_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
INSERT INTO `works_on` VALUES (1,13,2),(2,13,3);
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-02 19:20:01
