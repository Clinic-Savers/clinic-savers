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
-- Database: `distance`
--
CREATE DATABASE IF NOT EXISTS `distance` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `distance`;

-- --------------------------------------------------------

--
-- Table structure for table `distance`
--

DROP TABLE IF EXISTS `distance`;
CREATE TABLE IF NOT EXISTS `distance` (
  `patientPostalCode` varchar(6) NOT NULL,
  `clinicPostalCode` varchar(6) NOT NULL,
  `distanceAway` varchar(5) NOT NULL,
  PRIMARY KEY (`patientPostalCode`,`clinicPostalCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `distance`
--

INSERT INTO `distance` (`patientPostalCode`,`clinicPostalCode`,`distanceAway`) VALUES
('161003','161011','1.7'),
('640520','640498','0.9'),
('460508','529509','4.4'),
('520230','529509','3.3'),
('408663','529509','8.4')
('579837','529509','13.5');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
