-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--

-- Tiempo de generación: 19-06-2023 a las 03:23:42
-- Versión del servidor: 5.5.62-0ubuntu0.14.04.1
-- Versión de PHP: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Attention_Control`
--

CREATE TABLE `Attention_Control` (
  `ID` int(11) NOT NULL,
  `FECHA` datetime NOT NULL,
  `NOMBRES` varchar(255) NOT NULL,
  `HORA_INGRESO` time NOT NULL,
  `HORA_SALIDA` time NOT NULL,
  `POLO_GIFT` tinyint(1) NOT NULL,
  `KEYCHAIN_GIFT` tinyint(1) NOT NULL,
  `CATALOG_BOOK` enum('Si','No') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Attention_Control`
--

INSERT INTO `Attention_Control` (`ID`, `FECHA`, `NOMBRES`, `HORA_INGRESO`, `HORA_SALIDA`, `POLO_GIFT`, `KEYCHAIN_GIFT`, `CATALOG_BOOK`) VALUES
(1, '2023-05-02 00:00:00', 'Jose Ponciano Carranza', '23:04:00', '13:06:00', 1, 1, 'Si'),
(2, '2023-05-31 00:00:00', 'Park Joe', '16:40:00', '16:42:00', 1, 1, 'Si'),
(3, '2023-05-31 00:00:00', 'Jose Ponciano', '15:42:00', '04:42:00', 0, 0, 'Si'),
(4, '2023-06-20 00:00:00', 'Americo Rojas', '22:30:00', '23:31:00', 1, 0, 'No'),
(5, '2023-06-21 00:00:00', 'Jose Ponciano', '21:26:00', '09:26:00', 0, 0, 'No'),
(6, '2023-06-13 00:00:00', 'Pedro Perez', '00:00:00', '00:00:00', 1, 0, 'Si'),
(7, '2023-06-13 00:00:00', 'Jhonny Cage', '17:00:00', '18:00:00', 0, 0, 'No'),
(8, '2023-06-08 00:00:00', 'Pedro Perez', '19:34:00', '21:36:00', 1, 1, 'No'),
(9, '2023-06-28 00:00:00', 'amalia caranza', '20:43:00', '21:32:00', 0, 0, 'Si'),
(10, '2023-06-22 00:00:00', 'Reinaldo DaSilva', '19:43:00', '18:44:00', 1, 1, 'Si'),
(11, '2023-06-01 00:00:00', 'Jose Ponciano', '12:07:00', '12:09:00', 1, 1, 'Si'),
(12, '2023-06-14 00:00:00', 'Valeria Carranza', '19:21:00', '20:23:00', 1, 0, 'No'),
(13, '2023-06-14 00:00:00', 'Horacio Perez', '20:30:00', '21:27:00', 1, 1, 'No'),
(14, '2023-06-14 00:00:00', 'Pedor Perez', '14:49:00', '02:49:00', 1, 1, 'Si'),
(15, '2023-06-13 00:00:00', 'amalia caranza', '12:12:00', '12:12:00', 1, 0, 'Si'),
(16, '2023-06-16 00:00:00', 'Pedro Perez', '00:00:00', '12:14:00', 1, 1, 'No'),
(17, '2023-06-08 00:00:00', 'Jose Ponciano', '12:30:00', '16:27:00', 1, 1, 'No'),
(19, '2023-06-13 00:00:00', 'Cristian Rodriguez', '11:00:00', '16:00:00', 1, 0, 'No'),
(20, '2023-06-12 00:00:00', 'Wilvert CONCHA', '16:36:00', '16:38:00', 1, 1, 'No'),
(21, '2023-06-13 00:00:00', 'Esther Mendoza Reyes', '18:45:00', '18:50:00', 1, 1, 'No');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Attention_Control`
--
ALTER TABLE `Attention_Control`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Attention_Control`
--
ALTER TABLE `Attention_Control`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
