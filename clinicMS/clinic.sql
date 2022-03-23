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
-- Database: `clinic`
--
CREATE DATABASE IF NOT EXISTS `clinic` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `clinic`;

-- --------------------------------------------------------

--
-- Table structure for table `clinic`
--

DROP TABLE IF EXISTS `clinic`;
CREATE TABLE IF NOT EXISTS `clinic` (
  `clinicName` varchar(128) NOT NULL,
  `clinicAddress` varchar(128) NOT NULL,
  `clinicPostalCode` varchar(6) NOT NULL,
  `description` varchar(128) NOT NULL,
  PRIMARY KEY (`clinicName`,`clinicPostalCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clinic`
--

INSERT INTO `clinic` (`clinicName`,`clinicAddress`,`clinicPostalCode`, `description`) VALUES
('Raffles Medical', '52 North Bridge Rd, #02 - 17', '179103', 'Our team of family physicians provides care for patients of all ages. Medical care includes treatment of acute and chronic conditions for adults and children, vaccinations, legal services and health screening.'),
('OneCare Medical Clinic Tiong Bahru', '11A Boon Tiong Rd, #01-08', '161011', 'OneCare Medical Clinics provide timely, affordable and professional healthcare. Our friendly team of general practitioners, family physicians, and nurses are always ready to help.'),
('Sunnyvale Clinic & Surgery', '498 Jurong West Street 41', '640498', 'nfmaslnasl'),
('Dayspring Medical Clinic (Tampines)', '2 Tampines Central 5, #04-09 Century Square', '529509', 'Minmed clinic is a CHAS registered General Practitioner (GP) clinic. We provide both teleconsult and in-clinic medical services such as doctor consultation and prescription, vaccinations and managing of chronic illnesses.'), 
('Mint Medical Centre', '107, #04-13A North Bridge Rd, Funan', '179105', 'We are a team of healthcare professionals who pride ourselves in delivering holistic general care, yet each having our own interests. We are bound by the mission to care for our patients with warmth, sincerity and concern from our heart. We the MINT healthcare team, are a family, and to us, so are you!')
;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
