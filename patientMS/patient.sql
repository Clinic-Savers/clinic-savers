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
-- Database: `patient`
--
CREATE DATABASE IF NOT EXISTS `patient` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `patient`;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE IF NOT EXISTS `patient` (
  `patientName` char(64) NOT NULL,
  `nric` varchar(9) NOT NULL,
  `mobileNumber` int(8) NOT NULL,
  `address` varchar(128) NOT NULL,
  `vaccinationStatus` char(64) NOT NULL,
  PRIMARY KEY (`nric`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patientName`,`nric`, `mobileNumber`, `address`, `vaccinationStatus`) VALUES
('Mary Lim Mei Ling', 'S9812381D', '81327832', '9 BISHAN PLACE, #01-40', 'Vaccinated'),
('Alfred Tan Jun Jie','S9812382B', '91134712', '3023 Ubi Road 3 06-01', 'Vaccinated'),
('Nur Fatimah Binte Muhammad','S9812385G', '92821321', '50 Seletar Hills Drive', 'Unvaccinated'),
('Simon Deyes','G1612350T', '81312554', '50 1003 Bukit Merah Central #02-10', 'Vaccinated'),
('Tan Wei Ming','F1612347K', '92233223', '9010 Tampines St 93 #04-109', 'Vaccinated');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
