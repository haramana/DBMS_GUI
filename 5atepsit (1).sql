-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2023 at 03:32 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Table structure for table `dipendenti_harman_singh`
--

CREATE TABLE `dipendenti_harman_singh` (
  `id` int(255) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `posizione_lavorativa` varchar(30) NOT NULL,
  `data_assunzione` date NOT NULL,
  `eta` int(99) NOT NULL,
  `indirizzo` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `dipendenti_harman_singh`
--

INSERT INTO `dipendenti_harman_singh` (`id`, `nome`, `cognome`, `posizione_lavorativa`, `data_assunzione`, `eta`, `indirizzo`) VALUES
(1, 'harman', 'singh', 'operaio', '2023-10-10', 18, 'rio saliceto'),
(2, 'niccolo', 'martucci', 'operaio', '2023-10-10', 18, 'rio saliceto'),
(3, 'davide', 'kasaro', 'operaio', '2023-10-10', 18, 'rio saliceto'),
(41, 'dario', 'foroni', 'contadino', '2005-10-17', 18, 'mandriolo'),
(48, 'lorenzo', 'arfeli', 'studente', '2000-12-12', 23, 'correggio');

-- --------------------------------------------------------

--
-- Table structure for table `utenti`
--

CREATE TABLE `utenti` (
  `username` varchar(100) NOT NULL,
  `identification` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `utenti`
--

INSERT INTO `utenti` (`username`, `identification`) VALUES
('ADMIN', '6613ddd54d6db890ec06519714257dd4c2abe8080229c86c900b57fa7552a8ec'),
('junior', 'c6423418192890e12d98954399a9ff89c1e0f3b53da50709ad51a98abec737a3');

-- --------------------------------------------------------

--
-- Table structure for table `zone_di_lavoro_harman_singh`
--

CREATE TABLE `zone_di_lavoro_harman_singh` (
  `id_zona` int(11) NOT NULL,
  `nome_zona` varchar(100) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `id_dipendente` int(11) NOT NULL,
  `reparto` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `zone_di_lavoro_harman_singh`
--

INSERT INTO `zone_di_lavoro_harman_singh` (`id_zona`, `nome_zona`, `numero_clienti`, `id_dipendente`, `reparto`) VALUES
(1, 'correggio', 10, 48, 'IT');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dipendenti_harman_singh`
--
ALTER TABLE `dipendenti_harman_singh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `zone_di_lavoro_harman_singh`
--
ALTER TABLE `zone_di_lavoro_harman_singh`
  ADD PRIMARY KEY (`id_zona`),
  ADD KEY `id_dipendente` (`id_dipendente`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dipendenti_harman_singh`
--
ALTER TABLE `dipendenti_harman_singh`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `zone_di_lavoro_harman_singh`
--
ALTER TABLE `zone_di_lavoro_harman_singh`
  MODIFY `id_zona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `zone_di_lavoro_harman_singh`
--
ALTER TABLE `zone_di_lavoro_harman_singh`
  ADD CONSTRAINT `zone_di_lavoro_harman_singh_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendenti_harman_singh` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
