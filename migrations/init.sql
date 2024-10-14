CREATE DATABASE supermarket;
USE supermarket;

CREATE TABLE product(
    prod_id INT NOT NULL AUTO_INCREMENT,
    prod_name VARCHAR(45),
    prod_measure VARCHAR(45),
    prod_price INT,
    prod_category INT,
    PRIMARY KEY (prod_id)
);

