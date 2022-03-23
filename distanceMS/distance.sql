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
  `patientPostalCode` int(6) NOT NULL,
  `clinicPostalCode` int(6) NOT NULL,
  `distanceAway` float(1) NOT NULL,
  PRIMARY KEY (`patientPostalCode`,`clinicPostalCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `distance`
--

INSERT INTO `distance` (`patientPostalCode`,`clinicPostalCode`,`distanceAway`) VALUES
(123456,234567,3.2),
(),
(),
();
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
