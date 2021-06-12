-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jun 12, 2021 at 11:42 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokolaptop`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `username` int(11) NOT NULL,
  `password` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `detailproduct`
--

CREATE TABLE `detailproduct` (
  `idstock` int(11) NOT NULL,
  `idlap` int(11) NOT NULL,
  `tanggal` date NOT NULL,
  `jumlahbarang` int(11) NOT NULL,
  `jumlahterjual` int(11) NOT NULL,
  `hargajual` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `detailproduct`
--

INSERT INTO `detailproduct` (`idstock`, `idlap`, `tanggal`, `jumlahbarang`, `jumlahterjual`, `hargajual`) VALUES
(1, 1, '2021-05-04', 10, 10, 8000000),
(2, 2, '2021-05-04', 9, 1, 10000);

-- --------------------------------------------------------

--
-- Table structure for table `infotoko`
--

CREATE TABLE `infotoko` (
  `idtoko` int(11) NOT NULL,
  `namaToko` text NOT NULL,
  `pemilikToko` text NOT NULL,
  `alamatToko` text NOT NULL,
  `emailtoko` text NOT NULL,
  `tlptoko` text NOT NULL,
  `igtoko` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `infotoko`
--

INSERT INTO `infotoko` (`idtoko`, `namaToko`, `pemilikToko`, `alamatToko`, `emailtoko`, `tlptoko`, `igtoko`) VALUES
(1, 'Toko laptop', 'unknown', 'jl,jember,Jember Kecamatan Kaliwates, Kabupaten Jember, Jawa Timur, Indonesia', 'tokolaptop@email.com', '080808080808', '@toko___laptop');

-- --------------------------------------------------------

--
-- Table structure for table `promo`
--

CREATE TABLE `promo` (
  `idpromo` int(11) NOT NULL,
  `namapromo` text NOT NULL,
  `potonganharga` int(11) NOT NULL,
  `durasi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `promo`
--

INSERT INTO `promo` (`idpromo`, `namapromo`, `potonganharga`, `durasi`) VALUES
(1, 'hujan besar', 25000, '23-03 sampai 30-03 2022'),
(2, 'batu loncat', 5000, '1-20 sampai 3-2 2022');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `id_romm` int(11) NOT NULL,
  `roomcode` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `saran`
--

CREATE TABLE `saran` (
  `id_saran` int(11) NOT NULL,
  `saran` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `saran`
--

INSERT INTO `saran` (`id_saran`, `saran`) VALUES
(1, 'gk papa'),
(2, 'gk jadi');

-- --------------------------------------------------------

--
-- Table structure for table `spesifikasi`
--

CREATE TABLE `spesifikasi` (
  `idlap` int(11) NOT NULL,
  `nama` text NOT NULL,
  `Processor` text NOT NULL,
  `Ram` text NOT NULL,
  `Display` text NOT NULL,
  `SistemOperasi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `spesifikasi`
--

INSERT INTO `spesifikasi` (`idlap`, `nama`, `Processor`, `Ram`, `Display`, `SistemOperasi`) VALUES
(1, 'dummy', 'dummy 1', '8', '116 inch', 'windows'),
(2, 'toshita', 'insel', '8 gb', '116 inch', 'widows 9');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Indexes for table `detailproduct`
--
ALTER TABLE `detailproduct`
  ADD PRIMARY KEY (`idstock`),
  ADD KEY `idlap` (`idlap`);

--
-- Indexes for table `infotoko`
--
ALTER TABLE `infotoko`
  ADD PRIMARY KEY (`idtoko`);

--
-- Indexes for table `promo`
--
ALTER TABLE `promo`
  ADD PRIMARY KEY (`idpromo`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id_romm`);

--
-- Indexes for table `saran`
--
ALTER TABLE `saran`
  ADD PRIMARY KEY (`id_saran`);

--
-- Indexes for table `spesifikasi`
--
ALTER TABLE `spesifikasi`
  ADD PRIMARY KEY (`idlap`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `detailproduct`
--
ALTER TABLE `detailproduct`
  MODIFY `idstock` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `infotoko`
--
ALTER TABLE `infotoko`
  MODIFY `idtoko` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `promo`
--
ALTER TABLE `promo`
  MODIFY `idpromo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `id_romm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `saran`
--
ALTER TABLE `saran`
  MODIFY `id_saran` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `spesifikasi`
--
ALTER TABLE `spesifikasi`
  MODIFY `idlap` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `detailproduct`
--
ALTER TABLE `detailproduct`
  ADD CONSTRAINT `detailproduct_ibfk_1` FOREIGN KEY (`idlap`) REFERENCES `spesifikasi` (`idlap`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
