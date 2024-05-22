/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.3.20-MariaDB : Database - lab_store
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lab_store` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `lab_store`;

/*Table structure for table `tbl_card` */

DROP TABLE IF EXISTS `tbl_card`;

CREATE TABLE `tbl_card` (
  `Card_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Cust_ID` int(5) NOT NULL,
  `Card_No` varchar(25) NOT NULL,
  `Card_Name` varchar(20) NOT NULL,
  `Exp_Date` varchar(10) NOT NULL,
  `Card_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Card_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_card` */

insert  into `tbl_card`(`Card_ID`,`Cust_ID`,`Card_No`,`Card_Name`,`Exp_Date`,`Card_Status`) values (1,1,'1263 7812 8126 6622','sankar','03/44','1'),(2,1,'2357 6126 2666 6666','sanka','02/33','1');

/*Table structure for table `tbl_cart_child` */

DROP TABLE IF EXISTS `tbl_cart_child`;

CREATE TABLE `tbl_cart_child` (
  `CC_ID` int(5) NOT NULL AUTO_INCREMENT,
  `CM_ID` int(5) NOT NULL,
  `Item_ID` int(5) NOT NULL,
  `qty` int(5) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `delivery_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CC_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_cart_child` */

insert  into `tbl_cart_child`(`CC_ID`,`CM_ID`,`Item_ID`,`qty`,`price`,`delivery_status`) values (2,2,1,2,7200.00,NULL),(3,3,1,6,14400.00,NULL),(5,4,4,2,699.30,NULL);

/*Table structure for table `tbl_cart_master` */

DROP TABLE IF EXISTS `tbl_cart_master`;

CREATE TABLE `tbl_cart_master` (
  `CM_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Cust_ID` int(5) NOT NULL,
  `Total_amount` decimal(8,2) NOT NULL,
  `Cart_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`CM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_cart_master` */

insert  into `tbl_cart_master`(`CM_ID`,`Cust_ID`,`Total_amount`,`Cart_Status`) values (2,1,7200.00,'delivered'),(3,1,21600.00,'checkout'),(4,1,33099.30,'pending');

/*Table structure for table `tbl_category` */

DROP TABLE IF EXISTS `tbl_category`;

