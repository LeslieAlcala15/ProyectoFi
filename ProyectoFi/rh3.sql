-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-11-2022 a las 08:19:28
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `rh3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cubierta`
--

CREATE TABLE `cubierta` (
  `idCubierta` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cubierta`
--

INSERT INTO `cubierta` (`idCubierta`, `descripcion`) VALUES
(2, 'Buttercream'),
(3, 'Chantilly'),
(4, 'Ganache'),
(5, 'Glasa Real'),
(6, 'Merengue'),
(7, 'Fondant'),
(8, 'Chocolate');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `decoraciones`
--

CREATE TABLE `decoraciones` (
  `idDecoraciones` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `decoraciones`
--

INSERT INTO `decoraciones` (`idDecoraciones`, `descripcion`) VALUES
(3, 'Chispas comestibles'),
(4, 'Fruta'),
(5, 'Chocolate'),
(6, 'Imagen Comestible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encargo`
--

CREATE TABLE `encargo` (
  `idEncargo` int(11) NOT NULL,
  `folio` varchar(25) NOT NULL,
  `fechapedido` date NOT NULL,
  `fechaautorizacion` date NOT NULL,
  `fechaentrega` date NOT NULL,
  `bancos` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipopago` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizados` tinyint(1) NOT NULL,
  `idPedido` int(11) NOT NULL,
  `idTipopan` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `encargo`
--

INSERT INTO `encargo` (`idEncargo`, `folio`, `fechapedido`, `fechaautorizacion`, `fechaentrega`, `bancos`, `motivoEspecifique`, `tipopago`, `nomSolicita`, `nomAutoriza`, `nomRevisa`, `autorizados`, `idPedido`, `idTipopan`) VALUES
(10, '46', '0000-00-00', '2022-11-18', '2022-12-01', 'Baja', '', 'Temporal', 'gfnfn', '', '', 0, 19, 0),
(11, '6436', '2022-11-09', '2022-11-10', '2022-11-25', 'Baja', '', 'Permanente', 'hgfh', '', '', 0, 19, 2),
(12, '1234', '2022-11-21', '2022-11-22', '2022-12-01', 'Baja', '', 'Temporal', 'Maria Torrez (Avenida Arqueros, Ags, AGS, #132)', '', '', 0, 20, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `forma`
--

CREATE TABLE `forma` (
  `idForma` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `forma`
--

INSERT INTO `forma` (`idForma`, `descripcion`) VALUES
(2, 'Cuadrado'),
(3, 'Redondo'),
(4, 'Rectangular');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `niveles`
--

CREATE TABLE `niveles` (
  `idNiveles` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `niveles`
--

INSERT INTO `niveles` (`idNiveles`, `descripcion`) VALUES
(2, '1'),
(3, '2'),
(4, '3'),
(5, '4'),
(6, '5'),
(7, '6');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `idPedido` int(11) NOT NULL,
  `codPedido` varchar(15) NOT NULL,
  `idTipopan` int(11) NOT NULL,
  `nomPedido` varchar(50) NOT NULL,
  `tipoevento` varchar(50) NOT NULL,
  `fechaentrega` varchar(70) NOT NULL,
  `adelanto` int(11) NOT NULL,
  `numtelefono` int(11) NOT NULL,
  `nomcliente` varchar(250) NOT NULL,
  `identificacion` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `idForma` int(11) NOT NULL,
  `idCubierta` int(11) NOT NULL,
  `idNiveles` int(11) NOT NULL,
  `idRelleno` int(11) NOT NULL,
  `quienrecibe` varchar(70) NOT NULL,
  `tematica` varchar(70) NOT NULL,
  `modoentrega` varchar(70) NOT NULL,
  `textopastel` varchar(70) NOT NULL,
  `email` varchar(70) NOT NULL,
  `numtarjeta` int(70) NOT NULL,
  `especificaciones` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`idPedido`, `codPedido`, `idTipopan`, `nomPedido`, `tipoevento`, `fechaentrega`, `adelanto`, `numtelefono`, `nomcliente`, `identificacion`, `edad`, `idForma`, `idCubierta`, `idNiveles`, `idRelleno`, `quienrecibe`, `tematica`, `modoentrega`, `textopastel`, `email`, `numtarjeta`, `especificaciones`) VALUES
(20, '1234', 4, 'Pedido Fiesta', 'Fiesta Infantil', '1-Diciembre-2022', 300, 2147483647, 'Maria Torres', 'MTFAH90KL', '32', 4, 3, 2, 3, 'Carlos Villa', 'Mario Bros', 'A Domicilio', '¡Feliz Cumpleaños!', 'MariaTo106@gmail.com', 898989976, 'Poner en la Superficie del Pastel a los personajes de Mario Bros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_has_decoraciones`
--

CREATE TABLE `pedido_has_decoraciones` (
  `idPedido` int(50) NOT NULL,
  `idDecoraciones` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pedido_has_decoraciones`
--

INSERT INTO `pedido_has_decoraciones` (`idPedido`, `idDecoraciones`) VALUES
(8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_has_presupuesto`
--

CREATE TABLE `pedido_has_presupuesto` (
  `idPedido` int(50) NOT NULL,
  `idPresupuesto` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pedido_has_presupuesto`
--

INSERT INTO `pedido_has_presupuesto` (`idPedido`, `idPresupuesto`) VALUES
(8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `presupuesto`
--

CREATE TABLE `presupuesto` (
  `idPresupuesto` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `presupuesto`
--

INSERT INTO `presupuesto` (`idPresupuesto`, `descripcion`) VALUES
(4, '300'),
(5, '400'),
(6, '500'),
(7, '600'),
(8, '700'),
(9, '800'),
(10, '1000');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `relleno`
--

CREATE TABLE `relleno` (
  `idRelleno` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `relleno`
--

INSERT INTO `relleno` (`idRelleno`, `descripcion`) VALUES
(2, 'Fresa'),
(3, 'Durazno'),
(4, 'Piña'),
(5, 'Kiwi'),
(6, 'Betun'),
(7, 'Nutella'),
(8, 'Merengue');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipopan`
--

CREATE TABLE `tipopan` (
  `idTipopan` int(50) NOT NULL,
  `descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipopan`
--

INSERT INTO `tipopan` (`idTipopan`, `descripcion`) VALUES
(3, 'Seco'),
(4, 'Tres Leches'),
(5, 'Masa Madre'),
(6, 'Hojaldre'),
(7, 'Queso'),
(8, 'Chocoflan'),
(9, 'Pay');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cubierta`
--
ALTER TABLE `cubierta`
  ADD PRIMARY KEY (`idCubierta`);

--
-- Indices de la tabla `decoraciones`
--
ALTER TABLE `decoraciones`
  ADD PRIMARY KEY (`idDecoraciones`);

--
-- Indices de la tabla `encargo`
--
ALTER TABLE `encargo`
  ADD PRIMARY KEY (`idEncargo`),
  ADD KEY `idPedido` (`idPedido`) USING BTREE,
  ADD KEY `idTipopan` (`idTipopan`) USING BTREE;

--
-- Indices de la tabla `forma`
--
ALTER TABLE `forma`
  ADD PRIMARY KEY (`idForma`);

--
-- Indices de la tabla `niveles`
--
ALTER TABLE `niveles`
  ADD PRIMARY KEY (`idNiveles`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`idPedido`),
  ADD KEY `idEstadoCivil` (`idForma`),
  ADD KEY `idGradoAvance` (`idNiveles`),
  ADD KEY `idCarrera` (`idRelleno`),
  ADD KEY `area` (`idTipopan`),
  ADD KEY `idCubierta` (`idCubierta`) USING BTREE;

--
-- Indices de la tabla `pedido_has_decoraciones`
--
ALTER TABLE `pedido_has_decoraciones`
  ADD PRIMARY KEY (`idPedido`,`idDecoraciones`) USING BTREE,
  ADD KEY `idDecoraciones` (`idDecoraciones`) USING BTREE;

--
-- Indices de la tabla `pedido_has_presupuesto`
--
ALTER TABLE `pedido_has_presupuesto`
  ADD PRIMARY KEY (`idPedido`,`idPresupuesto`) USING BTREE,
  ADD KEY `idPresupuesto` (`idPresupuesto`) USING BTREE;

--
-- Indices de la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  ADD PRIMARY KEY (`idPresupuesto`);

--
-- Indices de la tabla `relleno`
--
ALTER TABLE `relleno`
  ADD PRIMARY KEY (`idRelleno`);

--
-- Indices de la tabla `tipopan`
--
ALTER TABLE `tipopan`
  ADD PRIMARY KEY (`idTipopan`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cubierta`
--
ALTER TABLE `cubierta`
  MODIFY `idCubierta` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `decoraciones`
--
ALTER TABLE `decoraciones`
  MODIFY `idDecoraciones` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `encargo`
--
ALTER TABLE `encargo`
  MODIFY `idEncargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `forma`
--
ALTER TABLE `forma`
  MODIFY `idForma` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `niveles`
--
ALTER TABLE `niveles`
  MODIFY `idNiveles` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `pedido`
--
ALTER TABLE `pedido`
  MODIFY `idPedido` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `presupuesto`
--
ALTER TABLE `presupuesto`
  MODIFY `idPresupuesto` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `relleno`
--
ALTER TABLE `relleno`
  MODIFY `idRelleno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tipopan`
--
ALTER TABLE `tipopan`
  MODIFY `idTipopan` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
