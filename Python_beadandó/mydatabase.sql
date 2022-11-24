-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2022. Nov 24. 21:17
-- Kiszolgáló verziója: 10.4.25-MariaDB
-- PHP verzió: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `mydatabase`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `bevetel`
--

CREATE TABLE `bevetel` (
  `sorszam` int(11) NOT NULL,
  `nev` varchar(50) NOT NULL,
  `osszeg` int(11) NOT NULL,
  `bevet_kategoria_id` int(11) NOT NULL,
  `datum` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `bevetel`
--

INSERT INTO `bevetel` (`sorszam`, `nev`, `osszeg`, `bevet_kategoria_id`, `datum`) VALUES
(1, 'Adam', 10000, 1, '2022-11-23 19:31:49');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `bevet_kategoria`
--

CREATE TABLE `bevet_kategoria` (
  `id` int(11) NOT NULL,
  `megnevezes` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `bevet_kategoria`
--

INSERT INTO `bevet_kategoria` (`id`, `megnevezes`) VALUES
(1, 'Fizetés'),
(2, 'Befektetés'),
(3, 'Egyéb');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `kiadas`
--

CREATE TABLE `kiadas` (
  `sorszam` int(11) NOT NULL,
  `nev` varchar(50) NOT NULL,
  `osszeg` int(11) NOT NULL,
  `kiadas_kategoria_id` int(11) NOT NULL,
  `datum` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `kiadas`
--

INSERT INTO `kiadas` (`sorszam`, `nev`, `osszeg`, `kiadas_kategoria_id`, `datum`) VALUES
(1, 'Balu', 100, 2, '2022-11-24 12:04:36');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `kiadas_kategoria`
--

CREATE TABLE `kiadas_kategoria` (
  `id` int(11) NOT NULL,
  `megnevezes` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- A tábla adatainak kiíratása `kiadas_kategoria`
--

INSERT INTO `kiadas_kategoria` (`id`, `megnevezes`) VALUES
(1, 'Egyéb'),
(2, 'Szórakozás');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `bevetel`
--
ALTER TABLE `bevetel`
  ADD PRIMARY KEY (`sorszam`),
  ADD KEY `bevet_kategoria_id` (`bevet_kategoria_id`);

--
-- A tábla indexei `bevet_kategoria`
--
ALTER TABLE `bevet_kategoria`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `kiadas`
--
ALTER TABLE `kiadas`
  ADD PRIMARY KEY (`sorszam`),
  ADD KEY `kiadas_kategoria_id` (`kiadas_kategoria_id`);

--
-- A tábla indexei `kiadas_kategoria`
--
ALTER TABLE `kiadas_kategoria`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `bevetel`
--
ALTER TABLE `bevetel`
  MODIFY `sorszam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT a táblához `kiadas`
--
ALTER TABLE `kiadas`
  MODIFY `sorszam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `bevetel`
--
ALTER TABLE `bevetel`
  ADD CONSTRAINT `bevetel_ibfk_1` FOREIGN KEY (`bevet_kategoria_id`) REFERENCES `bevet_kategoria` (`id`);

--
-- Megkötések a táblához `kiadas`
--
ALTER TABLE `kiadas`
  ADD CONSTRAINT `kiadas_ibfk_1` FOREIGN KEY (`kiadas_kategoria_id`) REFERENCES `kiadas_kategoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
