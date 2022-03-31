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
-- Database: `patientRecord`
--
CREATE DATABASE IF NOT EXISTS `patientRecord` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `patientRecord`;

-- --------------------------------------------------------

--
-- Table structure for table `patientRecord`
--

DROP TABLE IF EXISTS `patientRecord`;
CREATE TABLE IF NOT EXISTS `patientRecord` (
  `patientRecordId` int(11) AUTO_INCREMENT NOT NULL,
  `nric` varchar(9) NOT NULL,
  `clinicId` int(3) NOT NULL, 
  `drugName` varchar(128) NOT NULL,
  `prescribeQuantity` int(11) NOT NULL,
  `date` varchar(64) NOT NULL,
  `time` varchar(64) NOT NULL,
  PRIMARY KEY (`patientRecordId`,`nric`,`clinicId`,`drugName`,`date`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patientRecord`
--

INSERT INTO `patientRecord` (`nric`,`clinicId`,`drugName`,`prescribeQuantity`,`date`,`time`) VALUES
('S9812381D',1,'Paracetamol', 20, '2022-01-27','13:30:00'),
('S9812381D',1,'Vitamin A', 25, '2022-01-27','13:30:00'),
('F1612347K',2,'Baricitinib', 20,'2022-03-19', '08:00:00'),
('F1612347K',2,'Hydrocortisone', 1,'2022-03-19', '08:00:00'),
('S9812385G',5, 'Hydrocortisone', 1,'2022-03-12', '09:00:00'),
('S9812382B',4,'Calcium Acetate', 20,'2022-02-01', '14:30:00'),
('S9812382B',4,'Sodium Bicarbonate', 15,'2022-02-01', '14:30:00'),
('G1612350T',3, 'Nitrazepam', 20, '2022-02-19', '18:00:00'),
('G1612350T',3, 'Baricitinib',15, '2022-02-19', '18:00:00'),
('S9912374E',6, 'Fludrocortisone Acetate', 30,'2022-02-07', '13:00:00'),
('S9912374E',6, 'Vitamin A', 30,'2022-02-07', '13:00:00'),
('S6005053H',1, 'Zidovudine', 30, '2022-02-27', '16:00:00'),
('S6005053H',1, 'Ibuprofen', 30,'2022-02-27', '16:00:00'),
('S6005053H',1, 'Etravirine', 30, '2022-02-27', '16:00:00'),
('S6005055',2, 'Gliclazide', 30, '2022-02-11', '16:30:00'),
('G1612348Q',1, 'Methoxsalen', 30, '2022-01-15', '08:00:00'),
('G1612348Q',1, 'Hydrocortisone', 2, '2022-01-15', '08:00:00')
;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
