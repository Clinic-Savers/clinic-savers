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
  `id` int(3) NOT NULL, 
  `name` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `postalCode` varchar(6) NOT NULL,
  `email` varchar(128) NOT NULL,
  `queueLength` int(3) NOT NULL
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `clinic`
--

INSERT INTO `clinic` (`id`,`name`,`address`, `postalCode`, `email`, `queueLength`) VALUES
(1, `Raffles Medical - Anchorvale`, `370 Alexandra Road #B1-41 Anchorpoint`, `159953`, `daryl.ang.2021@scis.smu.edu.sg`, 3), 
(2, `Raffles Medical - Ang Mo Kio`, `Blk 722 Ang Mo Kio Avenue 8 #01-2825`, `560722`, `jann.chia.2020@scis.smu.edu.sg`, 2), 
(3, `Raffles Medical - Anson Centre`, `51 Anson Road, #01-51 Anson Centre`, `079904`, `jannoying@hotmail.com`, 1), 
(4, `Raffles Medical - Bishan`, `Blk 283 Bishan Street 22, #01-177`, `570283`, `janntravel@gmail.com`, 4), 
(5, `Raffles Medical - Compass One`, `1 Sengkang Square, #04-09, Compass One`, `545078`, `jannlearns@gmail.com`, 2), 
(6, `Raffles Medical - Rivervale Mall`, `11, Rivervale Crescent, #02-17 Rivervale Mall`, `545082`, `jannchia29@yahoo.com`, 1)
;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
