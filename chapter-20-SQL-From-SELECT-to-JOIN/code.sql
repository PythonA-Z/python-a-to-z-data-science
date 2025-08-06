-- ----------------------------------------
-- Section: Create Tables and Insert Data
-- ----------------------------------------

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT
);

INSERT INTO Customers (CustomerID, Name, City)
VALUES 
(1, 'Alice', 'London'),
(2, 'Bob', 'Manchester'),
(3, 'Charlie', 'Birmingham'),
(4, 'Diana', 'Leeds');

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Amount INTEGER,
    Date TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders (OrderID, CustomerID, Amount, Date)
VALUES 
(101, 1, 250, '2024-06-01'),
(102, 1, 120, '2024-06-04'),
(103, 2, 300, '2024-06-02'),
(104, 4, 180, '2024-06-03');

-- ----------------------------------------
-- Section: Basic SELECT Queries
-- ----------------------------------------

SELECT Name, City FROM Customers;
SELECT * FROM Customers;

-- ----------------------------------------
-- Section: Filtering with WHERE
-- ----------------------------------------

SELECT Name, City FROM Customers WHERE City = 'London';
SELECT Name, City FROM Customers WHERE City <> 'London';

-- ----------------------------------------
-- Section: Sorting and Limiting
-- ----------------------------------------

SELECT Name, City FROM Customers ORDER BY Name ASC;
SELECT OrderID, CustomerID, Amount FROM Orders ORDER BY Amount DESC;
SELECT OrderID, Amount FROM Orders ORDER BY Amount DESC LIMIT 2;

-- ----------------------------------------
-- Section: Grouping and Aggregation
-- ----------------------------------------

SELECT CustomerID, SUM(Amount) AS TotalSpent FROM Orders GROUP BY CustomerID;
SELECT CustomerID, COUNT(*) AS OrderCount FROM Orders GROUP BY CustomerID;

-- ----------------------------------------
-- Section: JOINs
-- ----------------------------------------

SELECT 
    Customers.Name,
    Customers.City,
    Orders.Amount,
    Orders.Date
FROM 
    Customers
    INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- Inspect Table Structure
SELECT * FROM pragma_table_info('Customers');
PRAGMA foreign_key_list(Orders);

-- ----------------------------------------
-- Section: Practical JOIN Queries
-- ----------------------------------------

-- INNER JOIN: Orders with Customer Names
SELECT Orders.OrderID, Customers.Name, Orders.Amount
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

-- LEFT JOIN: Customers with and without Orders
SELECT Customers.Name, Orders.Amount
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- ----------------------------------------
-- Section: Export High-Value Orders
-- ----------------------------------------

SELECT Customers.Name, Orders.Amount, Orders.Date
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Orders.Amount > 200;

-- ----------------------------------------
-- Section: Interview Confidence Builder Solutions
-- ----------------------------------------

-- 1. Customers who placed an order
SELECT DISTINCT Customers.Name
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;

-- 2. Total spent by each customer, sorted high to low
SELECT Customers.Name, SUM(Orders.Amount) AS TotalSpent
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name
ORDER BY TotalSpent DESC;

-- 3. Customers who haven't placed any orders
SELECT Customers.Name
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;

-- ----------------------------------------
-- Section: Mini Project Queries
-- ----------------------------------------

-- 1. Number of orders placed by each customer
SELECT Customers.Name, COUNT(Orders.OrderID) AS OrderCount
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name;

-- 2. Average order amount per customer
SELECT Customers.Name, AVG(Orders.Amount) AS AvgOrder
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name;

-- 3. Top 2 customers by total spend
SELECT Customers.Name, SUM(Orders.Amount) AS TotalSpent
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name
ORDER BY TotalSpent DESC
LIMIT 2;

-- 4. Customers who placed more than one order
SELECT Customers.Name, COUNT(Orders.OrderID) AS OrderCount
FROM Customers
JOIN Orders ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.Name
HAVING COUNT(Orders.OrderID) > 1;

-- 5. Customers who haven’t placed any orders
SELECT Customers.Name
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE Orders.OrderID IS NULL;
