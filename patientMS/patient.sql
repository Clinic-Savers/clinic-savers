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
  `postalCode` int(6) NOT NULL, 
  `address` varchar(128) NOT NULL,
  `vaccinationStatus` char(64) NOT NULL,
  PRIMARY KEY (`nric`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`patientName`,`nric`, `mobileNumber`, `address`, `postalCode`, `vaccinationStatus`) VALUES
('TAN MING HENG TERENCE', 'S9812388A', '81312554', 'Blk 123 TOA PAYOH VIEW #14-22', '310123', 'Vaccinated'), 
('LIM YONG XIANG', 'S9812379B', '97399245', 'Blk 123 TOA PAYOH VIEW #12-22', '310123', 'Vaccinated'), 
('BERNARD WONG', 'S9912375C', '97399245', 'Blk 138 HDB-TAMPINES #38-10', '520138', 'Vaccinated'),
('XIA YIN CHOW', 'S9640091H', '99472910', 'Blk 148 HDB-BUKIT PANJANG #02-101', '670148', 'Vaccinated'),
('DA DONG BAI','S7955237B', '93749284', 'Blk 148 HDB-BUKIT PANJANG #04-101', '670148', 'Vaccinated'),
('HENG GANG ZHENG JASMON', 'S9245177A', '91822847', 'Blk 148 HDB-BUKIT PANJANG #12-102', '670148', 'Vaccinated'), 
('LEE SHU KWAN ELICIA', 'S8243452F', '83888811', 'Blk 148 HDB-BUKIT PANJANG #11-101', '670148', 'Vaccinated'), 
('RATAN SHIVALI JOSHI', 'S7380725E', '94891920', 'Blk 148 HDB-BUKIT PANJANG #8-106', '670148', 'Vaccinated')
;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
