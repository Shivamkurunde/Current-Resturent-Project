-- ============================================================================
-- DBMS PRACTICAL DEMONSTRATION
-- Restaurant Management System
-- Complete SQL Commands for Teacher Demo
-- ============================================================================

-- ============================================================================
-- SECTION 1: DATABASE CREATION & SETUP
-- ============================================================================

-- Create database
CREATE DATABASE IF NOT EXISTS restaurant_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Use database
USE restaurant_db;

-- Show all databases
SHOW DATABASES;


-- ============================================================================
-- SECTION 2: TABLE CREATION (DDL - Data Definition Language)
-- ============================================================================

-- Create USERS table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- Create OTPS table
CREATE TABLE otps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL,
    otp_code VARCHAR(10) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    is_used BOOLEAN DEFAULT FALSE,
    INDEX idx_email (email)
) ENGINE=InnoDB;

-- Create CART_ITEMS table with Foreign Key
CREATE TABLE cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(200) NOT NULL,
    item_price FLOAT NOT NULL,
    quantity INT DEFAULT 1,
    category VARCHAR(100),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB;

-- Create ORDERS table with Foreign Key
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount FLOAT NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    delivery_address TEXT,
    phone_number VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_status (status)
) ENGINE=InnoDB;

-- Create ORDER_ITEMS table with Foreign Key
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_name VARCHAR(200) NOT NULL,
    item_price FLOAT NOT NULL,
    quantity INT NOT NULL,
    category VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    INDEX idx_order_id (order_id)
) ENGINE=InnoDB;

-- Show all tables
SHOW TABLES;

-- Describe table structure
DESCRIBE users;
DESCRIBE cart_items;
DESCRIBE orders;
DESCRIBE order_items;


-- ============================================================================
-- SECTION 3: DATA INSERTION (DML - Data Manipulation Language)
-- ============================================================================

-- Insert users
INSERT INTO users (name, email, password_hash, is_verified) VALUES
('Rahul Kumar', 'rahul@example.com', '$2b$12$hashed_password_1', TRUE),
('Priya Sharma', 'priya@example.com', '$2b$12$hashed_password_2', TRUE),
('Amit Patel', 'amit@example.com', '$2b$12$hashed_password_3', TRUE);

-- Insert cart items for Rahul (user_id = 1)
INSERT INTO cart_items (user_id, item_name, item_price, quantity, category) VALUES
(1, 'Gulab Jamun', 50, 2, 'Desserts'),
(1, 'Paneer Tikka', 120, 1, 'Veg'),
(1, 'Pav Bhaji', 80, 1, 'Street Chaat');

-- Insert orders
INSERT INTO orders (user_id, total_amount, status, delivery_address, phone_number) VALUES
(2, 350, 'Delivered', '123 MG Road, Mumbai', '9876543210'),
(3, 280, 'Pending', '456 Park Street, Pune', '9876543211'),
(2, 450, 'Confirmed', '123 MG Road, Mumbai', '9876543210');

-- Insert order items for Order #1
INSERT INTO order_items (order_id, item_name, item_price, quantity, category) VALUES
(1, 'Chocolate Ice Cream', 100, 2, 'Desserts'),
(1, 'Veg Biryani', 150, 1, 'Veg');

-- Insert order items for Order #2
INSERT INTO order_items (order_id, item_name, item_price, quantity, category) VALUES
(2, 'Pani Puri', 40, 2, 'Street Chaat'),
(2, 'Protein Shake', 200, 1, 'Gym Food');

-- Insert order items for Order #3
INSERT INTO order_items (order_id, item_name, item_price, quantity, category) VALUES
(3, 'Paneer Butter Masala', 180, 1, 'Veg'),
(3, 'Dal Makhani', 150, 1, 'Veg'),
(3, 'Gulab Jamun', 60, 2, 'Desserts');


-- ============================================================================
-- SECTION 4: BASIC QUERIES (SELECT)
-- ============================================================================

-- 1. Select all users
SELECT * FROM users;

-- 2. Select specific columns
SELECT id, name, email FROM users;

-- 3. Select with WHERE clause
SELECT * FROM users WHERE email = 'rahul@example.com';

-- 4. Select with multiple conditions
SELECT * FROM orders WHERE status = 'Pending' AND total_amount > 200;

-- 5. Select with ORDER BY
SELECT * FROM orders ORDER BY created_at DESC;

-- 6. Select with LIMIT
SELECT * FROM orders ORDER BY total_amount DESC LIMIT 3;

-- 7. Select with LIKE (pattern matching)
SELECT * FROM users WHERE name LIKE '%Kumar%';

-- 8. Select with IN
SELECT * FROM orders WHERE status IN ('Pending', 'Confirmed');

