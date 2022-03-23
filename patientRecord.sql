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
  `nric` varchar(9) NOT NULL,
  `patientName` char(64) NOT NULL,
  `drugName` varchar(128) NOT NULL,
  `quantity` int(11) NOT NULL,
  `refillStatus` char(64) NOT NULL,
  `date` varchar(64) NOT NULL,
  `time` varchar(64) NOT NULL,
  PRIMARY KEY (`nric`,`drugName`,`date`,`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patientRecord`
--

INSERT INTO `patientRecord` (`nric`,`patientName`,`drugName`,`quantity`,`refillStatus`,`date`,`time`) VALUES
('S9812381D','Mary Lim Mei Ling','Paracetamol', 20, 'non-refillable', '2022-01-29','14:25:30'),
('S9812381D','Mary Lim Mei Ling','Vitamin A', 25, 'refillable', '2022-01-29','14:25:30'),
('Albendazole', 100),
('Baricitinib', 150),
('Calcium Acetate', 200),
('Diazepam', 210),
('Etravirine', 130),
('Fludrocortisone Acetate', 50),
('Gliclazide', 60),
('Hydrocortisone', 350),
('Ibuprofen', 400),
('Ketoprofen', 150),
('Lidocaine', 50),
('Methoxsalen', 190),
('Nitrazepam', 30),
('Olanzapine', 70),
('Quetiapine', 40),
('Rifampicin', 80),
('Sodium Bicarbonate', 240),
('Tamoxifen', 40),
('Ursodeoxycholic Acid', 70),
('Warfarin Sodium', 40),
('Zidovudine', 160);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
