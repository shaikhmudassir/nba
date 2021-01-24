Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@shaikhmudassir 
MDAffanMafia
/
nba
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
nba/nba.sql
@MDAffanMafia
MDAffanMafia Add files via upload
Latest commit f37d3b0 2 days ago
 History
 1 contributor
564 lines (474 sloc)  12.9 KB
  
-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2021 at 01:40 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

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

CREATE TABLE IF NOT EXISTS `comapping` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `comapping`
--

INSERT INTO `comapping` (`Id`, `coCode`, `statement`, `po1`, `po2`, `po3`, `po4`, `po5`, `po6`, `po7`, `pso1`, `pso2`, `fieldId`) VALUES
(1, 'CO008.1', 's1', 3, 3, 0, 0, 0, 0, 0, 0, 0, 1),
(2, 'CO008.2', 's2', 2, 2, 0, 0, 2, 0, 0, 0, 0, 1),
(3, 'CO008.3', 's3', 2, 2, 2, 3, 0, 0, 0, 3, 0, 1),
(4, 'CO008.4', 's4', 3, 3, 0, 0, 0, 0, 0, 0, 0, 1),
(5, 'CO008.5', 's5', 2, 2, 0, 1, 3, 0, 1, 0, 0, 1),
(6, 'CO008.6', 's6', 2, 2, 2, 1, 0, 0, 1, 0, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `index`
--

CREATE TABLE IF NOT EXISTS `index` (
`Id` int(11) NOT NULL,
  `academicYear` varchar(10) NOT NULL,
  `semester` int(5) NOT NULL,
  `faculty` text NOT NULL,
  `subject` text NOT NULL,
  `subjectCode` int(10) NOT NULL,
  `abbreviation` varchar(5) NOT NULL,
  `courseSemester` varchar(10) NOT NULL,
  `coCode` varchar(10) NOT NULL,
  `ese_th` int(5) NOT NULL,
  `ese_prh` int(5) NOT NULL,
  `ct` int(5) NOT NULL,
  `mp` int(5) NOT NULL,
  `ese_pra` int(5) NOT NULL,
  `pr_pa` int(5) NOT NULL,
  `userId` int(10) NOT NULL,
  `filename` varchar(30) DEFAULT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `index`
--

INSERT INTO `index` (`Id`, `academicYear`, `semester`, `faculty`, `subject`, `subjectCode`, `abbreviation`, `courseSemester`, `coCode`, `ese_th`, `ese_prh`, `ct`, `mp`, `ese_pra`, `pr_pa`, `userId`, `filename`) VALUES
(1, '2020-21', 3, 'Khan sir', 'Science', 20015, 'BMA', 'CO3I', 'CO008', 70, 0, 10, 50, 0, 0, 1, 'BMA2020-21.csv'),
(2, '2021-22', 5, 'Patil sir', 'Netwotk', 45671, 'DCC', 'CO5I', 'CO0051', 40, 0, 60, 50, 0, 0, 1, 'DCC2021-22.csv'),
(3, '2020-21', 3, 'aaaa', 'Physics', 46814, 'aaa', 'aaa', 'CO1001', 70, 0, 30, 45, 0, 0, 2, NULL),
(4, '2021-22', 6, 'ZZ', 'kuch Bhi', 12213, '23', 'bbb', '213', 12, 12, 12, 65, 0, 0, 1, 'Book1.csv'),
(5, 'dfds', 2, 'dfgdf', 'dfgdf', 546, 'fdgdf', 'fgdd', 'dfgdf', -4545454, -456, -56, 456, 0, 0, 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
`Id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`Id`, `username`, `password`) VALUES
(1, 'khansir', 'pbkdf2:sha256:150000$jllcfg4p$b3227221474afc5ebfd9a77111c34eb468b1248fd9b1e1bde6cdaa2a3a5c2c4f'),
(2, 'test', 'pbkdf2:sha256:150000$zgV75bD7$00836c4cf27f1402fa1012816489446d002e8f55c9e1ae7c82494b2be030a53a'),
(3, 'test2', 'pbkdf2:sha256:150000$6YLiDEyF$e7622286ed2019d13d92650c4f7445c69197bd08beb6f3b0290da741219d33d5');

-- --------------------------------------------------------

--
-- Table structure for table `micro_project`
--

CREATE TABLE `micro_project` (
  `Id` int(11) NOT NULL,
  `co1` int(3) DEFAULT NULL,
  `co2` int(3) DEFAULT NULL,
  `co3` int(3) DEFAULT NULL,
  `co4` int(3) DEFAULT NULL,
  `co5` int(3) DEFAULT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Table structure for table `po_attainment`
--

CREATE TABLE `po_attainment` (
  `Id` int(11) NOT NULL,
  `finalpo1` int(3) NOT NULL,
  `finalpo2` int(3) NOT NULL,
  `finalpo3` int(3) NOT NULL,
  `finalpo4` int(3) NOT NULL,
  `finalpo5` int(3) NOT NULL,
  `finalpo6` int(3) NOT NULL,
  `finalpo7` int(3) NOT NULL,
  `finalpo8` int(3) NOT NULL,
  `fieldId` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `practical_prpa`
--

CREATE TABLE `practical_prpa` (
  `Id` int(11) NOT NULL,
  `CO1` int(3) NOT NULL,
  `CO2` int(3) NOT NULL,
  `CO3` int(3) NOT NULL,
  `CO4` int(3) NOT NULL,
  `CO5` int(3) NOT NULL,
  `Total` int(3) NOT NULL,
  `fieldId` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `prpa`
--

CREATE TABLE `prpa` (
  `Id` int(11) NOT NULL,
  `rollNo` int(11) NOT NULL,
  `StudentName` text NOT NULL,
  `CO1` int(3) NOT NULL,
  `CO2` int(3) NOT NULL,
  `CO3` int(3) NOT NULL,
  `CO4` int(3) NOT NULL,
  `CO5` int(3) NOT NULL,
  `Marks_Obtained` int(3) NOT NULL,
  `fieldId` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `studentlist`
--

CREATE TABLE IF NOT EXISTS `studentlist` (
`id` int(11) NOT NULL,
  `rollNo` int(11) NOT NULL,
  `enrollNo` int(11) NOT NULL,
  `studentsName` text NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=415 ;

--
-- Dumping data for table `studentlist`
--

INSERT INTO `studentlist` (`id`, `rollNo`, `enrollNo`, `studentsName`, `fieldId`) VALUES
(1, 33101, 1215010305, 'Ariyan Motowani', 2),
(2, 33102, 1315010150, ' DEHADRAY SHIVANI RAJENDRA', 2),
(3, 33103, 1415010092, ' WANKHEDE POOJA DIPAK', 2),
(4, 33104, 1415010202, ' SUHAS SANJAY DEHADE', 2),
(5, 33105, 1515010031, ' SHAHANE KOMAL KARBHARI', 2),
(6, 33106, 1515010036, ' SABLE SHRADDHA VIJAY', 2),
(7, 33107, 1515010044, ' PADME AARTI NAMDEO', 2),
(8, 33108, 1515010046, ' BANKAR SWAPNIL RAJU', 2),
(9, 33109, 1515010048, ' GAIKWAD ASHWINI YASHWANT', 2),
(10, 33110, 1515010051, ' SHARDUL NEHA ROHIDAS', 2),
(11, 33111, 1515010101, 'HAREL GEETANJALI BHAGWAN', 2),
(12, 33112, 1515010104, 'JOSHI SHUBHANGI LAXMIKANT ', 2),
(13, 33113, 1515010106, ' NIKAM VARSHA PRAKASH', 2),
(14, 33114, 1515010112, ' DANDEKAR RUTUJA VASANT', 2),
(15, 33115, 1515010118, ' SHUKLA SAMRUDHI GOPALKRISHNA', 2),
(16, 33116, 1515010126, ' MOGRE RUCHITA RAMESHWAR', 2),
(17, 33117, 1515010137, ' KHAN MOHAMMED SOHAIL ', 2),
(18, 33118, 1515010140, 'JOSHI PRATHMESH NANDKUMAR', 2),
(19, 33119, 1615010001, 'PATIL DHANASHREE KRISHNA', 2),
(20, 33120, 1615010021, ' SONAWANE MANISHA RAOSAHEB', 2),
(21, 33121, 1615010028, ' KACHWAH GAYATRI AJMATSINH', 2),
(22, 33122, 1615010022, ' GIGANI AFZAL AKBAR', 2),
(23, 33123, 1615010032, ' KAMBLE AMOL SUNIL', 2),
(24, 33124, 1615010035, ' KALLOLE SAKSHI SHRINIVAS', 2),
(25, 33125, 1615010038, ' DESHPANDE REVATI PRASHANT', 2),
(26, 33126, 1615010040, ' PANMAND TEJAL SAMPAT', 2),
(27, 33127, 1615010042, ' PANDHEKAR SHRIKANT RAJESH', 2),
(28, 33128, 1615010046, ' TANGADE PRIYA PRASHANT', 2),
(29, 33129, 1615010050, ' POPHALE ABHISHEK LAXMIKANT', 2),
(30, 33130, 1615010061, ' GADGILE KISHORI KAILAS', 2),
(31, 33131, 1615010063, ' KUTE AMRUTA SANJAY', 2),
(32, 33132, 1615010069, ' ROHOKALE PALLAVI SURESH', 2),
(33, 33133, 1615010071, ' GANGAWANE PRATIKSHA RAJENDRA', 2),
(34, 33134, 1615010073, ' SABIR MUSTANSIR ABDEALI', 2),
(35, 33135, 1615010074, ' SANKAYE MANSI SATISH', 2),
(36, 33136, 1615010101, ' BULDAK MUKESHKUMAR KESHARRAM', 2),
(37, 33137, 1615010106, ' PANDE SAKSHI SHAILESH', 2),
(38, 33138, 1615010107, ' SHERE SHALAKA SHASHIR', 2),
(39, 33139, 1615010111, ' PATHARE RUTUJA PRAVIN', 2),
(40, 33140, 1615010120, ' KHADKE SHUBHANGI LAXMAN', 2),
(41, 33141, 1615010124, ' GIRGAONKAR DIKSHA LAXMIKANT', 2),
(42, 33142, 1615010131, ' SARODE ABHISHEK SANJEEV', 2),
(43, 33143, 1615010135, ' KULKARNI PRATIK RAHUL', 2),
(44, 33144, 1615010138, ' CHAVAN SNEHA BABASAHEB', 2),
(45, 33145, 1615010140, ' BHIVSANE PALLAVI PRADIP', 2),
(46, 33146, 1615010150, ' JOSHI KALYANI PANDURANG', 2),
(47, 33147, 1615010155, ' PATIL KUNDAN RAJENDRA', 2),
(48, 33148, 1615010165, ' MAHALANKAR SAURADH SANJAY', 2),
(49, 33149, 1615010168, ' BAHIWAL NEHA VIJAY', 2),
(50, 33150, 1615010185, ' MENDHE RAVI PARASHRAM', 2),
(51, 33151, 1615010188, ' MENDHE RAJ PARASHRAM', 2),
(52, 33152, 1615010273, ' WAGH JAGRUTI SUNIL', 2),
(53, 33153, 1615010274, ' GODSE POOJA PANDHARINATH', 2),
(54, 33154, 1615010276, ' LAHANE NIKITA UTTAM', 2),
(55, 33155, 1715010053, ' DOBHAL SHUBHAM RAMCHANDRA', 2),
(56, 33156, 1715010056, ' SHAIKH SABIR SHAIKH TAHER', 2),
(57, 33157, 1715010057, ' TRISHITA PANJA', 2),
(58, 33158, 1715010058, ' KHODASKAR SHREYASH PRASHANT', 2),
(59, 33159, 1715010060, ' SAWANDKAR SUDARSHAN BALAJI', 2),
(60, 33160, 1715010061, ' PATHAK JAYESH PRAMOD', 2),
(61, 33161, 1715010064, ' SHAIKH IRFAN SHAFEEK', 2),
(62, 33162, 1715010065, ' GADKARI PRATHAMESH NARENDRA', 2),
(63, 33163, 1715010066, ' SHAIKH SARA MOHAMMED SAFIULLAH', 2),
(64, 33201, 1311540002, ' KAYANDE KRISHNA CHANDRAKANT', 2),
(65, 33206, 1515010073, ' BEDVE GAYATREE LALIT', 2),
(66, 33212, 1615010471, ' TATHE RISHIKESH RAJENDRA', 2),
(67, 33219, 1615010181, ' KACHWAH AMARESHSINH AJMATSINH', 2),
(68, 33220, 1615010261, ' MODI PRATIKSHA GOKULPRASAD', 2),
(69, 33229, 1416300008, ' SIDDAMSHETTY AKASH NAGRAJ', 2),
(346, 33101, 1215010305, 'Ariyan Kulkarni', 1),
(347, 33102, 1315010150, ' DEHADRAY SHIVANI RAJENDRA', 1),
(348, 33103, 1415010092, ' WANKHEDE POOJA DIPAK', 1),
(349, 33104, 1415010202, ' SUHAS SANJAY DEHADE', 1),
(350, 33105, 1515010031, ' SHAHANE KOMAL KARBHARI', 1),
(351, 33106, 1515010036, ' SABLE SHRADDHA VIJAY', 1),
(352, 33107, 1515010044, ' PADME AARTI NAMDEO', 1),
(353, 33108, 1515010046, ' BANKAR SWAPNIL RAJU', 1),
(354, 33109, 1515010048, ' GAIKWAD ASHWINI YASHWANT', 1),
(355, 33110, 1515010051, ' SHARDUL NEHA ROHIDAS', 1),
(356, 33111, 1515010101, 'HAREL GEETANJALI BHAGWAN', 1),
(357, 33112, 1515010104, 'JOSHI SHUBHANGI LAXMIKANT ', 1),
(358, 33113, 1515010106, ' NIKAM VARSHA PRAKASH', 1),
(359, 33114, 1515010112, ' DANDEKAR RUTUJA VASANT', 1),
(360, 33115, 1515010118, ' SHUKLA SAMRUDHI GOPALKRISHNA', 1),
(361, 33116, 1515010126, ' MOGRE RUCHITA RAMESHWAR', 1),
(362, 33117, 1515010137, ' KHAN MOHAMMED SOHAIL ', 1),
(363, 33118, 1515010140, 'JOSHI PRATHMESH NANDKUMAR', 1),
(364, 33119, 1615010001, 'PATIL DHANASHREE KRISHNA', 1),
(365, 33120, 1615010021, ' SONAWANE MANISHA RAOSAHEB', 1),
(366, 33121, 1615010028, ' KACHWAH GAYATRI AJMATSINH', 1),
(367, 33122, 1615010022, ' GIGANI AFZAL AKBAR', 1),
(368, 33123, 1615010032, ' KAMBLE AMOL SUNIL', 1),
(369, 33124, 1615010035, ' KALLOLE SAKSHI SHRINIVAS', 1),
(370, 33125, 1615010038, ' DESHPANDE REVATI PRASHANT', 1),
(371, 33126, 1615010040, ' PANMAND TEJAL SAMPAT', 1),
(372, 33127, 1615010042, ' PANDHEKAR SHRIKANT RAJESH', 1),
(373, 33128, 1615010046, ' TANGADE PRIYA PRASHANT', 1),
(374, 33129, 1615010050, ' POPHALE ABHISHEK LAXMIKANT', 1),
(375, 33130, 1615010061, ' GADGILE KISHORI KAILAS', 1),
(376, 33131, 1615010063, ' KUTE AMRUTA SANJAY', 1),
(377, 33132, 1615010069, ' ROHOKALE PALLAVI SURESH', 1),
(378, 33133, 1615010071, ' GANGAWANE PRATIKSHA RAJENDRA', 1),
(379, 33134, 1615010073, ' SABIR MUSTANSIR ABDEALI', 1),
(380, 33135, 1615010074, ' SANKAYE MANSI SATISH', 1),
(381, 33136, 1615010101, ' BULDAK MUKESHKUMAR KESHARRAM', 1),
(382, 33137, 1615010106, ' PANDE SAKSHI SHAILESH', 1),
(383, 33138, 1615010107, ' SHERE SHALAKA SHASHIR', 1),
(384, 33139, 1615010111, ' PATHARE RUTUJA PRAVIN', 1),
(385, 33140, 1615010120, ' KHADKE SHUBHANGI LAXMAN', 1),
(386, 33141, 1615010124, ' GIRGAONKAR DIKSHA LAXMIKANT', 1),
(387, 33142, 1615010131, ' SARODE ABHISHEK SANJEEV', 1),
(388, 33143, 1615010135, ' KULKARNI PRATIK RAHUL', 1),
(389, 33144, 1615010138, ' CHAVAN SNEHA BABASAHEB', 1),
(390, 33145, 1615010140, ' BHIVSANE PALLAVI PRADIP', 1),
(391, 33146, 1615010150, ' JOSHI KALYANI PANDURANG', 1),
(392, 33147, 1615010155, ' PATIL KUNDAN RAJENDRA', 1),
(393, 33148, 1615010165, ' MAHALANKAR SAURADH SANJAY', 1),
(394, 33149, 1615010168, ' BAHIWAL NEHA VIJAY', 1),
(395, 33150, 1615010185, ' MENDHE RAVI PARASHRAM', 1),
(396, 33151, 1615010188, ' MENDHE RAJ PARASHRAM', 1),
(397, 33152, 1615010273, ' WAGH JAGRUTI SUNIL', 1),
(398, 33153, 1615010274, ' GODSE POOJA PANDHARINATH', 1),
(399, 33154, 1615010276, ' LAHANE NIKITA UTTAM', 1),
(400, 33155, 1715010053, ' DOBHAL SHUBHAM RAMCHANDRA', 1),
(401, 33156, 1715010056, ' SHAIKH SABIR SHAIKH TAHER', 1),
(402, 33157, 1715010057, ' TRISHITA PANJA', 1),
(403, 33158, 1715010058, ' KHODASKAR SHREYASH PRASHANT', 1),
(404, 33159, 1715010060, ' SAWANDKAR SUDARSHAN BALAJI', 1),
(405, 33160, 1715010061, ' PATHAK JAYESH PRAMOD', 1),
(406, 33161, 1715010064, ' SHAIKH IRFAN SHAFEEK', 1),
(407, 33162, 1715010065, ' GADKARI PRATHAMESH NARENDRA', 1),
(408, 33163, 1715010066, ' SHAIKH SARA MOHAMMED SAFIULLAH', 1),
(409, 33201, 1311540002, ' KAYANDE KRISHNA CHANDRAKANT', 1),
(410, 33206, 1515010073, ' BEDVE GAYATREE LALIT', 1),
(411, 33212, 1615010471, ' TATHE RISHIKESH RAJENDRA', 1),
(412, 33219, 1615010181, ' KACHWAH AMARESHSINH AJMATSINH', 1),
(413, 33220, 1615010261, ' MODI PRATIKSHA GOKULPRASAD', 1),
(414, 33229, 1416300008, ' SIDDAMSHETTY AKASH NAGRAJ', 1);

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
-- Table structure for table `total_attainment`
--

CREATE TABLE `total_attainment` (
  `Id` int(11) NOT NULL,
  `CO1_level` int(3) DEFAULT NULL,
  `CO2_level` int(3) DEFAULT NULL,
  `CO3_level` int(3) DEFAULT NULL,
  `CO4_level` int(3) DEFAULT NULL,
  `CO5_level` int(3) DEFAULT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `total_micro_project`
--

CREATE TABLE `total_micro_project` (
  `Id` int(11) NOT NULL,
  `nostudents_attempted_Co1` int(6) NOT NULL,
  `nostudents_attempted_Co2` int(6) NOT NULL,
  `nostudents_attempted_Co3` int(6) NOT NULL,
  `nostudents_attempted_Co4` int(6) NOT NULL,
  `nostudents_attempted_Co5` int(6) NOT NULL,
  `nostudents_more_than_avgMarks_Co1` int(6) NOT NULL,
  `nostudents_more_than_avgMarks_Co2` int(6) NOT NULL,
  `nostudents_more_than_avgMarks_Co3` int(6) NOT NULL,
  `nostudents_more_than_avgMarks_Co4` int(6) NOT NULL,
  `nostudents_more_than_avgMarks_Co5` int(6) NOT NULL,
  `per_of_students_more_than_avgMarks_Co1` float NOT NULL,
  `per_of_students_more_than_avgMarks_Co2` float NOT NULL,
  `per_of_students_more_than_avgMarks_Co3` float NOT NULL,
  `per_of_students_more_than_avgMarks_Co4` float NOT NULL,
  `per_of_students_more_than_avgMarks_Co5` float NOT NULL,
  `attainment_level_acheived_Co1` int(3) NOT NULL,
  `attainment_level_acheived_Co2` int(3) NOT NULL,
  `attainment_level_acheived_Co3` int(3) NOT NULL,
  `attainment_level_acheived_Co4` int(3) NOT NULL,
  `attainment_level_acheived_Co5` int(3) NOT NULL,
  `fieldId` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Table structure for table `total_prpa`
--

CREATE TABLE `total_prpa` (
  `Id` int(11) NOT NULL,
  `Total_CO1` int(3) NOT NULL,
  `Total_CO2` int(3) NOT NULL,
  `Total_CO3` int(3) NOT NULL,
  `Total_CO4` int(3) NOT NULL,
  `Total_CO5` int(3) NOT NULL,
  `Level_CO1` int(3) NOT NULL,
  `Level_CO2` int(2) NOT NULL,
  `Level_CO3` int(3) NOT NULL,
  `Level_CO4` int(3) NOT NULL,
  `Level_CO5` int(3) NOT NULL,
  `fieldId` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `id` int(11) NOT NULL DEFAULT '0',
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
-- Indexes for table `micro_project`
--
ALTER TABLE `micro_project`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `msbte`
--
ALTER TABLE `msbte`
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `po_attainment`
--
ALTER TABLE `po_attainment`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `practical_prpa`
--
ALTER TABLE `practical_prpa`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `prpa`
--
ALTER TABLE `prpa`
  ADD PRIMARY KEY (`Id`);

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
-- Indexes for table `total_attainment`
--
ALTER TABLE `total_attainment`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `total_micro_project`
--
ALTER TABLE `total_micro_project`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `total_msbte`
--
ALTER TABLE `total_msbte`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `total_prpa`
--
ALTER TABLE `total_prpa`
  ADD PRIMARY KEY (`Id`);

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
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `index`
--
ALTER TABLE `index`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `micro_project`
--
ALTER TABLE `micro_project`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `msbte`
--
ALTER TABLE `msbte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `po_attainment`
--
ALTER TABLE `po_attainment`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `practical_prpa`
--
ALTER TABLE `practical_prpa`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `prpa`
--
ALTER TABLE `prpa`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `studentlist`
--
ALTER TABLE `studentlist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `total_attainment`
--
ALTER TABLE `total_attainment`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_micro_project`
--
ALTER TABLE `total_micro_project`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_msbte`
--
ALTER TABLE `total_msbte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_prpa`
--
ALTER TABLE `total_prpa`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_test1`
--
ALTER TABLE `total_test1`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
