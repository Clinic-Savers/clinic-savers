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
-- Database: `drugRefill`
--
CREATE DATABASE IF NOT EXISTS `drugRefill` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `drugRefill`;

-- --------------------------------------------------------

--
-- Table structure for table `drugRefill`
--

DROP TABLE IF EXISTS `drugRefill`;
CREATE TABLE IF NOT EXISTS `drugRefill` (
  `nric` varchar(9) NOT NULL,
  `patientName` char(64) NOT NULL,
  `existingCondition` char(64) NOT NULL,
  `drugName` varchar(128) NOT NULL,
  `date` varchar(64) NOT NULL,
  PRIMARY KEY (`nric`,`drugName`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `drugRefill`
--

INSERT INTO `drugRefill` (`nric`,`patientName`,`existingCondition`,`drugName`,`date`) VALUES
('S9812381D','Tricia Tan Xiao Hui','refill vitamins','Vitamin A', '2022-02-27'),
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
