-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2021 at 09:56 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nba`
--

-- --------------------------------------------------------

--
-- Table structure for table `comapping`
--

CREATE TABLE `comapping` (
  `Id` int(11) NOT NULL,
  `coCode` varchar(20) NOT NULL,
  `statement` text NOT NULL,
  `po1` int(5) DEFAULT NULL,
  `po2` int(5) DEFAULT NULL,
  `po3` int(5) DEFAULT NULL,
  `po4` int(5) DEFAULT NULL,
  `po5` int(5) DEFAULT NULL,
  `po6` int(5) DEFAULT NULL,
  `po7` int(5) DEFAULT NULL,
  `pso1` int(5) DEFAULT NULL,
  `pso2` int(5) DEFAULT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `comapping`
--

INSERT INTO `comapping` (`Id`, `coCode`, `statement`, `po1`, `po2`, `po3`, `po4`, `po5`, `po6`, `po7`, `pso1`, `pso2`, `fieldId`) VALUES
(1, 'CO008.1', 's1', 3, 3, 0, 0, 0, 0, 0, 0, 0, 1),
(2, 'CO008.2', 's2', 2, 2, 0, 0, 2, 0, 0, 0, 0, 1),
(3, 'CO008.3', 's3', 2, 2, 2, 3, 0, 0, 0, 3, 0, 1),
(4, 'CO008.4', 's4', 3, 3, 0, 0, 0, 0, 0, 0, 0, 1),
(5, 'CO008.5', 's5', 2, 2, 0, 1, 3, 0, 1, 0, 0, 1),
(6, 'CO008.6', 's6', 2, 2, 2, 1, 0, 0, 1, 0, 0, 1),
(7, 'CO443.1', 'jh', 9, 9, 9, 9, 9, 9, 9, 9, 9, 7),
(8, 'C000.1', 'lij;o', 87, 7, 7, 7, 7, 7, 7, 7, 7, 8),
(9, 'C000.2', 'kjnkj', 5, 4, 3, 3, 323, 3, 3, 3, 3, 8),
(10, 'C000.3', 'lkl', 9, 9, 99, 9, 0, 9, 9, 9, 9, 8);

-- --------------------------------------------------------

--
-- Table structure for table `index`
--

CREATE TABLE `index` (
  `Id` int(11) NOT NULL,
  `academicYear` varchar(10) NOT NULL,
  `semester` int(5) NOT NULL,
  `faculty` text NOT NULL,
  `subject` text NOT NULL,
  `subjectCode` int(10) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  `courseSemester` varchar(10) NOT NULL,
  `coCode` varchar(10) NOT NULL,
  `th` int(5) NOT NULL,
  `poe` int(5) NOT NULL,
  `tw` int(5) NOT NULL,
  `avgMarks` int(5) NOT NULL,
  `userId` int(10) NOT NULL,
  `filename` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `index`
--

INSERT INTO `index` (`Id`, `academicYear`, `semester`, `faculty`, `subject`, `subjectCode`, `abbreviation`, `courseSemester`, `coCode`, `th`, `poe`, `tw`, `avgMarks`, `userId`, `filename`) VALUES
(1, '2020-21', 3, 'Khan sir', 'Science', 20015, 'BMA', 'CO3I', 'CO008', 70, 0, 30, 50, 1, 'BMA2020-21.csv'),
(2, '2021-22', 5, 'Patil sir', 'Netwotk', 45671, 'DCC', 'CO5I', 'CO0051', 40, 0, 60, 50, 1, 'DCC2021-22.csv'),
(3, '2020-21', 3, 'aaaa', 'Physics', 46814, 'aaa', 'aaa', 'CO1001', 70, 0, 30, 45, 2, NULL),
(4, '2021-22', 6, 'ZZ', 'kuch Bhi', 12213, '23', 'bbb', '213', 12, 12, 12, 65, 1, 'Book1.csv'),
(5, 'dfds', 2, 'dfgdf', 'dfgdf', 546, 'fdgdf', 'fgdd', 'dfgdf', -4545454, -456, -56, 456, 1, NULL),
(6, '2020-21', 1, 'ABC', 'maths', 1226, 'XYZ', 'CO2I', 'C000', 2, 1, 3, 50, 4, 'XYZ2020-21.csv'),
(7, '2020-21', 3, 'ABC', 'maths', 112, 'AB', 'CO22', 'CO443', 2, 2, 5, 6, 4, NULL),
(8, '2020-21', 1, 'ABC', 'maths', -1, 'XYZ', 'CO2I', 'C000', -1, -1, -1, -1, 4, NULL),
(9, '2020-21', 1, 'ABC', 'maths', -1, 'XYZ', 'CO2I', 'C000', -1, -1, -1, -1, 4, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Id`, `username`, `password`) VALUES
(1, 'khansir', 'pbkdf2:sha256:150000$jllcfg4p$b3227221474afc5ebfd9a77111c34eb468b1248fd9b1e1bde6cdaa2a3a5c2c4f'),
(2, 'test', 'pbkdf2:sha256:150000$zgV75bD7$00836c4cf27f1402fa1012816489446d002e8f55c9e1ae7c82494b2be030a53a'),
(3, 'test2', 'pbkdf2:sha256:150000$6YLiDEyF$e7622286ed2019d13d92650c4f7445c69197bd08beb6f3b0290da741219d33d5'),
(4, 'abc', 'pbkdf2:sha256:150000$XM8eNW0s$e3d5a8f47bc0471f6ece5a55f057f8fcaf4ef933baf16342313bf1dc23b5eda3');

