-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drug`
--
CREATE DATABASE IF NOT EXISTS `drug` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `drug`;

-- --------------------------------------------------------

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
CREATE TABLE IF NOT EXISTS `drug` (
  `clinicId` int(3) NOT NULL, 
  `drugName` varchar(128) NOT NULL,
  `quantity` int(11) NOT NULL,
  `restockStatus` char(3) NOT NULL,
  `supplierName` varchar(128) NOT NULL,
  `supplierEmail` varchar(128) NOT NULL,
  `reorderQuantity` int(11) NOT NULL,
  PRIMARY KEY (`clinicId`, `drugName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `drug`
--

INSERT INTO `drug` (`clinicId`,`drugName`,`quantity`,`restockStatus`,`supplierName`,`supplierEmail`,`reorderQuantity`) VALUES
(1,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(1,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Baricitinib', 150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Diazepam', 210, 'yes','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Etravirine', 130,'yes','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Fludrocortisone Acetate', 280,'yes','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(1,'Gliclazide', 180,'yes','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Hydrocortisone', 350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(1,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(1,'Ketoprofen', 150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Lidocaine', 120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Methoxsalen', 190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Nitrazepam', 110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Olanzapine', 190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Quetiapine', 210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Rifampicin', 160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Sodium Bicarbonate', 240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(1,'Tamoxifen', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Ursodeoxycholic Acid', 170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(1,'Vitamin A', 110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Warfarin Sodium', 140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(1,'Zidovudine', 160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(2,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Baricitinib',150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Diazepam', 210, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Etravirine', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Fludrocortisone Acetate',  280,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(2,'Gliclazide',  180,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Hydrocortisone',  350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(2,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(2,'Ketoprofen',  150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Lidocaine',  120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Methoxsalen',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Nitrazepam',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Olanzapine',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Quetiapine',  210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Rifampicin',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Sodium Bicarbonate',  240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(2,'Tamoxifen',  130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Ursodeoxycholic Acid', 170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(2,'Vitamin A', 110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Warfarin Sodium', 140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(2,'Zidovudine', 160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(3,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Baricitinib', 150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Diazepam', 210, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Etravirine', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Fludrocortisone Acetate',  280,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(3,'Gliclazide',  180,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Hydrocortisone',  350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(3,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(3,'Ketoprofen',  150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Lidocaine',  120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Methoxsalen',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Nitrazepam',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Olanzapine',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Quetiapine',  210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Rifampicin',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Sodium Bicarbonate',  240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(3,'Tamoxifen',  130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Ursodeoxycholic Acid',  170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(3,'Vitamin A',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Warfarin Sodium',  140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(3,'Zidovudine',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(4,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Baricitinib', 150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Diazepam', 210, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Etravirine', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Fludrocortisone Acetate',  280,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(4,'Gliclazide',  180,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Hydrocortisone',  350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(4,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(4,'Ketoprofen',  150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Lidocaine',  120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Methoxsalen',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Nitrazepam',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Olanzapine',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Quetiapine',  210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Rifampicin',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Sodium Bicarbonate',  240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(4,'Tamoxifen',  130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Ursodeoxycholic Acid',  170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(4,'Vitamin A',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Warfarin Sodium',  140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(4,'Zidovudine',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(5,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Baricitinib', 150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Diazepam', 210, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Etravirine', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Fludrocortisone Acetate',  280,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(5,'Gliclazide',  180,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Hydrocortisone',  350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(5,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(5,'Ketoprofen',  150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Lidocaine',  120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Methoxsalen',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Nitrazepam',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Olanzapine',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Quetiapine',  210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Rifampicin',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Sodium Bicarbonate',  240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(5,'Tamoxifen',  130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Ursodeoxycholic Acid',  170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(5,'Vitamin A',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Warfarin Sodium',  140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(5,'Zidovudine',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Paracetamol', 500, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',500),
(6,'Albendazole', 110, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Baricitinib', 150, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Calcium Acetate', 200, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Diazepam', 210, 'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Etravirine', 130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Fludrocortisone Acetate',  280,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',300),
(6,'Gliclazide',  180,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Hydrocortisone',  350,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(6,'Ibuprofen', 400,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',400),
(6,'Ketoprofen',  150,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Lidocaine',  120,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Methoxsalen',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Nitrazepam',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Olanzapine',  190,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Quetiapine',  210,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Rifampicin',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Sodium Bicarbonate',  240,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',250),
(6,'Tamoxifen',  130,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Ursodeoxycholic Acid',  170,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',200),
(6,'Vitamin A',  110,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Warfarin Sodium',  140,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150),
(6,'Zidovudine',  160,'no','ClinicDrugSupplier','clinicDrugSupplier@gmail.com',150);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
