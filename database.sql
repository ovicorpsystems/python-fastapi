CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
);

INSERT INTO customers (name, email) VALUES
  ('Oscar Lopez', 'olopez@example.com'),
  ('Pepito Perez', 'pperez@example.com');
