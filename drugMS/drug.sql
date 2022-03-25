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
  `drugId` int(11) AUTO_INCREMENT NOT NULL ,
  `quantity` int(11) NOT NULL,
  `restockStatus` char(3) NOT NULL,
  PRIMARY KEY (`clinicId`,`drugId`, `drugName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `drug`
--

INSERT INTO `drug` (`clinicId`,`drugName`,`drugId`,`quantity`,`restockStatus`) VALUES
(1,'Paracetamol', 1, 500, 'no'),
(1,'Albendazole', 2, 110, 'no'),
(1,'Baricitinib', 3, 150, 'no'),
(1,'Calcium Acetate', 4, 200, 'no'),
(1,'Diazepam', 5, 210, 'no'),
(1,'Etravirine', 6, 130,'no'),
(1,'Fludrocortisone Acetate', 7, 280,'no'),
(1,'Gliclazide', 8, 180,'no'),
(1,'Hydrocortisone', 9, 350,'no'),
(1,'Ibuprofen', 10, 400,'no'),
(1,'Ketoprofen', 11, 150,'no'),
(1,'Lidocaine', 12, 120,'no'),
(1,'Methoxsalen', 13, 190,'no'),
(1,'Nitrazepam', 14, 110,'no'),
(1,'Olanzapine', 15, 190,'no'),
(1,'Quetiapine', 16, 210,'no'),
(1,'Rifampicin', 17, 160,'no'),
(1,'Sodium Bicarbonate', 18, 240,'no'),
(1,'Tamoxifen', 19, 130,'no'),
(1,'Ursodeoxycholic Acid', 20, 170,'no'),
(1,'Vitamin A', 21, 110,'no'),
(1,'Warfarin Sodium', 22, 140,'no'),
(1,'Zidovudine', 23, 160,'no'),
(2,'Paracetamol', 1, 500, 'no'),
(2,'Albendazole', 2, 110, 'no'),
(2,'Baricitinib', 3, 150, 'no'),
(2,'Calcium Acetate', 4, 200, 'no'),
(2,'Diazepam', 5, 210, 'no'),
(2,'Etravirine', 6, 130,'no'),
(2,'Fludrocortisone Acetate', 7, 280,'no'),
(2,'Gliclazide', 8, 180,'no'),
(2,'Hydrocortisone', 9, 350,'no'),
(2,'Ibuprofen', 10, 400,'no'),
(2,'Ketoprofen', 11, 150,'no'),
(2,'Lidocaine', 12, 120,'no'),
(2,'Methoxsalen', 13, 190,'no'),
(2,'Nitrazepam', 14, 110,'no'),
(2,'Olanzapine', 15, 190,'no'),
(2,'Quetiapine', 16, 210,'no'),
(2,'Rifampicin', 17, 160,'no'),
(2,'Sodium Bicarbonate', 18, 240,'no'),
(2,'Tamoxifen', 19, 130,'no'),
(2,'Ursodeoxycholic Acid', 20, 170,'no'),
(2,'Vitamin A', 21, 110,'no'),
(2,'Warfarin Sodium', 22, 140,'no'),
(2,'Zidovudine', 23, 160,'no'),
(3,'Paracetamol', 1, 500, 'no'),
(3,'Albendazole', 2, 110, 'no'),
(3,'Baricitinib', 3, 150, 'no'),
(3,'Calcium Acetate', 4, 200, 'no'),
(3,'Diazepam', 5, 210, 'no'),
(3,'Etravirine', 6, 130,'no'),
(3,'Fludrocortisone Acetate', 7, 280,'no'),
(3,'Gliclazide', 8, 180,'no'),
(3,'Hydrocortisone', 9, 350,'no'),
(3,'Ibuprofen', 10, 400,'no'),
(3,'Ketoprofen', 11, 150,'no'),
(3,'Lidocaine', 12, 120,'no'),
(3,'Methoxsalen', 13, 190,'no'),
(3,'Nitrazepam', 14, 110,'no'),
(3,'Olanzapine', 15, 190,'no'),
(3,'Quetiapine', 16, 210,'no'),
(3,'Rifampicin', 17, 160,'no'),
(3,'Sodium Bicarbonate', 18, 240,'no'),
(3,'Tamoxifen', 19, 130,'no'),
(3,'Ursodeoxycholic Acid', 20, 170,'no'),
(3,'Vitamin A', 21, 110,'no'),
(3,'Warfarin Sodium', 22, 140,'no'),
(3,'Zidovudine', 23, 160,'no'),
(4,'Paracetamol', 1, 500, 'no'),
(4,'Albendazole', 2, 110, 'no'),
(4,'Baricitinib', 3, 150, 'no'),
(4,'Calcium Acetate', 4, 200, 'no'),
(4,'Diazepam', 5, 210, 'no'),
(4,'Etravirine', 6, 130,'no'),
(4,'Fludrocortisone Acetate', 7, 280,'no'),
(4,'Gliclazide', 8, 180,'no'),
(4,'Hydrocortisone', 9, 350,'no'),
(4,'Ibuprofen', 10, 400,'no'),
(4,'Ketoprofen', 11, 150,'no'),
(4,'Lidocaine', 12, 120,'no'),
(4,'Methoxsalen', 13, 190,'no'),
(4,'Nitrazepam', 14, 110,'no'),
(4,'Olanzapine', 15, 190,'no'),
(4,'Quetiapine', 16, 210,'no'),
(4,'Rifampicin', 17, 160,'no'),
(4,'Sodium Bicarbonate', 18, 240,'no'),
(4,'Tamoxifen', 19, 130,'no'),
(4,'Ursodeoxycholic Acid', 20, 170,'no'),
(4,'Vitamin A', 21, 110,'no'),
(4,'Warfarin Sodium', 22, 140,'no'),
(4,'Zidovudine', 23, 160,'no'),
(5,'Paracetamol', 1, 500, 'no'),
(5,'Albendazole', 2, 110, 'no'),
(5,'Baricitinib', 3, 150, 'no'),
(5,'Calcium Acetate', 4, 200, 'no'),
(5,'Diazepam', 5, 210, 'no'),
(5,'Etravirine', 6, 130,'no'),
(5,'Fludrocortisone Acetate', 7, 280,'no'),
(5,'Gliclazide', 8, 180,'no'),
(5,'Hydrocortisone', 9, 350,'no'),
(5,'Ibuprofen', 10, 400,'no'),
(5,'Ketoprofen', 11, 150,'no'),
(5,'Lidocaine', 12, 120,'no'),
(5,'Methoxsalen', 13, 190,'no'),
(5,'Nitrazepam', 14, 110,'no'),
(5,'Olanzapine', 15, 190,'no'),
(5,'Quetiapine', 16, 210,'no'),
(5,'Rifampicin', 17, 160,'no'),
(5,'Sodium Bicarbonate', 18, 240,'no'),
(5,'Tamoxifen', 19, 130,'no'),
(5,'Ursodeoxycholic Acid', 20, 170,'no'),
(5,'Vitamin A', 21, 110,'no'),
(5,'Warfarin Sodium', 22, 140,'no'),
(5,'Zidovudine', 23, 160,'no'),
(6,'Paracetamol', 1, 500, 'no'),
(6,'Albendazole', 2, 110, 'no'),
(6,'Baricitinib', 3, 150, 'no'),
(6,'Calcium Acetate', 4, 200, 'no'),
(6,'Diazepam', 5, 210, 'no'),
(6,'Etravirine', 6, 130,'no'),
(6,'Fludrocortisone Acetate', 7, 280,'no'),
(6,'Gliclazide', 8, 180,'no'),
(6,'Hydrocortisone', 9, 350,'no'),
(6,'Ibuprofen', 10, 400,'no'),
(6,'Ketoprofen', 11, 150,'no'),
(6,'Lidocaine', 12, 120,'no'),
(6,'Methoxsalen', 13, 190,'no'),
(6,'Nitrazepam', 14, 110,'no'),
(6,'Olanzapine', 15, 190,'no'),
(6,'Quetiapine', 16, 210,'no'),
(6,'Rifampicin', 17, 160,'no'),
(6,'Sodium Bicarbonate', 18, 240,'no'),
(6,'Tamoxifen', 19, 130,'no'),
(6,'Ursodeoxycholic Acid', 20, 170,'no'),
(6,'Vitamin A', 21, 110,'no'),
(6,'Warfarin Sodium', 22, 140,'no'),
(6,'Zidovudine', 23, 160,'no');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
