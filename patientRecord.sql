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
('S9812381D','Mary Lim Mei Ling','Paracetamol', 20, 'non-refillable', '2022-01-27','13:30:00'),
('S9812381D','Mary Lim Mei Ling','Vitamin A', 25, 'refillable', '2022-01-27','13:30:00'),
('F1612347K','Tan Wei Ming', 'Aspirin', 20, 'non-refillable',  '2022-03-19', '08:00:00'),
('F1612347K','Tan Wei Ming', 'Hydrocortisone', 1, 'refillable',  '2022-03-19', '08:00:00'),
('S9812385G', 'Nur Fatimah Binte Muhammad', 'Hydrocortisone', 1, 'refillable', '2022-03-12', '09:00:00'),
('S9812382B', 'Alfred Tan Jun Jie', 'Calcium Acetate', 20,'non-refillable', '2022-02-01', '14:30:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
