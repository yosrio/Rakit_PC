-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 03, 2018 at 04:24 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `komponen_komputer`
--

-- --------------------------------------------------------

--
-- Table structure for table `harddisk`
--

CREATE TABLE `harddisk` (
  `nama_hdd` varchar(100) NOT NULL,
  `interface` varchar(50) DEFAULT NULL,
  `kapasitas` int(10) DEFAULT NULL,
  `cache` int(5) DEFAULT NULL,
  `speed` int(10) DEFAULT NULL,
  `form_factor` varchar(10) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `harddisk`
--

INSERT INTO `harddisk` (`nama_hdd`, `interface`, `kapasitas`, `cache`, `speed`, `form_factor`, `harga`) VALUES
('Seagate - 500GB BarraCuda', 'SATA 6Gb/s', 500, 32, 7200, '3.5\"', 720000),
('Seagate - 1TB BarraCuda', 'SATA 6Gb/s', 1024, 64, 7200, '3.5\"', 780000),
('Seagate - 2TB BarraCuda', 'SATA 6Gb/s', 2048, 64, 7200, '3.5\"', 1080000),
('Western Digital - 500GB Blue', 'SATA 6Gb/s', 500, 16, 7200, '3.5\"', 620000),
('Western Digital - 1TB Blue', 'SATA 6Gb/s', 1024, 64, 7200, '3.5\"', 655000),
('Seagate - 10TB BarraCuda Pro', 'SATA 6Gb/s', 10240, 256, 7200, '3.5\"', 6905000),
('Western Digital - 4TB Blue ', 'SATA 6Gb/s', 4096, 64, 5400, '3.5\"', 1720000),
('Western Digital - 4TB Black', 'SATA 6Gb/s', 4096, 256, 7200, '3.5\"', 2990000),
('Western Digital - 2TB Blue', 'SATA 6Gb/s', 2048, 64, 5400, '3.5\"', 910000);

-- --------------------------------------------------------

--
-- Table structure for table `motherboard`
--

CREATE TABLE `motherboard` (
  `nama_motherboard` varchar(100) NOT NULL,
  `chipset` varchar(50) DEFAULT NULL,
  `socket` varchar(50) DEFAULT NULL,
  `tipe_memori` varchar(6) DEFAULT NULL,
  `slot_memori` varchar(3) DEFAULT NULL,
  `maksimal_memori` int(3) DEFAULT NULL,
  `interface_storage` varchar(20) DEFAULT NULL,
  `form_factor` varchar(100) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `motherboard`
--

INSERT INTO `motherboard` (`nama_motherboard`, `chipset`, `socket`, `tipe_memori`, `slot_memori`, `maksimal_memori`, `interface_storage`, `form_factor`, `harga`) VALUES
('Asus - ROG Maximus XI Formula', 'Intel® Z390', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'ATX', 7865000),
('ASRock - Z390 Phantom Gaming 4', 'Intel® Z390', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'ATX', 2449000),
('ASRock - Fatal1ty X470 Gaming-ITX/ac', 'AMD B450', 'AM 4', 'DDR4', '2', 64, 'SATA 6Gb/s', 'Mini-ITX', 3180000),
('Asus - TUF Z390-Plus Gaming', 'Intel® Z390', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'ATX', 3480000),
('Gigabyte - Z390 Aorus Elite', 'Intel® Z390', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'ATX', 3555000),
('ASRock - H81M-VG4 R2.0', 'Intel® H81', '1150', 'DDR3 ', '2', 16, 'SATA 6Gb/s', 'mATX', 710000),
('MSI A68HM-E33 V2 int', 'AMD® A68H', 'FM2+', 'DDR3', '2', 32, 'SATA 6Gb/s', 'mATX', 800000),
('MSI - A320M Pro-VH Plus', 'AMD® A320', 'AM 4', 'DDR4', '2', 32, 'SATA 6Gb/s', 'mATX', 839000),
('ASRock - H110M-HDV', 'Intel® H110', 'LGA 1151', 'DDR4', '2', 32, 'SATA 6Gb/s', 'mATX', 855000),
('ASRock - FM2A68M-HD+', 'AMD A68H (Bolton-D2H)', 'FM2+ 95W / FM2 100W processors', 'DDR3', '2', 32, 'SATA 6Gb/s', 'mATX', 790000),
('MSI - H110M Grenade ', 'Intel® H110', 'LGA 1151', 'DDR4', '2', 32, 'SATA 6Gb/s', 'mATX', 1000000),
('MSI - B250M Pro-VDH', 'Intel® B250', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'mATX', 1300000),
('Gigabyte - GA-B250M-D2V', 'Intel® B250', 'LGA 1151', 'DDR4', '4', 64, 'SATA 6Gb/s', 'm-ATX', 1345000);

-- --------------------------------------------------------

--
-- Table structure for table `power_supply`
--

CREATE TABLE `power_supply` (
  `nama_psu` varchar(100) NOT NULL,
  `modular_cable_management` varchar(50) DEFAULT NULL,
  `sleeved_cable` enum('yes','no') DEFAULT NULL,
  `form_factor` varchar(50) DEFAULT NULL,
  `efficiency` varchar(50) DEFAULT NULL,
  `power_supply` int(10) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `power_supply`
--

INSERT INTO `power_supply` (`nama_psu`, `modular_cable_management`, `sleeved_cable`, `form_factor`, `efficiency`, `power_supply`, `harga`) VALUES
('be quite! - System Power 400W', 'Non Modular', 'yes', 'ATX', '80 Plus (230V EU)', 400, 540000),
('be quite! - System Power 500W', 'Non Modular', 'yes', 'ATX', '80 Plus (230V EU)', 500, 640000),
('be quite! - Dark Power Pro 1000W', 'Semi Modular', 'yes', 'ATX', '80 Plus Platinum', 1000, 3320000),
('BitFenix - Whisper 650W Gold', 'Fully Modular', 'yes', 'ATX', '80 Plus Gold', 650, 1475000),
('Seasonic-S12II-520W', 'Non Modular', 'yes', 'ATX', '80 Plus Bronze', 520, 880000),
('Thermaltake- Smart RGB 600W', 'No', 'yes', 'ATX', '80 Plus', 504, 970000),
('Be Quite!-Pure Power 500W', 'Semi Modular', 'yes', 'ATX', '80 Plus Silver', 480, 1100000),
('Corsair-CX550W', 'Semi Modular', 'yes', 'ATX', '80 Plus Bronze', 550, 1185000),
('Seasonic-S12G 650W', 'Non Modular', 'yes', 'ATX', '80 Plus Gold', 650, 1250000),
('Corsair-CX650M', 'Semi Modular', 'yes', 'ATX', '80 Plus Bronze', 648, 1285000),
('BitFenix-Whisper 550W Gold', 'Fully Modular', 'yes', 'ATX', '80 Plus Gold', 550, 1295000),
('Corsair-SF450', 'Fully Modular', 'yes', 'SFX', '80 Plus Gold', 450, 1560000),
('Corsair-RM550x', 'Fully Modular', 'yes', 'ATX', '80 Plus Gold', 550, 1685000),
('Thermaltake-Smart Pro RGB 850W Bronze', 'Fully Modular', 'yes', 'ATX', '80 Plus Bronze', 850, 1840000),
('Corsair-SF600', 'Fully Modular', 'yes', 'SFX', '80 Plus Gold', 600, 2005000),
('be quite!-Straight Power 800W', 'Semi Modular', 'yes', 'ATX', '80 Plus Gold', 780, 2240000),
('Corsair-RM850x', 'Fully Modular', 'yes', 'ATX', '80 Plus Gold', 850, 2285000),
('Enermax-Triathlor ECO 1000W', 'Semi Modular', 'yes', 'ATX', '80 Plus Bronze', 996, 2500000),
('Corsair-AX1200i', 'Fully Modular', 'yes', 'ATX', '80 Plus Platinum', 1205, 5560000);

-- --------------------------------------------------------

--
-- Table structure for table `processor`
--

CREATE TABLE `processor` (
  `nama_processor` varchar(100) NOT NULL,
  `model_number` varchar(50) DEFAULT NULL,
  `socket` varchar(50) DEFAULT NULL,
  `core` varchar(50) DEFAULT NULL,
  `clock` int(10) DEFAULT NULL,
  `tdp` int(5) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `processor`
--

INSERT INTO `processor` (`nama_processor`, `model_number`, `socket`, `core`, `clock`, `tdp`, `harga`) VALUES
('Intel - Pentium G4400', 'G4400', 'LGA 1151', 'Skylake-S', 3300, 54, 980000),
('Intel - Core i3 7100', 'i3 7100', 'LGA 1151', 'Kaby Lake-S', 3900, 51, 2200000),
('Intel - Core i3 6100', 'i3 6100', 'LGA 1151', 'Skylake-S', 3700, 51, 1950000),
('Intel - Pentium G5400', 'G5400', 'LGA 1151', 'Coffee Lake-S', 3700, 54, 1090000),
('Intel - Core i5 8500', 'i5 8500', 'LGA 1151', 'Coffee Lake-S', 3000, 65, 3660000),
('Intel-Core i7 7700', 'i7 7700', 'LGA 1151', 'Kaby Lake-S', 3600, 65, 5340000),
('Intel-Core i5 8600K', 'i5 8600K', 'LGA 1151', 'Coffee Lake-S', 3600, 95, 4600000),
('Intel-Core i9 9900K', 'i9 9900K', 'LGA 1151', 'Coffee Lake-S', 3600, 95, 10200000),
('Intel-Core i7 7820X', 'i7-7820X', 'LGA 2066', 'Skylake-X', 3600, 140, 9890000),
('AMD-A6 9500', 'A6-9600', 'Socket AM4', 'Bristol Ridge', 3500, 65, 620000),
('AMD-Ryzen 3 1200', '1200', 'Socket AM4', 'Summit Ridge', 3100, 65, 1425000),
('AMD-Ryzen 5 1600', '1600', 'Socket AM4', 'Summit Ridge', 3500, 65, 2580000),
('AMD-Ryzen 7 2700X', '2700X', 'Socket AM4', 'Pinnacle Ridge', 3700, 105, 5100000),
('AMD-Ryzen Threadripper 2950X', '2950X', 'Socket TR4', 'Colfax', 3500, 180, 14800000),
('AMD-A6-7470K', 'A4-7400K', 'FM2+', 'Godavari', 3700, 65, 750000),
('Intel-Xeon E3-1220 v5', 'E3-1220 v5', 'LGA 1151', 'Skylake-S', 3000, 80, 3450000);

-- --------------------------------------------------------

--
-- Table structure for table `ram`
--

CREATE TABLE `ram` (
  `nama_ram` varchar(100) NOT NULL,
  `tipe_ram` varchar(10) DEFAULT NULL,
  `ukuran_ram` int(5) DEFAULT NULL,
  `jumlah_ram` int(5) DEFAULT NULL,
  `total_ukuran_ram` int(5) DEFAULT NULL,
  `seri` varchar(50) DEFAULT NULL,
  `speed` int(10) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ram`
--

INSERT INTO `ram` (`nama_ram`, `tipe_ram`, `ukuran_ram`, `jumlah_ram`, `total_ukuran_ram`, `seri`, `speed`, `harga`) VALUES
('Corsair - CMW16GX4M2Z2933C16', 'DDR4', 8, 2, 16, 'PC4-24000', 2933, 3060000),
('Crucial - Ballistix 8GB PC4-21300', 'DDR4', 4, 1, 8, 'PC4-21300', 2666, 1259000),
('Corsair - CMV4GX3M1A1600C11', 'DDR3', 4, 1, 4, 'PC3-12800', 1600, 465000),
('Corsair - CMV4GX4M1A2400C16', 'DDR4', 4, 1, 4, 'PC4-19200', 2400, 625000),
('CORSAIR Memory PC 2GB', 'DDR3', 2, 1, 2, 'PC-10600', 1333, 335000),
('KINGSTON Memory PC 2GB', 'DDR3', 2, 1, 2, 'PC-12800', 1600, 350560),
('TEAM Elite Plus Memory PC 2 x 2GB', 'DDR3', 2, 2, 4, 'PC-12800', 1600, 635000),
('TEAM Mac Edition 2GB', 'DDR3', 2, 1, 2, 'PC-12800', 1600, 285000),
('TEAM Elite Plus Memory PC 2GB', 'DDR3', 2, 1, 2, 'PC-12800', 1600, 265000),
('TEAM Elite Sodimm 2GB', 'DDR3', 2, 1, 2, 'PC-12800', 1600, 245000),
('TEAM Sodimm 2GB', 'DDR2', 2, 1, 2, 'PC-6400', 800, 315000),
('TEAM Mac Edition 2GB PC3-10600', 'DDR3', 2, 1, 2, 'PC3-10600', 1333, 285000),
('KINGSTON Memory Notebook 2GB', 'DDR3', 2, 1, 2, 'PC-12800', 1600, 350560),
('TEAM Xtreem Dark Memory', 'DDR3', 8, 2, 16, 'PC3-19200', 2400, 1985500),
('TEAM T-Force Vulcan Memory', 'DDR4', 4, 1, 4, 'PC4-2400', 3000, 615000);

-- --------------------------------------------------------

--
-- Table structure for table `vga`
--

CREATE TABLE `vga` (
  `nama_vga` varchar(100) NOT NULL,
  `form_factor` varchar(50) NOT NULL,
  `ukuran_memori` int(3) DEFAULT NULL,
  `tipe_memori` varchar(10) DEFAULT NULL,
  `tdp` int(5) DEFAULT NULL,
  `core_clock` int(5) DEFAULT NULL,
  `harga` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vga`
--

INSERT INTO `vga` (`nama_vga`, `form_factor`, `ukuran_memori`, `tipe_memori`, `tdp`, `core_clock`, `harga`) VALUES
('Asus - Radeon RX550-2G', 'ITX', 2, 'GDDR5', 65, 1183, 1450000),
('Gigabyte - GT 1030 Low Profile 2G', 'Low Profile', 2, 'GDDR4', 30, 1227, 1410000),
('MSI - GeForce GT 1030 Aero ITX 2GD4 OC', 'ITX', 2, 'GDDR5', 20, 1189, 1319000),
('Asus - PH-GTX1050-2G', 'ATX', 2, 'GDDR5', 75, 1354, 2300000),
('MSI-GeForce GTX 1050 Aero ITX 2G OCV1', 'ITX', 2, 'GDDR5', 75, 1404, 2099000),
('Asus-ROG STRIX-GTX1050TI-O4G-GAMING', 'ATX', 2, 'GDDR5', 75, 1379, 3650000),
('Digital Alliance-GeForce GTX 1050 Ti Dual OC', 'ATX', 4, 'GDDR5', 75, 1366, 3020000),
('Asus-ROG STRIX-GTX1060-O6G-GAMING', 'ATX', 6, 'GDDR5', 120, 1620, 6200000),
('Asus-ROG STRIX-GTX1070-O8G-GAMING', 'ATX', 8, 'GDDR5', 150, 1632, 7600000),
('Inno3D-GeForce GTX 1070 iChill X4', 'ATX', 8, 'GDDR5', 190, 1620, 7500000),
('MSI-GeForce GTX 1070 Ti Armor 8G', 'ATX', 8, 'GDDR5', 180, 1607, 7349000),
('MSI-GeForce RTX 2070 Gaming Z 8G', 'ATX', 11, 'GDDR6X', 300, 1410, 11199000),
('Digital Alliance-GeForce GTX 1070 Ti Dual', 'ATX', 8, 'GDDR5', 180, 1607, 7000000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
