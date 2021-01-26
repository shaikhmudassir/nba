-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 26, 2021 at 01:28 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
  `ese_th` int(5) NOT NULL,
  `ese_prh` int(5) NOT NULL,
  `ct` int(5) NOT NULL,
  `mp` int(5) NOT NULL,
  `ese_pra` int(5) NOT NULL,
  `pr_pa` int(5) NOT NULL,
  `userId` int(10) NOT NULL,
  `filename` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `Id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `Id` int(11) NOT NULL,
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

CREATE TABLE `studentlist` (
  `Id` int(11) NOT NULL,
  `rollNo` int(11) NOT NULL,
  `enrollNo` int(11) NOT NULL,
  `studentsName` text NOT NULL,
  `fieldId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `test1`
--

CREATE TABLE `test1` (
  `Id` int(11) NOT NULL,
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
  `Id` int(11) NOT NULL,
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
  `Id` int(11) NOT NULL,
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
  `Id` int(11) NOT NULL,
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
  `Id` int(11) NOT NULL,
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
  ADD PRIMARY KEY (`Id`) USING BTREE,
  ADD UNIQUE KEY `id` (`Id`);

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
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `test1`
--
ALTER TABLE `test1`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `test2`
--
ALTER TABLE `test2`
  ADD PRIMARY KEY (`Id`);

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
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `total_prpa`
--
ALTER TABLE `total_prpa`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `total_test1`
--
ALTER TABLE `total_test1`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `total_test2`
--
ALTER TABLE `total_test2`
  ADD PRIMARY KEY (`Id`);

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
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test1`
--
ALTER TABLE `test1`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test2`
--
ALTER TABLE `test2`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_prpa`
--
ALTER TABLE `total_prpa`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_test1`
--
ALTER TABLE `total_test1`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `total_test2`
--
ALTER TABLE `total_test2`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
