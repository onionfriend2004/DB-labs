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


INSERT INTO product (prod_name, prod_measure, prod_price, prod_category)
VALUES
-- Meat
('Chicken fillet', 'kg', 450, 'Meat'),
('Beef', 'kg', 700, 'Meat'),
('Pork', 'kg', 600, 'Meat'),
('Lamb', 'kg', 800, 'Meat'),
('Chicken wings', 'kg', 300, 'Meat'),
('Beef mince', 'kg', 650, 'Meat'),
('Sausages', 'kg', 350, 'Meat'),

-- Dairy products
('Milk 2.5%', 'l', 50, 'Dairy products'),
('Kefir 1%', 'l', 55, 'Dairy products'),
('Cottage cheese 9%', 'kg', 200, 'Dairy products'),
('Sour cream 20%', 'g', 80, 'Dairy products'),
('Strawberry yogurt', 'g', 25, 'Dairy products'),
('Hard cheese', 'kg', 500, 'Dairy products'),
('Butter', 'kg', 400, 'Dairy products'),

-- Vegetables
('Potatoes', 'kg', 25, 'Vegetables'),
('Carrots', 'kg', 30, 'Vegetables'),
('White cabbage', 'kg', 20, 'Vegetables'),
('Cucumbers', 'kg', 80, 'Vegetables'),
('Tomatoes', 'kg', 100, 'Vegetables'),
('Onions', 'kg', 40, 'Vegetables'),
('Bell peppers', 'kg', 120, 'Vegetables'),

-- Fruits
('Apples', 'kg', 60, 'Fruits'),
('Bananas', 'kg', 80, 'Fruits'),
('Oranges', 'kg', 90, 'Fruits'),
('Pears', 'kg', 75, 'Fruits'),
('Mandarins', 'kg', 100, 'Fruits'),
('Kiwi', 'kg', 120, 'Fruits'),
('Grapes', 'kg', 150, 'Fruits'),

-- Grains
('Buckwheat', 'kg', 60, 'Grains'),
('Rice', 'kg', 70, 'Grains'),
('Oatmeal', 'kg', 50, 'Grains'),
('Pearl barley', 'kg', 30, 'Grains'),
('Semolina', 'kg', 40, 'Grains'),
('Millet', 'kg', 35, 'Grains'),
('Quinoa', 'kg', 200, 'Grains'),

-- Beverages
('Mineral water', 'l', 30, 'Beverages'),
('Orange juice', 'l', 70, 'Beverages'),
('Black tea', 'pack', 100, 'Beverages'),
('Ground coffee', 'g', 300, 'Beverages'),
('Soda', 'l', 50, 'Beverages'),
('Cherry compote', 'l', 60, 'Beverages'),
('Energy drink', 'l', 150, 'Beverages'),

-- Bakery products
('Wheat bread', 'piece', 25, 'Bakery products'),
('Loaf', 'piece', 20, 'Bakery products'),
('Poppy seed roll', 'piece', 15, 'Bakery products'),
('Croissant', 'piece', 40, 'Bakery products'),
('Potato pie', 'piece', 25, 'Bakery products'),
('Raisin bun', 'piece', 30, 'Bakery products'),
('Baguette', 'piece', 35, 'Bakery products');