-- 9. Select with BETWEEN
SELECT * FROM orders WHERE total_amount BETWEEN 200 AND 400;


-- ============================================================================
-- SECTION 5: AGGREGATE FUNCTIONS
-- ============================================================================

-- COUNT
SELECT COUNT(*) AS total_users FROM users;
SELECT COUNT(*) AS total_orders FROM orders;
SELECT COUNT(*) AS pending_orders FROM orders WHERE status = 'Pending';

-- SUM
SELECT SUM(total_amount) AS total_revenue FROM orders;
SELECT SUM(total_amount) AS revenue_delivered 
FROM orders WHERE status = 'Delivered';

-- AVG
SELECT AVG(total_amount) AS average_order_value FROM orders;

-- MAX and MIN
SELECT MAX(total_amount) AS highest_order FROM orders;
SELECT MIN(total_amount) AS lowest_order FROM orders;

-- Multiple aggregates
SELECT 
    COUNT(*) AS total_orders,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order,
    MAX(total_amount) AS max_order,
    MIN(total_amount) AS min_order
FROM orders;


-- ============================================================================
-- SECTION 6: GROUP BY & HAVING
-- ============================================================================

-- Group by status
SELECT status, COUNT(*) AS order_count, SUM(total_amount) AS total
FROM orders
GROUP BY status;

-- Group by user
SELECT user_id, COUNT(*) AS order_count, SUM(total_amount) AS total_spent
FROM orders
GROUP BY user_id;

-- Group with HAVING (filter groups)
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 1;

-- Most ordered items
SELECT item_name, SUM(quantity) AS times_ordered, SUM(item_price * quantity) AS revenue
FROM order_items
GROUP BY item_name
ORDER BY times_ordered DESC;

-- Revenue by category
SELECT category, SUM(item_price * quantity) AS revenue
FROM order_items
GROUP BY category
ORDER BY revenue DESC;


-- ============================================================================
-- SECTION 7: JOINS
-- ============================================================================

-- INNER JOIN - Orders with user details
SELECT 
    o.id AS order_id,
    u.name AS customer_name,
    u.email,
    o.total_amount,
    o.status,
    o.created_at
FROM orders o
INNER JOIN users u ON o.user_id = u.id
ORDER BY o.created_at DESC;

-- LEFT JOIN - All users with their order count (including users with no orders)
SELECT 
    u.id,
    u.name,
    u.email,
    COUNT(o.id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, u.email;

-- Multiple JOINS - Complete order details
SELECT 
    o.id AS order_id,
    u.name AS customer_name,
    u.email,
    oi.item_name,
    oi.item_price,
    oi.quantity,
    (oi.item_price * oi.quantity) AS item_total,
    o.total_amount AS order_total,
    o.status
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN order_items oi ON o.id = oi.order_id
ORDER BY o.id, oi.id;

-- Cart items with user details
SELECT 
    u.name,
    u.email,
    c.item_name,
    c.item_price,
    c.quantity,
    (c.item_price * c.quantity) AS subtotal
FROM cart_items c
INNER JOIN users u ON c.user_id = u.id;


-- ============================================================================
-- SECTION 8: SUBQUERIES
-- ============================================================================

-- Scalar subquery - Users who spent more than average
SELECT name, email
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
    GROUP BY user_id
    HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM orders)
);

-- Subquery in SELECT - User with their latest order date
SELECT 
    u.name,
    u.email,
    (SELECT MAX(created_at) FROM orders WHERE user_id = u.id) AS last_order_date,
    (SELECT COUNT(*) FROM orders WHERE user_id = u.id) AS total_orders
FROM users u;

-- Subquery with EXISTS
SELECT name, email
FROM users u
WHERE EXISTS (
    SELECT 1 FROM orders WHERE user_id = u.id AND status = 'Pending'
);


-- ============================================================================
-- SECTION 9: UPDATE OPERATIONS
-- ============================================================================

-- Update single record
UPDATE orders SET status = 'Confirmed' WHERE id = 2;

-- Update with condition
UPDATE orders 
SET status = 'Delivered' 
WHERE id = 1 AND status = 'Confirmed';

-- Update multiple records
UPDATE cart_items 
SET quantity = quantity + 1 
WHERE user_id = 1;

-- Update with calculation
UPDATE orders 
SET total_amount = total_amount * 0.9 
WHERE status = 'Pending';


-- ============================================================================
-- SECTION 10: DELETE OPERATIONS
-- ============================================================================

-- Delete specific record
DELETE FROM cart_items WHERE id = 1;

-- Delete with condition
DELETE FROM cart_items WHERE user_id = 1 AND quantity = 0;

-- Delete all cart items for a user
DELETE FROM cart_items WHERE user_id = 1;

