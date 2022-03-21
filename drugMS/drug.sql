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
-- Database: `drug`
--
CREATE DATABASE IF NOT EXISTS `drug` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `drug`;

-- --------------------------------------------------------

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
CREATE TABLE IF NOT EXISTS `drug` (
  `drugName` varchar(128) NOT NULL,
  `drugId` int(11) AUTO_INCREMENT NOT NULL ,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`drugId`, `drugName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `drug`
--

INSERT INTO `drug` (`drugName`,`quantity`) VALUES
('Paracetamol', 500),
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
('Vitamin A', 110),
('Warfarin Sodium', 40),
('Zidovudine', 160);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
