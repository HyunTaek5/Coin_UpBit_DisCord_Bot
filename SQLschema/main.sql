CREATE DATABASE coin default CHARACTER SET UTF8;

use coin;

CREATE TABLE coin
(
    idx         INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    market      VARCHAR(256) NOT NULL,
    trade_price FLOAT        NOT NULL
);