-- Note: Deleting user will CASCADE delete their cart_items and orders
-- DELETE FROM users WHERE id = 1;


-- ============================================================================
-- SECTION 11: TRANSACTIONS (ACID Properties)
-- ============================================================================

-- Example: Place Order Transaction
START TRANSACTION;

-- Step 1: Create order
INSERT INTO orders (user_id, total_amount, status, delivery_address, phone_number)
VALUES (1, 250, 'Pending', '789 New Street, Delhi', '9876543212');

-- Get the order ID
SET @new_order_id = LAST_INSERT_ID();

-- Step 2: Copy cart items to order_items
INSERT INTO order_items (order_id, item_name, item_price, quantity, category)
SELECT @new_order_id, item_name, item_price, quantity, category
FROM cart_items
WHERE user_id = 1;

-- Step 3: Clear cart
DELETE FROM cart_items WHERE user_id = 1;

-- Commit transaction (make changes permanent)
COMMIT;

-- If error occurs, use ROLLBACK to undo all changes
-- ROLLBACK;


-- ============================================================================
-- SECTION 12: VIEWS (Virtual Tables)
-- ============================================================================

-- Create view for order summary
CREATE OR REPLACE VIEW order_summary AS
SELECT 
    o.id AS order_id,
    u.name AS customer_name,
    u.email,
    o.total_amount,
    o.status,
    o.created_at,
    COUNT(oi.id) AS item_count
FROM orders o
INNER JOIN users u ON o.user_id = u.id
LEFT JOIN order_items oi ON o.id = oi.order_id
GROUP BY o.id, u.name, u.email, o.total_amount, o.status, o.created_at;

-- Query the view
SELECT * FROM order_summary;

