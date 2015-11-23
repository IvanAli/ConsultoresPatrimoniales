-- MySQL dump 10.13  Distrib 5.5.45, for CYGWIN (i686)
--
-- Host: localhost    Database: consultores_patrimoniales
-- ------------------------------------------------------
-- Server version	5.5.45

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'admin'),(1,'agente');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_20b2c0b5_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_5ca07131_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_20b2c0b5_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_4e5ddfe2_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add cliente',7,'add_cliente'),(20,'Can change cliente',7,'change_cliente'),(21,'Can delete cliente',7,'delete_cliente'),(22,'Can add cliente fisico',8,'add_clientefisico'),(23,'Can change cliente fisico',8,'change_clientefisico'),(24,'Can delete cliente fisico',8,'delete_clientefisico'),(25,'Can add cliente moral',9,'add_clientemoral'),(26,'Can change cliente moral',9,'change_clientemoral'),(27,'Can delete cliente moral',9,'delete_clientemoral'),(28,'Can add agente',10,'add_agente'),(29,'Can change agente',10,'change_agente'),(30,'Can delete agente',10,'delete_agente'),(31,'Can add administrador',11,'add_administrador'),(32,'Can change administrador',11,'change_administrador'),(33,'Can delete administrador',11,'delete_administrador'),(34,'Can add tipo seguro',12,'add_tiposeguro'),(35,'Can change tipo seguro',12,'change_tiposeguro'),(36,'Can delete tipo seguro',12,'delete_tiposeguro'),(37,'Can add aseguradora',13,'add_aseguradora'),(38,'Can change aseguradora',13,'change_aseguradora'),(39,'Can delete aseguradora',13,'delete_aseguradora'),(40,'Can add comparativa',14,'add_comparativa'),(41,'Can change comparativa',14,'change_comparativa'),(42,'Can delete comparativa',14,'delete_comparativa'),(43,'Can add cotizacion',15,'add_cotizacion'),(44,'Can change cotizacion',15,'change_cotizacion'),(45,'Can delete cotizacion',15,'delete_cotizacion'),(46,'Can add area tramites',16,'add_areatramites'),(47,'Can change area tramites',16,'change_areatramites'),(48,'Can delete area tramites',16,'delete_areatramites'),(49,'Can add poliza',17,'add_poliza'),(50,'Can change poliza',17,'change_poliza'),(51,'Can delete poliza',17,'delete_poliza'),(52,'Can add pago',18,'add_pago'),(53,'Can change pago',18,'change_pago'),(54,'Can delete pago',18,'delete_pago'),(55,'Can add comision',19,'add_comision'),(56,'Can change comision',19,'change_comision'),(57,'Can delete comision',19,'delete_comision'),(58,'Can add asignacion comision',20,'add_asignacioncomision'),(59,'Can change asignacion comision',20,'change_asignacioncomision'),(60,'Can delete asignacion comision',20,'delete_asignacioncomision'),(61,'Can add contacto',21,'add_contacto'),(62,'Can change contacto',21,'change_contacto'),(63,'Can delete contacto',21,'delete_contacto'),(64,'Can add orden servicio',22,'add_ordenservicio'),(65,'Can change orden servicio',22,'change_ordenservicio'),(66,'Can delete orden servicio',22,'delete_ordenservicio'),(67,'Can add cobertura',23,'add_cobertura'),(68,'Can change cobertura',23,'change_cobertura'),(69,'Can delete cobertura',23,'delete_cobertura'),(70,'Can add cobertura utilizada',24,'add_coberturautilizada'),(71,'Can change cobertura utilizada',24,'change_coberturautilizada'),(72,'Can delete cobertura utilizada',24,'delete_coberturautilizada'),(73,'Can add seguro',25,'add_seguro'),(74,'Can change seguro',25,'change_seguro'),(75,'Can delete seguro',25,'delete_seguro'),(76,'Can add seguro ap',26,'add_seguroap'),(77,'Can change seguro ap',26,'change_seguroap'),(78,'Can delete seguro ap',26,'delete_seguroap'),(79,'Can add seguro c',27,'add_seguroc'),(80,'Can change seguro c',27,'change_seguroc'),(81,'Can delete seguro c',27,'delete_seguroc'),(82,'Can add seguro r',28,'add_seguror'),(83,'Can change seguro r',28,'change_seguror'),(84,'Can delete seguro r',28,'delete_seguror'),(85,'Can add seguro g',29,'add_segurog'),(86,'Can change seguro g',29,'change_segurog'),(87,'Can delete seguro g',29,'delete_segurog'),(88,'Can add seguro v',30,'add_segurov'),(89,'Can change seguro v',30,'change_segurov'),(90,'Can delete seguro v',30,'delete_segurov'),(91,'Can add seguro h',31,'add_seguroh'),(92,'Can change seguro h',31,'change_seguroh'),(93,'Can delete seguro h',31,'delete_seguroh'),(94,'Can add seguro i',32,'add_seguroi'),(95,'Can change seguro i',32,'change_seguroi'),(96,'Can delete seguro i',32,'delete_seguroi'),(97,'Can add seguro e',33,'add_seguroe'),(98,'Can change seguro e',33,'change_seguroe'),(99,'Can delete seguro e',33,'delete_seguroe'),(100,'Can add seguro ec',34,'add_seguroec'),(101,'Can change seguro ec',34,'change_seguroec'),(102,'Can delete seguro ec',34,'delete_seguroec'),(103,'Can add seguro t',35,'add_segurot'),(104,'Can change seguro t',35,'change_segurot'),(105,'Can delete seguro t',35,'delete_segurot');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$7499PMrEfIvM$yRPGKSIK/Wahq4HqZ5tSL2aNrQ4Is25muAtFDC2aXzY=','2015-11-21 22:52:15',0,'ivanalejandro','Ivan','Soto','ivanali@outlook.com',0,1,'2015-11-21 18:11:40'),(2,'pbkdf2_sha256$20000$zkiP2FHVSqen$d8Yq7C8t9B9TD4uecK7EBBXqzIbmQ/It4h0b15pAn2o=',NULL,0,'squgus','Gustavo','Gutierrez','squgus@gmail.com',0,1,'2015-11-21 18:11:40'),(3,'pbkdf2_sha256$20000$AM5y6WgP9pnV$vmGckegwUetC2LHXpIzjdkBwOSeoiM76WkPMNQbCW24=','2015-11-21 22:44:54',0,'joaquintech','Joaquin','Gutierrez','joaquin_tech@hotmail.com',0,1,'2015-11-21 22:44:27');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_4f245a34_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_4f245a34_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_36564d86_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1),(2,2,1),(3,3,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3c78c3bf_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_1661f213_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3c78c3bf_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_3a2a2a22_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_5703792b_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_5703792b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_3a2a2a22_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_74683724_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'schema','administrador'),(10,'schema','agente'),(16,'schema','areatramites'),(13,'schema','aseguradora'),(20,'schema','asignacioncomision'),(7,'schema','cliente'),(8,'schema','clientefisico'),(9,'schema','clientemoral'),(23,'schema','cobertura'),(24,'schema','coberturautilizada'),(19,'schema','comision'),(14,'schema','comparativa'),(21,'schema','contacto'),(15,'schema','cotizacion'),(22,'schema','ordenservicio'),(18,'schema','pago'),(17,'schema','poliza'),(25,'schema','seguro'),(26,'schema','seguroap'),(27,'schema','seguroc'),(33,'schema','seguroe'),(34,'schema','seguroec'),(29,'schema','segurog'),(31,'schema','seguroh'),(32,'schema','seguroi'),(28,'schema','seguror'),(35,'schema','segurot'),(30,'schema','segurov'),(12,'schema','tiposeguro'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-11-21 18:10:51'),(2,'auth','0001_initial','2015-11-21 18:10:53'),(3,'admin','0001_initial','2015-11-21 18:10:53'),(4,'contenttypes','0002_remove_content_type_name','2015-11-21 18:10:53'),(5,'auth','0002_alter_permission_name_max_length','2015-11-21 18:10:54'),(6,'auth','0003_alter_user_email_max_length','2015-11-21 18:10:54'),(7,'auth','0004_alter_user_username_opts','2015-11-21 18:10:54'),(8,'auth','0005_alter_user_last_login_null','2015-11-21 18:10:54'),(9,'auth','0006_require_contenttypes_0002','2015-11-21 18:10:54'),(10,'schema','0001_initial','2015-11-21 18:11:05'),(11,'schema','0002_auto_20151111_1811','2015-11-21 18:11:06'),(12,'schema','0003_auto_20151111_1832','2015-11-21 18:11:06'),(13,'schema','0004_auto_20151111_1846','2015-11-21 18:11:06'),(14,'schema','0005_auto_20151111_2001','2015-11-21 18:11:07'),(15,'schema','0006_auto_20151111_2032','2015-11-21 18:11:07'),(16,'schema','0007_auto_20151117_1530','2015-11-21 18:11:14'),(17,'schema','0008_auto_20151117_1601','2015-11-21 18:11:14'),(18,'schema','0009_auto_20151117_1633','2015-11-21 18:11:15'),(19,'schema','0010_auto_20151117_1752','2015-11-21 18:11:20'),(20,'schema','0011_auto_20151119_1443','2015-11-21 18:11:28'),(21,'schema','0012_auto_20151119_1623','2015-11-21 18:11:28'),(22,'schema','0013_cotizacion_archivo','2015-11-21 18:11:28'),(23,'schema','0014_auto_20151120_1055','2015-11-21 18:11:29'),(24,'schema','0015_auto_20151120_1937','2015-11-21 18:11:29'),(25,'schema','0016_areatramites','2015-11-21 18:11:30'),(26,'schema','0017_ordenservicio_agente','2015-11-21 18:11:31'),(27,'sessions','0001_initial','2015-11-21 18:11:31'),(28,'schema','0018_auto_20151121_1732','2015-11-21 23:32:30'),(29,'schema','0019_auto_20151121_1830','2015-11-22 00:30:58'),(30,'schema','0020_auto_20151121_1839','2015-11-22 00:40:01'),(31,'schema','0021_auto_20151121_1840','2015-11-22 00:40:56'),(32,'schema','0022_poliza_nopoliza','2015-11-22 19:23:26'),(33,'schema','0023_auto_20151122_1324','2015-11-22 19:24:12'),(34,'schema','0024_auto_20151122_1536','2015-11-22 21:36:27');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('m6dl9lecnss4r6jdmjx9s8y4yhk0twlv','MDcwYTgzNWZmNWRmMzEyNmJhYzBiMjg0NmJjMGZlMGMyYjczNGExZjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUzOTg3Yjc4ZjgyNzA2ZjYxMWVhOTQ4NGY3MDU4YTM0MDQ5MzY1MWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-12-05 22:52:15');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_administrador`
--

DROP TABLE IF EXISTS `schema_administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_administrador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `edad` smallint(5) unsigned DEFAULT NULL,
  `sexo` varchar(1) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `telefonoLada` varchar(3) NOT NULL,
  `telefono` varchar(7) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `numeroExt` smallint(5) unsigned DEFAULT NULL,
  `numeroInt` smallint(5) unsigned DEFAULT NULL,
  `colonia` varchar(40) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `estado` varchar(19) NOT NULL,
  `codigoPostal` varchar(5) NOT NULL,
  `userAdmin_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userAdmin_id` (`userAdmin_id`),
  CONSTRAINT `schema_administrador_userAdmin_id_758490b5_fk_auth_user_id` FOREIGN KEY (`userAdmin_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_administrador`
--

LOCK TABLES `schema_administrador` WRITE;
/*!40000 ALTER TABLE `schema_administrador` DISABLE KEYS */;
INSERT INTO `schema_administrador` VALUES (1,'',NULL,'','','','','',NULL,NULL,'','','','',3);
/*!40000 ALTER TABLE `schema_administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_agente`
--

DROP TABLE IF EXISTS `schema_agente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_agente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `edad` smallint(5) unsigned DEFAULT NULL,
  `sexo` varchar(1) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `telefonoLada` varchar(3) NOT NULL,
  `telefono` varchar(7) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `numeroExt` smallint(5) unsigned DEFAULT NULL,
  `numeroInt` smallint(5) unsigned DEFAULT NULL,
  `colonia` varchar(40) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `estado` varchar(19) NOT NULL,
  `codigoPostal` varchar(5) NOT NULL,
  `claveAgente` int(11) DEFAULT NULL,
  `cuentaBancaria` varchar(34) NOT NULL,
  `banco` varchar(30) NOT NULL,
  `userAgente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userAgente_id` (`userAgente_id`),
  CONSTRAINT `schema_agente_userAgente_id_290e2091_fk_auth_user_id` FOREIGN KEY (`userAgente_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_agente`
--

LOCK TABLES `schema_agente` WRITE;
/*!40000 ALTER TABLE `schema_agente` DISABLE KEYS */;
INSERT INTO `schema_agente` VALUES (1,'',NULL,'','','','','',NULL,NULL,'','','','',12345,'','',1),(2,'',NULL,'','','','','',NULL,NULL,'','','','',666,'','',2);
/*!40000 ALTER TABLE `schema_agente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_agente_clientes`
--

DROP TABLE IF EXISTS `schema_agente_clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_agente_clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agente_id` int(11) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agente_id` (`agente_id`,`cliente_id`),
  KEY `schema_agente_cl_cliente_id_3f9e98fe_fk_schema_cliente_idCliente` (`cliente_id`),
  CONSTRAINT `schema_agente_clientes_agente_id_65e6e7bb_fk_schema_agente_id` FOREIGN KEY (`agente_id`) REFERENCES `schema_agente` (`id`),
  CONSTRAINT `schema_agente_cl_cliente_id_3f9e98fe_fk_schema_cliente_idCliente` FOREIGN KEY (`cliente_id`) REFERENCES `schema_cliente` (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_agente_clientes`
--

LOCK TABLES `schema_agente_clientes` WRITE;
/*!40000 ALTER TABLE `schema_agente_clientes` DISABLE KEYS */;
INSERT INTO `schema_agente_clientes` VALUES (1,1,1),(2,1,2),(3,1,3);
/*!40000 ALTER TABLE `schema_agente_clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_areatramites`
--

DROP TABLE IF EXISTS `schema_areatramites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_areatramites` (
  `idAreaTramites` int(11) NOT NULL AUTO_INCREMENT,
  `encargado` varchar(60) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`idAreaTramites`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_areatramites`
--

LOCK TABLES `schema_areatramites` WRITE;
/*!40000 ALTER TABLE `schema_areatramites` DISABLE KEYS */;
INSERT INTO `schema_areatramites` VALUES (1,'Ivan Alejandro Soto Velazquez','ivanali@outlook.com');
/*!40000 ALTER TABLE `schema_areatramites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_aseguradora`
--

DROP TABLE IF EXISTS `schema_aseguradora`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_aseguradora` (
  `idAseguradora` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `sitioWeb` varchar(200) DEFAULT NULL,
  `telefonoLada` varchar(3) NOT NULL,
  `telefono` varchar(7) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `numeroExt` smallint(5) unsigned NOT NULL,
  `numeroInt` smallint(5) unsigned DEFAULT NULL,
  `colonia` varchar(40) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `estado` varchar(19) NOT NULL,
  `codigoPostal` varchar(5) NOT NULL,
  PRIMARY KEY (`idAseguradora`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_aseguradora`
--

LOCK TABLES `schema_aseguradora` WRITE;
/*!40000 ALTER TABLE `schema_aseguradora` DISABLE KEYS */;
INSERT INTO `schema_aseguradora` VALUES (1,'GNP Seguros','http://www.gnp.com.mx','442','1234567','Rainbow',1234,NULL,'asdf','Queretaro','Queretaro','54321'),(2,'Seguros Potosi','http://www.segurospotosi.com.mx','442','1234567','Rainbow',1234,NULL,'asdf','Queretaro','Queretaro','54321'),(3,'MAPFRE','http://www.mapfre.com.mx','442','1234567','Rainbow',1234,NULL,'asdf','Queretaro','Queretaro','54321');
/*!40000 ALTER TABLE `schema_aseguradora` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_aseguradora_seguros`
--

DROP TABLE IF EXISTS `schema_aseguradora_seguros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_aseguradora_seguros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aseguradora_id` int(11) NOT NULL,
  `tiposeguro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aseguradora_id` (`aseguradora_id`,`tiposeguro_id`),
  KEY `schema__tiposeguro_id_63f528f4_fk_schema_tiposeguro_idTipoSeguro` (`tiposeguro_id`),
  CONSTRAINT `schema__tiposeguro_id_63f528f4_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tiposeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`),
  CONSTRAINT `sche_aseguradora_id_14372198_fk_schema_aseguradora_idAseguradora` FOREIGN KEY (`aseguradora_id`) REFERENCES `schema_aseguradora` (`idAseguradora`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_aseguradora_seguros`
--

LOCK TABLES `schema_aseguradora_seguros` WRITE;
/*!40000 ALTER TABLE `schema_aseguradora_seguros` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_aseguradora_seguros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_asignacioncomision`
--

DROP TABLE IF EXISTS `schema_asignacioncomision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_asignacioncomision` (
  `idAsignacion` int(11) NOT NULL AUTO_INCREMENT,
  `fechaAsignacion` datetime NOT NULL,
  `porcentaje` decimal(4,2) NOT NULL,
  `aseguradora_id` int(11) NOT NULL,
  `tipoSeguro_id` int(11) NOT NULL,
  PRIMARY KEY (`idAsignacion`),
  KEY `sche_aseguradora_id_6bc1c657_fk_schema_aseguradora_idAseguradora` (`aseguradora_id`),
  KEY `schema_asignacioncomision_36643dd4` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_1842d97f_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`),
  CONSTRAINT `sche_aseguradora_id_6bc1c657_fk_schema_aseguradora_idAseguradora` FOREIGN KEY (`aseguradora_id`) REFERENCES `schema_aseguradora` (`idAseguradora`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_asignacioncomision`
--

LOCK TABLES `schema_asignacioncomision` WRITE;
/*!40000 ALTER TABLE `schema_asignacioncomision` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_asignacioncomision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_cliente`
--

DROP TABLE IF EXISTS `schema_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_cliente` (
  `email` varchar(254) NOT NULL,
  `edad` smallint(5) unsigned DEFAULT NULL,
  `sexo` varchar(1) NOT NULL,
  `rfc` varchar(13) NOT NULL,
  `telefonoLada` varchar(3) NOT NULL,
  `telefono` varchar(7) NOT NULL,
  `calle` varchar(50) NOT NULL,
  `numeroExt` smallint(5) unsigned DEFAULT NULL,
  `numeroInt` smallint(5) unsigned DEFAULT NULL,
  `colonia` varchar(40) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `estado` varchar(19) NOT NULL,
  `codigoPostal` varchar(5) NOT NULL,
  `idCliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `apellidoPaterno` varchar(30) NOT NULL,
  `apellidoMaterno` varchar(30) NOT NULL,
  `linkRegistroRFC` varchar(200) DEFAULT NULL,
  `linkComprobanteDomicilio` varchar(200) DEFAULT NULL,
  `calleFact` varchar(50) NOT NULL,
  `numeroExtFact` smallint(5) unsigned DEFAULT NULL,
  `numeroIntFact` smallint(5) unsigned DEFAULT NULL,
  `coloniaFact` varchar(40) NOT NULL,
  `ciudadFact` varchar(30) NOT NULL,
  `estadoFact` varchar(19) NOT NULL,
  `codigoPostalFact` varchar(5) NOT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_cliente`
--

LOCK TABLES `schema_cliente` WRITE;
/*!40000 ALTER TABLE `schema_cliente` DISABLE KEYS */;
INSERT INTO `schema_cliente` VALUES ('gerchez93@gmail.com',22,'H','GORM931232323','477','7152032','',NULL,NULL,'','','','',1,'Gerardo','Garcia','Sanchez',NULL,NULL,'',NULL,NULL,'','','',''),('ivanali@outlook.com',20,'H','SOVI','644','1421909','',NULL,NULL,'','','','',2,'Ivan Alejandro','Soto','Velazquez',NULL,NULL,'',NULL,NULL,'','','',''),('squgus@gmail.com',21,'H','GUSASDADAD','422','1234567','Porahi',109,NULL,'Nolose','Morelia','Michoacan','37150',3,'Gustavo','Gutierrez','Gomez',NULL,NULL,'',NULL,NULL,'','','','');
/*!40000 ALTER TABLE `schema_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_clienteagente`
--

DROP TABLE IF EXISTS `schema_clienteagente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_clienteagente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_clienteagente`
--

LOCK TABLES `schema_clienteagente` WRITE;
/*!40000 ALTER TABLE `schema_clienteagente` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_clienteagente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_clientefisico`
--

DROP TABLE IF EXISTS `schema_clientefisico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_clientefisico` (
  `cliente_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`cliente_ptr_id`),
  CONSTRAINT `schema_clien_cliente_ptr_id_19ed98ef_fk_schema_cliente_idCliente` FOREIGN KEY (`cliente_ptr_id`) REFERENCES `schema_cliente` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_clientefisico`
--

LOCK TABLES `schema_clientefisico` WRITE;
/*!40000 ALTER TABLE `schema_clientefisico` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_clientefisico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_clientemoral`
--

DROP TABLE IF EXISTS `schema_clientemoral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_clientemoral` (
  `cliente_ptr_id` int(11) NOT NULL,
  `razonSocial` varchar(100) DEFAULT NULL,
  `linkActaConstitutiva` varchar(200) DEFAULT NULL,
  `linkIdRepresentante` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`cliente_ptr_id`),
  CONSTRAINT `schema_clien_cliente_ptr_id_46407e9f_fk_schema_cliente_idCliente` FOREIGN KEY (`cliente_ptr_id`) REFERENCES `schema_cliente` (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_clientemoral`
--

LOCK TABLES `schema_clientemoral` WRITE;
/*!40000 ALTER TABLE `schema_clientemoral` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_clientemoral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_cobertura`
--

DROP TABLE IF EXISTS `schema_cobertura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_cobertura` (
  `idCobertura` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `seguro_id` varchar(3),
  PRIMARY KEY (`idCobertura`),
  KEY `schema_cobertura_1d8c034f` (`seguro_id`),
  CONSTRAINT `schema_cobertura_seguro_id_54ace9c6_fk_schema_seguro_idSeguro` FOREIGN KEY (`seguro_id`) REFERENCES `schema_seguro` (`idSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_cobertura`
--

LOCK TABLES `schema_cobertura` WRITE;
/*!40000 ALTER TABLE `schema_cobertura` DISABLE KEYS */;
INSERT INTO `schema_cobertura` VALUES (1,'Danos materiales','AP'),(2,'Exencion de deducible por perdida total','AP'),(3,'Deducible cero en robo total','AP'),(4,'Responsabilidad civil danos a bienes y personas','AP'),(5,'Robo parcial','AP'),(6,'Gastos medicos ocupantes','AP'),(7,'Danos materiales','C'),(8,'Exencion de deducible por perdida total','C'),(9,'Deducible cero en robo total','C'),(10,'Responsabilidad civil danos a bienes y personas','C'),(11,'Robo parcial','C'),(12,'Gastos medicos ocupantes','C'),(13,'Emergencias en el extranjero','G'),(14,'Cobertura en el extranjero','G'),(15,'Continuacion familiar','G'),(16,'Incendio/rayo','E'),(17,'Huracan','E'),(18,'Extension de cubierta','E'),(19,'Terremoto','E'),(20,'Explosion','E'),(21,'Objetos caidos de aviones','E'),(22,'Huelgas y alborotos populares','E');
/*!40000 ALTER TABLE `schema_cobertura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_coberturautilizada`
--

DROP TABLE IF EXISTS `schema_coberturautilizada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_coberturautilizada` (
  `idCoberturaUtilizada` int(11) NOT NULL AUTO_INCREMENT,
  `sumaAsegurada` varchar(30) NOT NULL,
  `deducible` decimal(4,2) NOT NULL,
  `cotizacion_id` int(11),
  `idCobertura_id` int(11) NOT NULL,
  PRIMARY KEY (`idCoberturaUtilizada`),
  KEY `schema_coberturautilizada_1b44b901` (`cotizacion_id`),
  KEY `schema_coberturautilizada_7fcb3e0a` (`idCobertura_id`),
  CONSTRAINT `schema_c_cotizacion_id_8e862a8_fk_schema_cotizacion_idCotizacion` FOREIGN KEY (`cotizacion_id`) REFERENCES `schema_cotizacion` (`idCotizacion`),
  CONSTRAINT `schema_c_idCobertura_id_1d4ddf8c_fk_schema_cobertura_idCobertura` FOREIGN KEY (`idCobertura_id`) REFERENCES `schema_cobertura` (`idCobertura`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_coberturautilizada`
--

LOCK TABLES `schema_coberturautilizada` WRITE;
/*!40000 ALTER TABLE `schema_coberturautilizada` DISABLE KEYS */;
INSERT INTO `schema_coberturautilizada` VALUES (1,'123',6.00,1,2),(2,'20',3.00,2,3),(3,'456',4.00,3,19);
/*!40000 ALTER TABLE `schema_coberturautilizada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_comision`
--

DROP TABLE IF EXISTS `schema_comision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_comision` (
  `idComision` int(11) NOT NULL AUTO_INCREMENT,
  `cantidadComision` decimal(11,2) NOT NULL,
  `fechaDeposito` datetime DEFAULT NULL,
  `agente_id` int(11) NOT NULL,
  `asignacionComision_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`idComision`),
  KEY `schema_comision_agente_id_3a3b7f5d_fk_schema_agente_id` (`agente_id`),
  KEY `D81da41381d64ad537e4e908a2b89203` (`asignacionComision_id`),
  CONSTRAINT `D81da41381d64ad537e4e908a2b89203` FOREIGN KEY (`asignacionComision_id`) REFERENCES `schema_asignacioncomision` (`idAsignacion`),
  CONSTRAINT `schema_comision_agente_id_3a3b7f5d_fk_schema_agente_id` FOREIGN KEY (`agente_id`) REFERENCES `schema_agente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_comision`
--

LOCK TABLES `schema_comision` WRITE;
/*!40000 ALTER TABLE `schema_comision` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_comision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_comparativa`
--

DROP TABLE IF EXISTS `schema_comparativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_comparativa` (
  `idComparativa` int(11) NOT NULL AUTO_INCREMENT,
  `fechaCreacion` datetime NOT NULL,
  `fechaConclusion` datetime DEFAULT NULL,
  `tipoSeguro_id` int(11) NOT NULL,
  `fechaEnvioCliente` datetime,
  `fechaEnvioTramite` datetime,
  PRIMARY KEY (`idComparativa`),
  KEY `schema_comparativa_36643dd4` (`tipoSeguro_id`),
  CONSTRAINT `schema_c_tipoSeguro_id_ffd6dcb_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_comparativa`
--

LOCK TABLES `schema_comparativa` WRITE;
/*!40000 ALTER TABLE `schema_comparativa` DISABLE KEYS */;
INSERT INTO `schema_comparativa` VALUES (1,'2015-11-21 18:18:17','2015-11-22 18:28:31',1,NULL,'2015-11-21 23:45:02'),(2,'2015-11-21 18:49:36',NULL,2,NULL,NULL),(3,'2015-11-21 18:50:29',NULL,3,NULL,NULL),(4,'2015-11-21 18:50:58',NULL,4,NULL,NULL),(5,'2015-11-21 18:55:06','2015-11-21 19:53:53',5,NULL,NULL),(6,'2015-11-22 00:19:08','2015-11-22 00:21:40',6,NULL,'2015-11-22 00:20:21');
/*!40000 ALTER TABLE `schema_comparativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_comparativa_coberturas`
--

DROP TABLE IF EXISTS `schema_comparativa_coberturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_comparativa_coberturas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comparativa_id` int(11) NOT NULL,
  `cobertura_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `comparativa_id` (`comparativa_id`,`cobertura_id`),
  KEY `schema_com_cobertura_id_4f9d6c25_fk_schema_cobertura_idCobertura` (`cobertura_id`),
  CONSTRAINT `schema_com_cobertura_id_4f9d6c25_fk_schema_cobertura_idCobertura` FOREIGN KEY (`cobertura_id`) REFERENCES `schema_cobertura` (`idCobertura`),
  CONSTRAINT `sche_comparativa_id_1ba9ff45_fk_schema_comparativa_idComparativa` FOREIGN KEY (`comparativa_id`) REFERENCES `schema_comparativa` (`idComparativa`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_comparativa_coberturas`
--

LOCK TABLES `schema_comparativa_coberturas` WRITE;
/*!40000 ALTER TABLE `schema_comparativa_coberturas` DISABLE KEYS */;
INSERT INTO `schema_comparativa_coberturas` VALUES (1,1,1),(2,1,3),(3,1,4),(4,3,4),(5,4,4),(6,6,16),(7,6,18),(8,6,19);
/*!40000 ALTER TABLE `schema_comparativa_coberturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_contacto`
--

DROP TABLE IF EXISTS `schema_contacto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_contacto` (
  `idContacto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `apellidoPaterno` varchar(30) NOT NULL,
  `apellidoMaterno` varchar(30) NOT NULL,
  `email` varchar(254) DEFAULT NULL,
  `telefonoLada` varchar(3) NOT NULL,
  `telefono` varchar(7) NOT NULL,
  `aseguradora_id` int(11) NOT NULL,
  PRIMARY KEY (`idContacto`),
  KEY `sche_aseguradora_id_27034f66_fk_schema_aseguradora_idAseguradora` (`aseguradora_id`),
  CONSTRAINT `sche_aseguradora_id_27034f66_fk_schema_aseguradora_idAseguradora` FOREIGN KEY (`aseguradora_id`) REFERENCES `schema_aseguradora` (`idAseguradora`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_contacto`
--

LOCK TABLES `schema_contacto` WRITE;
/*!40000 ALTER TABLE `schema_contacto` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_contacto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_cotizacion`
--

DROP TABLE IF EXISTS `schema_cotizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_cotizacion` (
  `idCotizacion` int(11) NOT NULL AUTO_INCREMENT,
  `costo` decimal(11,2) NOT NULL,
  `fechaCreacion` datetime NOT NULL,
  `formaPago` int(11) NOT NULL,
  `aseguradora_id` int(11) NOT NULL,
  `comparativa_id` int(11) DEFAULT NULL,
  `archivo` varchar(100),
  `elegida` tinyint(1) NOT NULL,
  PRIMARY KEY (`idCotizacion`),
  KEY `sche_aseguradora_id_7d21369d_fk_schema_aseguradora_idAseguradora` (`aseguradora_id`),
  KEY `schem_comparativa_id_c0bd213_fk_schema_comparativa_idComparativa` (`comparativa_id`),
  CONSTRAINT `schem_comparativa_id_c0bd213_fk_schema_comparativa_idComparativa` FOREIGN KEY (`comparativa_id`) REFERENCES `schema_comparativa` (`idComparativa`),
  CONSTRAINT `sche_aseguradora_id_7d21369d_fk_schema_aseguradora_idAseguradora` FOREIGN KEY (`aseguradora_id`) REFERENCES `schema_aseguradora` (`idAseguradora`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_cotizacion`
--

LOCK TABLES `schema_cotizacion` WRITE;
/*!40000 ALTER TABLE `schema_cotizacion` DISABLE KEYS */;
INSERT INTO `schema_cotizacion` VALUES (1,666.00,'2015-11-21 18:21:51',1,1,1,'./2_IYkNadj.png',1),(2,456.00,'2015-11-21 18:23:22',1,2,1,'./1-e1c8d63667_r8INcRq.jpg',0),(3,456.00,'2015-11-22 00:19:45',2,3,6,'./1-e1c8d63667_rUhRlL4.jpg',1);
/*!40000 ALTER TABLE `schema_cotizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_ordenservicio`
--

DROP TABLE IF EXISTS `schema_ordenservicio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_ordenservicio` (
  `idServicio` int(11) NOT NULL AUTO_INCREMENT,
  `fechaServicio` datetime NOT NULL,
  `fechaConclusion` datetime DEFAULT NULL,
  `cliente_id` int(11) NOT NULL,
  `comparativa_id` int(11),
  `agente_id` int(11),
  PRIMARY KEY (`idServicio`),
  UNIQUE KEY `comparativa_id` (`comparativa_id`),
  KEY `schema_ordenservicio_4a860110` (`cliente_id`),
  KEY `schema_ordenservicio_32400660` (`agente_id`),
  CONSTRAINT `schema_ordenservicio_agente_id_1050d91_fk_schema_agente_id` FOREIGN KEY (`agente_id`) REFERENCES `schema_agente` (`id`),
  CONSTRAINT `schema_ordenservi_cliente_id_4fbd612_fk_schema_cliente_idCliente` FOREIGN KEY (`cliente_id`) REFERENCES `schema_cliente` (`idCliente`),
  CONSTRAINT `sche_comparativa_id_6b02642c_fk_schema_comparativa_idComparativa` FOREIGN KEY (`comparativa_id`) REFERENCES `schema_comparativa` (`idComparativa`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_ordenservicio`
--

LOCK TABLES `schema_ordenservicio` WRITE;
/*!40000 ALTER TABLE `schema_ordenservicio` DISABLE KEYS */;
INSERT INTO `schema_ordenservicio` VALUES (1,'2015-11-21 18:18:18',NULL,1,1,1),(2,'2015-11-21 18:50:59',NULL,1,4,1),(3,'2015-11-21 18:55:06',NULL,1,5,1),(4,'2015-11-22 00:19:09',NULL,3,6,1);
/*!40000 ALTER TABLE `schema_ordenservicio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_pago`
--

DROP TABLE IF EXISTS `schema_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_pago` (
  `idPago` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad` decimal(11,2) NOT NULL,
  `fechaPago` datetime NOT NULL,
  `numeroPago` smallint(5) unsigned NOT NULL,
  `poliza_id` int(11) NOT NULL,
  `comprobante` varchar(100),
  PRIMARY KEY (`idPago`),
  KEY `schema_pago_2cc6c735` (`poliza_id`),
  CONSTRAINT `schema_pago_poliza_id_7d7583cd_fk_schema_poliza_idPoliza` FOREIGN KEY (`poliza_id`) REFERENCES `schema_poliza` (`idPoliza`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_pago`
--

LOCK TABLES `schema_pago` WRITE;
/*!40000 ALTER TABLE `schema_pago` DISABLE KEYS */;
INSERT INTO `schema_pago` VALUES (3,123.00,'2015-11-22 06:00:00',1,1,'./1-e1c8d63667_Uiclf35.jpg');
/*!40000 ALTER TABLE `schema_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_poliza`
--

DROP TABLE IF EXISTS `schema_poliza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_poliza` (
  `idPoliza` int(11) NOT NULL AUTO_INCREMENT,
  `primaNeta` decimal(11,2) NOT NULL,
  `fechaEmision` datetime NOT NULL,
  `fechaInicio` datetime NOT NULL,
  `fechaFin` datetime DEFAULT NULL,
  `endosoBeneficiario` varchar(100) NOT NULL,
  `comision_id` int(11) DEFAULT NULL,
  `cotizacion_id` int(11) DEFAULT NULL,
  `ordenServicio_id` int(11) DEFAULT NULL,
  `caratulaPDF` varchar(100),
  `noPoliza` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`idPoliza`),
  UNIQUE KEY `ordenServicio_id` (`ordenServicio_id`),
  UNIQUE KEY `cotizacion_id` (`cotizacion_id`),
  UNIQUE KEY `comision_id` (`comision_id`),
  CONSTRAINT `schema_poliza_comision_id_26e3acf6_fk_schema_comision_idComision` FOREIGN KEY (`comision_id`) REFERENCES `schema_comision` (`idComision`),
  CONSTRAINT `schema__cotizacion_id_49ed3b11_fk_schema_cotizacion_idCotizacion` FOREIGN KEY (`cotizacion_id`) REFERENCES `schema_cotizacion` (`idCotizacion`),
  CONSTRAINT `sch_ordenServicio_id_4ea8e11b_fk_schema_ordenservicio_idServicio` FOREIGN KEY (`ordenServicio_id`) REFERENCES `schema_ordenservicio` (`idServicio`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_poliza`
--

LOCK TABLES `schema_poliza` WRITE;
/*!40000 ALTER TABLE `schema_poliza` DISABLE KEYS */;
INSERT INTO `schema_poliza` VALUES (1,123.00,'2015-11-21 06:00:00','2015-11-21 06:00:00',NULL,'Mi persona',NULL,2,4,'./1-e1c8d63667_D9MbxnP.jpg',NULL);
/*!40000 ALTER TABLE `schema_poliza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguro`
--

DROP TABLE IF EXISTS `schema_seguro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguro` (
  `idSeguro` varchar(3) NOT NULL,
  `nombre` varchar(80) NOT NULL,
  PRIMARY KEY (`idSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguro`
--

LOCK TABLES `schema_seguro` WRITE;
/*!40000 ALTER TABLE `schema_seguro` DISABLE KEYS */;
INSERT INTO `schema_seguro` VALUES ('AP','Automóviles y pickups'),('C','Camiones'),('E','Empresas'),('EC','Equipo de contratistas'),('G','Gastos médicos mayores'),('H','Hogares'),('I','Inversiones'),('R','Remolques, cajas secas y adaptaciones en general'),('T','Transportes'),('V','Vida');
/*!40000 ALTER TABLE `schema_seguro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroap`
--

DROP TABLE IF EXISTS `schema_seguroap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroap` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(30) DEFAULT NULL,
  `modelo` varchar(30) DEFAULT NULL,
  `tipoPlan` varchar(50) NOT NULL,
  `ano` smallint(5) unsigned DEFAULT NULL,
  `descripcion` longtext,
  `pasajeros` smallint(5) unsigned DEFAULT NULL,
  `estadoCirculacion` varchar(19) DEFAULT NULL,
  `version` varchar(10) NOT NULL,
  `transmision` varchar(1) DEFAULT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_537c42c6_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroap`
--

LOCK TABLES `schema_seguroap` WRITE;
/*!40000 ALTER TABLE `schema_seguroap` DISABLE KEYS */;
INSERT INTO `schema_seguroap` VALUES (1,'Chevrolet','Focus','VIP',2006,'BBB',3,'Sonora','','A',1),(2,'Chevy','Focus','',NULL,'',NULL,'','',NULL,2),(3,'Chevy','Focus','',NULL,'',NULL,'','',NULL,3),(4,'Chevy','Focus','',NULL,'',NULL,'','',NULL,4);
/*!40000 ALTER TABLE `schema_seguroap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroc`
--

DROP TABLE IF EXISTS `schema_seguroc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroc` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `marca` varchar(30) DEFAULT NULL,
  `modelo` varchar(30) DEFAULT NULL,
  `ano` smallint(5) unsigned DEFAULT NULL,
  `descripcion` longtext,
  `pasajeros` smallint(5) unsigned DEFAULT NULL,
  `unidad` smallint(5) unsigned NOT NULL,
  `transmision` varchar(1) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_7a042190_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroc`
--

LOCK TABLES `schema_seguroc` WRITE;
/*!40000 ALTER TABLE `schema_seguroc` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_seguroc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroe`
--

DROP TABLE IF EXISTS `schema_seguroe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroe` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `nombreEmpresa` varchar(50) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `tipoMuro` varchar(30) NOT NULL,
  `tipoConstruccion` varchar(30) NOT NULL,
  `numeroPisos` smallint(5) unsigned NOT NULL,
  `numeroSotanos` smallint(5) unsigned NOT NULL,
  `numeroExt` smallint(5) unsigned DEFAULT NULL,
  `numeroInt` smallint(5) unsigned DEFAULT NULL,
  `colonia` varchar(40) NOT NULL,
  `ciudad` varchar(30) NOT NULL,
  `estado` varchar(19) NOT NULL,
  `codigoPostal` varchar(5) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_4f1ef3c2_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroe`
--

LOCK TABLES `schema_seguroe` WRITE;
/*!40000 ALTER TABLE `schema_seguroe` DISABLE KEYS */;
INSERT INTO `schema_seguroe` VALUES (1,'Nintendo','Japan','Chido','Videojuegos',10,10,123,321,'Midori','Tokyo','Japan','12345',6);
/*!40000 ALTER TABLE `schema_seguroe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroec`
--

DROP TABLE IF EXISTS `schema_seguroec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroec` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `tipoEquipo` varchar(30) NOT NULL,
  `caracteristicas` longtext NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_211da8e9_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroec`
--

LOCK TABLES `schema_seguroec` WRITE;
/*!40000 ALTER TABLE `schema_seguroec` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_seguroec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_segurog`
--

DROP TABLE IF EXISTS `schema_segurog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_segurog` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `nombreAsegurado` varchar(80) NOT NULL,
  `coaseguro` decimal(11,2) NOT NULL,
  `topeCoaseguro` decimal(11,2) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_415bd479_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_segurog`
--

LOCK TABLES `schema_segurog` WRITE;
/*!40000 ALTER TABLE `schema_segurog` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_segurog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroh`
--

DROP TABLE IF EXISTS `schema_seguroh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroh` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `codigoPostal` varchar(5) NOT NULL,
  `tipoVivienda` varchar(50) NOT NULL,
  `primeraResidencia` tinyint(1) DEFAULT NULL,
  `metrosCuadrados` smallint(5) unsigned DEFAULT NULL,
  `capitalContinente` longtext NOT NULL,
  `capitalContenido` longtext NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_4b12b973_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroh`
--

LOCK TABLES `schema_seguroh` WRITE;
/*!40000 ALTER TABLE `schema_seguroh` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_seguroh` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguroi`
--

DROP TABLE IF EXISTS `schema_seguroi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguroi` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `sumaAsegurada` decimal(11,2) NOT NULL,
  `planAhorro` varchar(20) NOT NULL,
  `identificacion` varchar(200) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_785a2214_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguroi`
--

LOCK TABLES `schema_seguroi` WRITE;
/*!40000 ALTER TABLE `schema_seguroi` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_seguroi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_seguror`
--

DROP TABLE IF EXISTS `schema_seguror`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_seguror` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `capacidad` varchar(15) NOT NULL,
  `ejes` smallint(5) unsigned NOT NULL,
  `descripcion` longtext,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_1a7076c3_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_seguror`
--

LOCK TABLES `schema_seguror` WRITE;
/*!40000 ALTER TABLE `schema_seguror` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_seguror` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_segurot`
--

DROP TABLE IF EXISTS `schema_segurot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_segurot` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `tipoMedio` varchar(30) NOT NULL,
  `bienTransportado` varchar(40) NOT NULL,
  `sumaAsegurada` decimal(11,2) NOT NULL,
  `ciudadOrigen` varchar(31) NOT NULL,
  `estadoOrigen` varchar(19) NOT NULL,
  `ciudadDestino` varchar(31) NOT NULL,
  `estadoDestino` varchar(19) NOT NULL,
  `tipoTrabajo` varchar(20) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_179261b9_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_segurot`
--

LOCK TABLES `schema_segurot` WRITE;
/*!40000 ALTER TABLE `schema_segurot` DISABLE KEYS */;
INSERT INTO `schema_segurot` VALUES (1,'Auto','Libro',2000.00,'Leon','Guanajuato','Queretaro','Queretaro','Interesante',5);
/*!40000 ALTER TABLE `schema_segurot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_segurov`
--

DROP TABLE IF EXISTS `schema_segurov`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_segurov` (
  `idSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `nombreAsegurado` varchar(80) NOT NULL,
  `edad` smallint(5) unsigned DEFAULT NULL,
  `sexo` varchar(1) NOT NULL,
  `fumador` tinyint(1) NOT NULL,
  `link` varchar(200) NOT NULL,
  `tipoSeguro_id` int(11),
  PRIMARY KEY (`idSeguro`),
  UNIQUE KEY `tipoSeguro_id` (`tipoSeguro_id`),
  CONSTRAINT `schema__tipoSeguro_id_78bc0bf1_fk_schema_tiposeguro_idTipoSeguro` FOREIGN KEY (`tipoSeguro_id`) REFERENCES `schema_tiposeguro` (`idTipoSeguro`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_segurov`
--

LOCK TABLES `schema_segurov` WRITE;
/*!40000 ALTER TABLE `schema_segurov` DISABLE KEYS */;
/*!40000 ALTER TABLE `schema_segurov` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schema_tiposeguro`
--

DROP TABLE IF EXISTS `schema_tiposeguro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `schema_tiposeguro` (
  `idTipoSeguro` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_id` varchar(3),
  PRIMARY KEY (`idTipoSeguro`),
  KEY `schema_tiposeguro_1888d7ca` (`nombre_id`),
  CONSTRAINT `schema_tiposeguro_nombre_id_193ce1d6_fk_schema_seguro_idSeguro` FOREIGN KEY (`nombre_id`) REFERENCES `schema_seguro` (`idSeguro`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schema_tiposeguro`
--

LOCK TABLES `schema_tiposeguro` WRITE;
/*!40000 ALTER TABLE `schema_tiposeguro` DISABLE KEYS */;
INSERT INTO `schema_tiposeguro` VALUES (1,'AP'),(2,'AP'),(3,'AP'),(4,'AP'),(6,'E'),(5,'T');
/*!40000 ALTER TABLE `schema_tiposeguro` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-22 16:35:23
