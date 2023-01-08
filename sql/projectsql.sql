--- project database is used
USE project;

-- Creating users table
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ;

-- Inserting values into users table
INSERT INTO `users` VALUES (1,'Jeena Mathew','Hamilton'
,'jeen@gmail.com',1231231231,NULL);


-- Creating services table
CREATE TABLE `services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `check_in` datetime DEFAULT NULL,
  `service` char(20) DEFAULT NULL,
  `premium` char(20) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `FK_users` (`user_id`),
  CONSTRAINT `FK_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
);

-- Inserting data into services table
INSERT INTO `services` VALUES
(1,1,'2021-10-15 00:00:00','Motion Graphics','Yes',NULL);

-- Creating login table
CREATE TABLE `login` (
`userid` INT(11) DEFAULT NULL,
`username` varchar(15) NOT NULL,
`password` varchar(10) NOT NULL,
`sec_que` varchar(100) NULL,
`sec_ans` varchar(30) NULL,
`created_at` datetime DEFAULT current_timestamp(),
PRIMARY KEY (`username`),
KEY `FK_usersid` (`userid`),
CONSTRAINT `FK_usersid` FOREIGN KEY (`userid`) REFERENCES `users` (`id`) ON DELETE CASCADE )

-- Inserting data into login table
INSERT INTO `login` VALUES (1,'admin','admin@123', NULL, NULL,'2021-08-13 01:34:25');