-- Create view for user statistics
CREATE OR REPLACE VIEW user_statistics AS
SELECT 
    u.id,
    u.name,
    u.email,
    COUNT(DISTINCT o.id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent,
    COALESCE(AVG(o.total_amount), 0) AS avg_order_value
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, u.email;

-- Query the view
SELECT * FROM user_statistics;


-- ============================================================================
-- SECTION 13: INDEXES (Performance Optimization)
-- ============================================================================

-- Show existing indexes
SHOW INDEX FROM users;
SHOW INDEX FROM orders;

-- Create custom index
CREATE INDEX idx_order_date ON orders(created_at);
CREATE INDEX idx_item_name ON order_items(item_name);

-- Analyze query performance
EXPLAIN SELECT * FROM orders WHERE created_at > '2024-01-01';
EXPLAIN SELECT * FROM order_items WHERE item_name = 'Gulab Jamun';


-- ============================================================================
-- SECTION 14: CONSTRAINTS DEMONSTRATION
-- ============================================================================

-- Try to insert duplicate email (UNIQUE constraint)
-- This will fail
-- INSERT INTO users (name, email, password_hash) 
-- VALUES ('Test User', 'rahul@example.com', 'hash');

-- Try to insert NULL in NOT NULL column
-- This will fail
-- INSERT INTO users (name, email) VALUES ('Test', NULL);

-- Try to insert invalid foreign key
-- This will fail
-- INSERT INTO cart_items (user_id, item_name, item_price) 
-- VALUES (999, 'Test Item', 100);

-- Demonstrate CASCADE DELETE
-- First, check cart items for user 1
SELECT * FROM cart_items WHERE user_id = 1;

-- Delete user (will cascade to cart_items and orders)
-- DELETE FROM users WHERE id = 1;

-- Check cart items again (will be empty)
-- SELECT * FROM cart_items WHERE user_id = 1;


-- ============================================================================
-- SECTION 15: ADVANCED ANALYTICS
-- ============================================================================

-- Daily revenue report
SELECT 
    DATE(created_at) AS order_date,
    COUNT(*) AS total_orders,
    SUM(total_amount) AS daily_revenue
FROM orders
GROUP BY DATE(created_at)
ORDER BY order_date DESC;

-- Top 5 customers by spending
SELECT 
    u.name,
    u.email,
    COUNT(o.id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, u.email
ORDER BY total_spent DESC
LIMIT 5;

-- Order status distribution
SELECT 
    status,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 2) AS percentage
FROM orders
GROUP BY status;

-- Items never ordered
SELECT DISTINCT c.item_name
FROM cart_items c
WHERE c.item_name NOT IN (SELECT item_name FROM order_items);

-- Users who added to cart but never ordered
SELECT DISTINCT u.name, u.email
FROM users u
INNER JOIN cart_items c ON u.id = c.user_id
WHERE u.id NOT IN (SELECT DISTINCT user_id FROM orders);


-- ============================================================================
-- SECTION 16: DATABASE MAINTENANCE
-- ============================================================================

-- Check table status
SHOW TABLE STATUS;

-- Optimize tables
OPTIMIZE TABLE users;
OPTIMIZE TABLE orders;
OPTIMIZE TABLE order_items;

-- Analyze tables (update statistics)
ANALYZE TABLE users;
ANALYZE TABLE orders;

-- Check table for errors
CHECK TABLE users;
CHECK TABLE orders;

-- Show database size
SELECT 
    table_name,
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS size_mb
FROM information_schema.TABLES
WHERE table_schema = 'restaurant_db'
ORDER BY (data_length + index_length) DESC;


-- ============================================================================
-- SECTION 17: BACKUP & RESTORE (Commands to run in terminal)
-- ============================================================================

-- Backup database (run in terminal, not in MySQL)
-- mysqldump -u root -p restaurant_db > backup.sql

-- Restore database (run in terminal)
-- mysql -u root -p restaurant_db < backup.sql

-- Backup specific table
-- mysqldump -u root -p restaurant_db users > users_backup.sql


-- ============================================================================
-- SECTION 18: USER PRIVILEGES (For Multi-User Environment)
-- ============================================================================

-- Create read-only user
-- CREATE USER 'readonly'@'localhost' IDENTIFIED BY 'password';
-- GRANT SELECT ON restaurant_db.* TO 'readonly'@'localhost';

-- Create full access user
-- CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
-- GRANT ALL PRIVILEGES ON restaurant_db.* TO 'admin'@'localhost';

-- Show grants
-- SHOW GRANTS FOR 'readonly'@'localhost';

-- Revoke privileges
-- REVOKE SELECT ON restaurant_db.* FROM 'readonly'@'localhost';

-- Drop user
-- DROP USER 'readonly'@'localhost';


-- ============================================================================
-- SECTION 19: STORED PROCEDURES (Advanced)
-- ============================================================================

-- Create procedure to place order
DELIMITER //
CREATE PROCEDURE place_order(
    IN p_user_id INT,
    IN p_delivery_address TEXT,
    IN p_phone_number VARCHAR(20)
)
BEGIN
    DECLARE v_total FLOAT;
    DECLARE v_order_id INT;
    
    -- Calculate total from cart
    SELECT SUM(item_price * quantity) INTO v_total
    FROM cart_items
    WHERE user_id = p_user_id;
    
    -- Create order
    INSERT INTO orders (user_id, total_amount, status, delivery_address, phone_number)
    VALUES (p_user_id, v_total, 'Pending', p_delivery_address, p_phone_number);
    
    SET v_order_id = LAST_INSERT_ID();
    
    -- Copy cart to order_items
    INSERT INTO order_items (order_id, item_name, item_price, quantity, category)
    SELECT v_order_id, item_name, item_price, quantity, category
    FROM cart_items
    WHERE user_id = p_user_id;
    
    -- Clear cart
    DELETE FROM cart_items WHERE user_id = p_user_id;
    
    -- Return order ID
    SELECT v_order_id AS order_id;
END //
DELIMITER ;

-- Call the procedure
-- CALL place_order(1, '123 Test Street', '9876543210');


-- ============================================================================
-- SECTION 20: TRIGGERS (Automatic Actions)
-- ============================================================================

-- Create trigger to update order timestamp
DELIMITER //
CREATE TRIGGER update_order_timestamp
BEFORE UPDATE ON orders
FOR EACH ROW
BEGIN
    SET NEW.updated_at = CURRENT_TIMESTAMP;
END //
DELIMITER ;

-- Create trigger to log order status changes
CREATE TABLE IF NOT EXISTS order_status_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    old_status VARCHAR(50),
    new_status VARCHAR(50),
    changed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER log_status_change
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    IF OLD.status != NEW.status THEN
        INSERT INTO order_status_log (order_id, old_status, new_status)
        VALUES (NEW.id, OLD.status, NEW.status);
    END IF;
END //
DELIMITER ;


-- ============================================================================
-- END OF DEMONSTRATION
-- ============================================================================

-- Show all tables one more time
SHOW TABLES;

-- Show record counts
SELECT 'users' AS table_name, COUNT(*) AS record_count FROM users
UNION ALL
SELECT 'cart_items', COUNT(*) FROM cart_items
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items;

-- ============================================================================
-- NOTES FOR TEACHER PRESENTATION:
-- ============================================================================
-- 1. Start with Section 1-2 (Database & Table Creation)
-- 2. Show Section 3 (Data Insertion)
-- 3. Demonstrate Section 4-6 (Basic Queries & Aggregates)
-- 4. Show Section 7 (JOINS - most important!)
-- 5. Demonstrate Section 11 (Transactions - ACID properties)
-- 6. Show Section 15 (Analytics - practical use)
-- 7. Explain constraints and foreign keys
-- 8. Show views for simplified queries
-- ============================================================================
