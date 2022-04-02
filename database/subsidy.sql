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
CREATE DATABASE IF NOT EXISTS `subsidy` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `subsidy`;

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `subsidy`;
CREATE TABLE IF NOT EXISTS `subsidy` (
  `nric` varchar(9) NOT NULL,
  `cardNumber` varchar(8) NOT NULL,
  `cardType` char(128) NOT NULL,
  `organisationType` char(64) NULL,
  `expiryDate` varchar(10) NOT NULL,
  PRIMARY KEY (`cardNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient`
--

INSERT INTO `subsidy` (`nric`, `cardNumber`, `cardType`, `organisationType`, `expiryDate`) VALUES
('S9812381D', '11237623', 'GreenCHAS', NULL, '29/03/2019'),
('S9812382B', '78045522', 'Merdeka', NULL, '05/09/2020'),
('S9812385G', '01148732', 'BlueCHAS', NULL, '15/12/2023'),
('G1612350T', '90348226', 'Pioneer', NULL, '26/01/2025'),
('F1612347K', '55230598', 'Company', 'DBS', '08/07/2022');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