CREATE TABLE `tbl_category` (
  `Cat_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Cat_Name` varchar(20) NOT NULL,
  `Cat_desc` varchar(100) DEFAULT NULL,
  `Cat_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Cat_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_category` */

insert  into `tbl_category`(`Cat_ID`,`Cat_Name`,`Cat_desc`,`Cat_Status`) values (1,'medical','hello','1'),(2,'surgial','Sample desc.......','1'),(3,'lab',NULL,'1');

/*Table structure for table `tbl_courier` */

DROP TABLE IF EXISTS `tbl_courier`;

CREATE TABLE `tbl_courier` (
  `Cour_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Staff_ID` int(5) NOT NULL,
  `Cour_Name` varchar(20) NOT NULL,
  `Cour_Phone` decimal(10,0) NOT NULL,
  `Cour_Address` varchar(50) NOT NULL,
  `Cour_Dist` varchar(20) NOT NULL,
  `Cour_State` varchar(20) NOT NULL,
  `Cour_Pin` int(10) NOT NULL,
  `Cour_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Cour_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_courier` */

insert  into `tbl_courier`(`Cour_ID`,`Username`,`Staff_ID`,`Cour_Name`,`Cour_Phone`,`Cour_Address`,`Cour_Dist`,`Cour_State`,`Cour_Pin`,`Cour_Status`) values (1,'cor@gmail.com',0,'sunny k',9123456722,'ross villa','ekm','andra',688523,'1');

/*Table structure for table `tbl_customer` */

DROP TABLE IF EXISTS `tbl_customer`;

CREATE TABLE `tbl_customer` (
  `Cust_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Cust_Fname` varchar(20) NOT NULL,
  `Cust_Lname` varchar(10) NOT NULL,
  `Cust_Phone` decimal(10,0) NOT NULL,
  `Cust_Hname` varchar(20) NOT NULL,
  `Cust_Street` varchar(25) NOT NULL,
  `Cust_Dist` varchar(20) NOT NULL,
  `Cust_State` varchar(20) NOT NULL,
  `Cust_Pincode` varchar(6) NOT NULL,
  `Cust_Date` varchar(10) NOT NULL,
  `Cust_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Cust_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_customer` */

insert  into `tbl_customer`(`Cust_ID`,`Username`,`Cust_Fname`,`Cust_Lname`,`Cust_Phone`,`Cust_Hname`,`Cust_Street`,`Cust_Dist`,`Cust_State`,`Cust_Pincode`,`Cust_Date`,`Cust_Status`) values (1,'san@gmail.com','san','kar',6238526459,'ross villa','Ernakulam','ekm','Kerala','688523','2023-03-13','1');

/*Table structure for table `tbl_delivery` */

DROP TABLE IF EXISTS `tbl_delivery`;

CREATE TABLE `tbl_delivery` (
  `Delivery_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Payment_ID` int(5) NOT NULL,
  `Cour_ID` int(5) NOT NULL,
  `Delivery_Date` varchar(10) NOT NULL,
  PRIMARY KEY (`Delivery_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_delivery` */

insert  into `tbl_delivery`(`Delivery_ID`,`Payment_ID`,`Cour_ID`,`Delivery_Date`) values (1,1,1,'2023-03-13');

/*Table structure for table `tbl_item` */

DROP TABLE IF EXISTS `tbl_item`;

CREATE TABLE `tbl_item` (
  `Item_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Item_Name` varchar(500) NOT NULL,
  `Cat_ID` int(5) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Item_Image` varchar(500) NOT NULL,
  `Stock` int(10) NOT NULL,
  `Profit_Percentage` decimal(10,2) NOT NULL,
  `price` varchar(100) DEFAULT NULL,
  `Item_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Item_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_item` */

insert  into `tbl_item`(`Item_ID`,`Item_Name`,`Cat_ID`,`Description`,`Item_Image`,`Stock`,`Profit_Percentage`,`price`,`Item_Status`) values (1,'lab desk',2,'sample product.....','static/uploads/e487b88a-07c0-4dfe-b2ad-3c6609f4adb34k-viper-valorant-f2.jpg',8,10.00,'3600.00','1'),(3,'vessel',3,'chumma','static/uploads/5f144c72-0722-4131-a5f1-6b80276b836061a50d69a13ad1e3ca6899eb90dc302d.jpg',33,10.00,'1100.00','1'),(4,'hello',2,'sdasdsa','static/uploads/86bdec5c-2d0d-4819-944e-db7a1d54cfd3avatar.jpg',333,5.00,'349.65','1');

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `Username` varchar(30) NOT NULL,
  `Password` varchar(10) NOT NULL,
  `User_Type` varchar(10) NOT NULL,
  `Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`Username`,`Password`,`User_Type`,`Status`) values ('admin@gmail.com','admin','admin','1'),('cor@gmail.com','cor','Courier','1'),('san@gmail.com','san','Customer','1'),('staff@gmail.com','staff','Staff','1');

/*Table structure for table `tbl_payment` */

DROP TABLE IF EXISTS `tbl_payment`;

CREATE TABLE `tbl_payment` (
  `Payment_ID` int(5) NOT NULL AUTO_INCREMENT,
  `CM_ID` int(5) NOT NULL,
  `Card_ID` int(5) NOT NULL,
  `amount` varchar(12) DEFAULT NULL,
  `Payment_Date` varchar(12) NOT NULL,
  PRIMARY KEY (`Payment_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_payment` */

insert  into `tbl_payment`(`Payment_ID`,`CM_ID`,`Card_ID`,`amount`,`Payment_Date`) values (1,2,1,'720.00','2023-03-13'),(2,3,2,'21600.00','2023-03-14'),(3,3,2,'21600.00','2023-03-14');

/*Table structure for table `tbl_purchase_child` */

DROP TABLE IF EXISTS `tbl_purchase_child`;

CREATE TABLE `tbl_purchase_child` (
  `PC_ID` int(5) NOT NULL AUTO_INCREMENT,
  `PM_ID` int(5) NOT NULL,
  `Item_ID` int(5) NOT NULL,
  `Quantity` decimal(10,2) NOT NULL,
  `Cost_Price` decimal(10,2) NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `p_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PC_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_purchase_child` */

insert  into `tbl_purchase_child`(`PC_ID`,`PM_ID`,`Item_ID`,`Quantity`,`Cost_Price`,`selling_price`,`p_status`) values (3,3,1,22.00,300.00,330.00,'available'),(4,4,1,222.00,300.00,330.00,'stock added'),(5,5,1,22.00,3000.00,3300.00,'stock added'),(6,6,4,333.00,333.00,349.65,'stock added'),(7,7,1,2.00,1000.00,1100.00,'available'),(8,8,3,33.00,1000.00,1100.00,'stock added'),(9,9,3,22.00,1000.00,1100.00,'available');

/*Table structure for table `tbl_purchase_master` */

DROP TABLE IF EXISTS `tbl_purchase_master`;

CREATE TABLE `tbl_purchase_master` (
  `PM_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Vendor_ID` int(5) NOT NULL,
  `Staff_ID` int(5) NOT NULL,
  `Tot_amount` decimal(10,2) NOT NULL,
  `Pur_Date` date NOT NULL,
  `Pur_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`PM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_purchase_master` */

insert  into `tbl_purchase_master`(`PM_ID`,`Vendor_ID`,`Staff_ID`,`Tot_amount`,`Pur_Date`,`Pur_Status`) values (3,1,0,6600.00,'2023-03-13','paid'),(4,1,0,66600.00,'2023-03-13','paid'),(5,1,0,6600.00,'2023-03-13','paid'),(6,1,0,110889.00,'2023-03-19','paid'),(7,1,0,2000.00,'2023-03-19','paid'),(8,2,0,33000.00,'2023-03-19','paid'),(9,1,0,22000.00,'2023-03-19','paid');

/*Table structure for table `tbl_staff` */

DROP TABLE IF EXISTS `tbl_staff`;

CREATE TABLE `tbl_staff` (
  `Staff_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Username` varchar(30) NOT NULL,
  `Staff_Fname` varchar(10) NOT NULL,
  `Staff_Lname` varchar(10) NOT NULL,
  `Staff_Phone` decimal(10,0) NOT NULL,
  `Staff_Hname` varchar(20) NOT NULL,
  `Staff_Street` varchar(25) NOT NULL,
  `Staff_Dist` varchar(20) NOT NULL,
  `Staff_State` varchar(20) NOT NULL,
  `Staff_Pin` int(6) NOT NULL,
  `Staff_Date` varchar(10) NOT NULL,
  `Staff_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Staff_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_staff` */

insert  into `tbl_staff`(`Staff_ID`,`Username`,`Staff_Fname`,`Staff_Lname`,`Staff_Phone`,`Staff_Hname`,`Staff_Street`,`Staff_Dist`,`Staff_State`,`Staff_Pin`,`Staff_Date`,`Staff_Status`) values (1,'staff@gmail.com','John','City',9846354290,'ross villa','Ernakulam','alappuzhass','Kerala',688523,'2023-03-13','1');

/*Table structure for table `tbl_vendor` */

DROP TABLE IF EXISTS `tbl_vendor`;

CREATE TABLE `tbl_vendor` (
  `Vendor_ID` int(5) NOT NULL AUTO_INCREMENT,
  `Staff_ID` int(5) NOT NULL,
  `Vendor_Name` varchar(20) NOT NULL,
  `Vendor_Email` varchar(30) NOT NULL,
  `Vendor_Phone` decimal(10,0) NOT NULL,
  `Vendor_Hname` varchar(20) NOT NULL,
  `Vendor_Dist` varchar(20) NOT NULL,
  `Vendor_State` varchar(20) NOT NULL,
  `Vendor_Pin` int(6) NOT NULL,
  `Vendor_Date` varchar(10) NOT NULL,
  `Vendor_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Vendor_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tbl_vendor` */

insert  into `tbl_vendor`(`Vendor_ID`,`Staff_ID`,`Vendor_Name`,`Vendor_Email`,`Vendor_Phone`,`Vendor_Hname`,`Vendor_Dist`,`Vendor_State`,`Vendor_Pin`,`Vendor_Date`,`Vendor_Status`) values (1,0,'Mok suni','newcus@gmail.com',9846354290,'kottakal','alpy','delhi',688523,'2023-03-13','1'),(2,0,'aswin','aswin@gmail.com',6345674553,'sabdjsa','alpy','kerala',688523,'2023-03-19','1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
