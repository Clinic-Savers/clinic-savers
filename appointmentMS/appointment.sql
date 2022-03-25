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
-- Database: `appointment`
--
CREATE DATABASE IF NOT EXISTS `appointment` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `appointment`;

-- --------------------------------------------------------

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE IF NOT EXISTS `appointment` (
  `nric` varchar(9) NOT NULL,
  `patientName` char(64) NOT NULL,
  `symptoms` varchar(128) NOT NULL,
  `potentialCovid` char(3) NOT NULL,
  `clinicId` int(3) NOT NULL, 
  `appointmentDate` varchar(64) NOT NULL,
  `appointmentTime` varchar(64) NOT NULL,
  PRIMARY KEY (`nric`,`appointmentDate`, `appointmentTime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `appointment`
--

INSERT INTO `appointment` (`nric`,`patientName`,`symptoms`, `potentialCovid`, `clinicID`, `appointmentDate`, `appointmentTime`) VALUES
('S9812381D', 'Tricia Tan Xiao Hui', 'runny nose, sore throat and fever', 'Yes', 1, '2022-01-27','13:30:00'),
('S9812382B', 'Alfred Tan Jun Jie', 'stomach pain, nausea and heartburn', 'No', 5, '2022-03-25', '23:30:00'),
('S9812385G', 'Nur Fatimah Binte Muhammad', 'rashes on my body', 'No', 5, '2022-03-25', '23:00:00'),
('F1612347K', 'Tan Wei Ming', 'insomnia and headache', 'No', '2022-03-19', 6, '08:00:00'); 

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
