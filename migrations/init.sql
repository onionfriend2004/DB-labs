CREATE DATABASE supermarket;
USE supermarket;

CREATE TABLE product (
    prod_id INT NOT NULL AUTO_INCREMENT,
    prod_name VARCHAR(45),
    prod_measure VARCHAR(45),
    prod_price INT,
    prod_category VARCHAR(45),
    PRIMARY KEY (prod_id)
);

CREATE TABLE users (
    login VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL,
    PRIMARY KEY (login)
);

INSERT INTO product (prod_name, prod_measure, prod_price, prod_category)
VALUES
('Apple', 'kg', 2, 'Fruits'),
('Banana', 'kg', 1, 'Fruits'),
('Carrot', 'kg', 3, 'Vegetables'),
('Milk', 'liter', 5, 'Dairy'),
('Bread', 'piece', 1, 'Bakery');

INSERT INTO users (login, password, role)
VALUES
('admin', 'admin123', 'admin'),
('user1', 'password1', 'manager'),
('user2', 'password2', 'user');