-- --------------------------------------------------------

--
-- Table structure for table `msbte`
--

CREATE TABLE `msbte` (
  `id` int(11) NOT NULL,
  `Rollno` int(11) NOT NULL,
  `StudentName` varchar(200) NOT NULL,
  `TH` int(11) NOT NULL,
  `PR` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `prpa`
--

CREATE TABLE `prpa` (
  `id` int(11) NOT NULL DEFAULT 0,
  `Rollno` int(11) NOT NULL,
  `StudentName` varchar(200) NOT NULL,
  `CO1` int(11) NOT NULL,
  `CO2` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL,
  `CO3` int(11) NOT NULL,
  `CO4` int(11) NOT NULL,
  `CO5` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentlist`
--

CREATE TABLE `studentlist` (
  `id` int(11) NOT NULL,
  `rollNo` int(11) NOT NULL,
  `enrollNo` int(11) NOT NULL,
  `studentsName` text NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `studentlist`
--

INSERT INTO `studentlist` (`id`, `rollNo`, `enrollNo`, `studentsName`, `fieldId`) VALUES
(1, 33101, 1215010305, ' SURADKAR JAYASHREE BHAGAJI', 6),
(2, 33102, 1315010150, ' DEHADRAY SHIVANI RAJENDRA', 6),
(3, 33103, 1415010092, ' WANKHEDE POOJA DIPAK', 6),
(4, 33104, 1415010202, ' SUHAS SANJAY DEHADE', 6),
(5, 33105, 1515010031, ' SHAHANE KOMAL KARBHARI', 6),
(6, 33106, 1515010036, ' SABLE SHRADDHA VIJAY', 6),
(7, 33107, 1515010044, ' PADME AARTI NAMDEO', 6),
(8, 33108, 1515010046, ' BANKAR SWAPNIL RAJU', 6),
(9, 33109, 1515010048, ' GAIKWAD ASHWINI YASHWANT', 6),
(10, 33110, 1515010051, ' SHARDUL NEHA ROHIDAS', 6),
(11, 33111, 1515010101, 'HAREL GEETANJALI BHAGWAN', 6),
(12, 33112, 1515010104, 'JOSHI SHUBHANGI LAXMIKANT ', 6),
(13, 33113, 1515010106, ' NIKAM VARSHA PRAKASH', 6),
(14, 33114, 1515010112, ' DANDEKAR RUTUJA VASANT', 6),
(15, 33115, 1515010118, ' SHUKLA SAMRUDHI GOPALKRISHNA', 6),
(16, 33116, 1515010126, ' MOGRE RUCHITA RAMESHWAR', 6),
(17, 33117, 1515010137, ' KHAN MOHAMMED SOHAIL ', 6),
(18, 33118, 1515010140, 'JOSHI PRATHMESH NANDKUMAR', 6),
(19, 33119, 1615010001, 'PATIL DHANASHREE KRISHNA', 6),
(20, 33120, 1615010021, ' SONAWANE MANISHA RAOSAHEB', 6),
(21, 33121, 1615010028, ' KACHWAH GAYATRI AJMATSINH', 6),
(22, 33122, 1615010022, ' GIGANI AFZAL AKBAR', 6),
(23, 33123, 1615010032, ' KAMBLE AMOL SUNIL', 6),
(24, 33124, 1615010035, ' KALLOLE SAKSHI SHRINIVAS', 6),
(25, 33125, 1615010038, ' DESHPANDE REVATI PRASHANT', 6),
(26, 33126, 1615010040, ' PANMAND TEJAL SAMPAT', 6),
(27, 33127, 1615010042, ' PANDHEKAR SHRIKANT RAJESH', 6),
(28, 33128, 1615010046, ' TANGADE PRIYA PRASHANT', 6),
(29, 33129, 1615010050, ' POPHALE ABHISHEK LAXMIKANT', 6),
(30, 33130, 1615010061, ' GADGILE KISHORI KAILAS', 6),
(31, 33131, 1615010063, ' KUTE AMRUTA SANJAY', 6),
(32, 33132, 1615010069, ' ROHOKALE PALLAVI SURESH', 6),
(33, 33133, 1615010071, ' GANGAWANE PRATIKSHA RAJENDRA', 6),
(34, 33134, 1615010073, ' SABIR MUSTANSIR ABDEALI', 6),
(35, 33135, 1615010074, ' SANKAYE MANSI SATISH', 6),
(36, 33136, 1615010101, ' BULDAK MUKESHKUMAR KESHARRAM', 6),
(37, 33137, 1615010106, ' PANDE SAKSHI SHAILESH', 6),
(38, 33138, 1615010107, ' SHERE SHALAKA SHASHIR', 6),
(39, 33139, 1615010111, ' PATHARE RUTUJA PRAVIN', 6),
(40, 33140, 1615010120, ' KHADKE SHUBHANGI LAXMAN', 6),
(41, 33141, 1615010124, ' GIRGAONKAR DIKSHA LAXMIKANT', 6),
(42, 33142, 1615010131, ' SARODE ABHISHEK SANJEEV', 6),
(43, 33143, 1615010135, ' KULKARNI PRATIK RAHUL', 6),
(44, 33144, 1615010138, ' CHAVAN SNEHA BABASAHEB', 6),
(45, 33145, 1615010140, ' BHIVSANE PALLAVI PRADIP', 6),
(46, 33146, 1615010150, ' JOSHI KALYANI PANDURANG', 6),
(47, 33147, 1615010155, ' PATIL KUNDAN RAJENDRA', 6),
(48, 33148, 1615010165, ' MAHALANKAR SAURADH SANJAY', 6),
(49, 33149, 1615010168, ' BAHIWAL NEHA VIJAY', 6),
(50, 33150, 1615010185, ' MENDHE RAVI PARASHRAM', 6),
(51, 33151, 1615010188, ' MENDHE RAJ PARASHRAM', 6),
(52, 33152, 1615010273, ' WAGH JAGRUTI SUNIL', 6),
(53, 33153, 1615010274, ' GODSE POOJA PANDHARINATH', 6),
(54, 33154, 1615010276, ' LAHANE NIKITA UTTAM', 6),
(55, 33155, 1715010053, ' DOBHAL SHUBHAM RAMCHANDRA', 6),
(56, 33156, 1715010056, ' SHAIKH SABIR SHAIKH TAHER', 6),
(57, 33157, 1715010057, ' TRISHITA PANJA', 6),
(58, 33158, 1715010058, ' KHODASKAR SHREYASH PRASHANT', 6),
(59, 33159, 1715010060, ' SAWANDKAR SUDARSHAN BALAJI', 6),
(60, 33160, 1715010061, ' PATHAK JAYESH PRAMOD', 6),
(61, 33161, 1715010064, ' SHAIKH IRFAN SHAFEEK', 6),
(62, 33162, 1715010065, ' GADKARI PRATHAMESH NARENDRA', 6),
(63, 33163, 1715010066, ' SHAIKH SARA MOHAMMED SAFIULLAH', 6),
(64, 33201, 1311540002, ' KAYANDE KRISHNA CHANDRAKANT', 6),
(65, 33206, 1515010073, ' BEDVE GAYATREE LALIT', 6),
(66, 33212, 1615010471, ' TATHE RISHIKESH RAJENDRA', 6),
(67, 33219, 1615010181, ' KACHWAH AMARESHSINH AJMATSINH', 6),
(68, 33220, 1615010261, ' MODI PRATIKSHA GOKULPRASAD', 6),
(69, 33229, 1416300008, ' SIDDAMSHETTY AKASH NAGRAJ', 6);

-- --------------------------------------------------------

--
-- Table structure for table `test1`
--

CREATE TABLE `test1` (
  `id` int(11) NOT NULL,
  `Rollno` int(11) NOT NULL,
  `StudentName` varchar(200) NOT NULL,
  `CO1_1` int(11) DEFAULT NULL,
  `CO1_2` int(11) NOT NULL,
  `CO1_3` int(11) NOT NULL,
  `CO2_1` int(11) NOT NULL,
  `CO2_2` int(11) NOT NULL,
  `CO2_3` int(11) NOT NULL,
  `CO3_1` int(11) NOT NULL,
  `CO3_2` int(11) DEFAULT NULL,
  `CO3_3` int(11) NOT NULL,
  `CO3_4` int(11) NOT NULL,
  `CO3_5` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `test2`
--

CREATE TABLE `test2` (
  `id` int(11) NOT NULL,
  `Rollno` int(11) NOT NULL,
  `StudentName` varchar(200) NOT NULL,
  `CO4_1` int(11) NOT NULL,
  `CO4_2` float NOT NULL,
  `CO4_3` int(11) NOT NULL,
  `CO4_4` float NOT NULL,
  `CO5_1` int(11) NOT NULL,
  `CO5_2` int(11) NOT NULL,
  `CO4_5` int(11) NOT NULL,
  `CO5_3` int(11) NOT NULL,
  `CO5_4` int(11) NOT NULL,
  `CO5_5` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `total_msbte`
--

CREATE TABLE `total_msbte` (
  `id` int(11) NOT NULL,
  `Total_TH` int(11) NOT NULL,
  `Total_PR` int(11) NOT NULL,
  `TH_Level` int(11) NOT NULL,
  `PR_Level` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `total_test1`
--

CREATE TABLE `total_test1` (
  `id` int(11) NOT NULL,
  `Total_CO1_1` int(11) NOT NULL,
  `Total_CO1_2` int(11) NOT NULL,
  `Total_CO1_3` int(11) NOT NULL,
  `Total_CO2_1` int(11) NOT NULL,
  `Total_CO2_2` int(11) NOT NULL,
  `Total_CO2_3` int(11) NOT NULL,
  `Total_CO3_1` int(11) NOT NULL,
  `Total_CO3_2` int(11) NOT NULL,
  `Total_CO3_3` int(11) NOT NULL,
  `Total_CO3_4` int(11) NOT NULL,
  `Total_CO3_5` int(11) NOT NULL,
  `CO1_Level` int(11) NOT NULL,
  `CO2_Level` int(11) NOT NULL,
  `CO3_Level` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `total_test2`
--

CREATE TABLE `total_test2` (
  `id` int(11) NOT NULL DEFAULT 0,
  `Total_CO4_1` int(11) NOT NULL,
  `Total_CO4_2` int(11) NOT NULL,
  `Total_CO4_3` int(11) NOT NULL,
  `Total_CO4_4` int(11) NOT NULL,
  `Total_CO5_1` int(11) NOT NULL,
  `Total_CO5_2` int(11) NOT NULL,
  `Total_CO4_5` int(11) NOT NULL,
  `Total_CO5_3` int(11) NOT NULL,
  `Total_CO5_4` int(11) NOT NULL,
  `Total_CO5_5` int(11) NOT NULL,
  `CO4_Level` int(11) NOT NULL,
  `CO5_Level` int(11) NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comapping`
--
ALTER TABLE `comapping`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `index`
--
ALTER TABLE `index`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `msbte`
--
ALTER TABLE `msbte`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `studentlist`
--
ALTER TABLE `studentlist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test1`
--
ALTER TABLE `test1`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test2`
--
ALTER TABLE `test2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `total_msbte`
--
ALTER TABLE `total_msbte`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `total_test1`
--
ALTER TABLE `total_test1`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comapping`
--
ALTER TABLE `comapping`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `index`
--
ALTER TABLE `index`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `msbte`
--
ALTER TABLE `msbte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `studentlist`
--
ALTER TABLE `studentlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `test1`
--
ALTER TABLE `test1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test2`
--
ALTER TABLE `test2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_msbte`
--
ALTER TABLE `total_msbte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_test1`
--
ALTER TABLE `total_test1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
