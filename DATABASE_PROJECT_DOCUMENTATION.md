# 🗄️ Restaurant Management System - Database Project Documentation

## Complete DBMS Implementation

---

## 📋 Table of Contents

1. [Database Overview](#database-overview)
2. [Database Schema](#database-schema)
3. [Tables Structure](#tables-structure)
4. [Relationships & Constraints](#relationships--constraints)
5. [Normalization](#normalization)
6. [SQL Queries](#sql-queries)
7. [Transactions](#transactions)
8. [Indexing](#indexing)
9. [Database Operations](#database-operations)
10. [ACID Properties](#acid-properties)

---

## 1. Database Overview

### Database Management System: **MySQL 8.x**
### Database Name: **restaurant_db**
### Character Set: **utf8mb4_unicode_ci**
### Storage Engine: **InnoDB**

### Purpose:
Complete restaurant management system with user authentication, shopping cart, and order management.

---

## 2. Database Schema

### Entity-Relationship Model:

```
┌─────────────┐
│    USERS    │
│  (Parent)   │
└──────┬──────┘
       │
       │ 1:M (One-to-Many)
       │
   ┌───┴────┬──────────┐
   │        │          │
   ▼        ▼          ▼
┌──────┐ ┌──────┐  ┌──────┐
│ CART │ │ORDERS│  │ OTPS │
│ITEMS │ │      │  │      │
└──────┘ └───┬──┘  └──────┘
             │
             │ 1:M
             │
             ▼
        ┌────────┐
        │ ORDER  │
        │ ITEMS  │
        └────────┘
```

### Total Tables: **5**
- users (Parent table)
- otps (Independent)
- cart_items (Child of users)
- orders (Child of users)
- order_items (Child of orders)

---

## 3. Tables Structure

### 3.1 USERS Table

**Purpose:** Store user account information

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_email (email),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique user identifier |
| name | VARCHAR(100) | NOT NULL | User's full name |
| email | VARCHAR(120) | UNIQUE, NOT NULL | Login email |
| password_hash | VARCHAR(255) | NOT NULL | Encrypted password |
| is_verified | BOOLEAN | DEFAULT FALSE | Email verification status |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Registration timestamp |

**Indexes:**
- PRIMARY KEY on `id`
- UNIQUE INDEX on `email`
- INDEX on `created_at` (for sorting)

---

### 3.2 OTPS Table

**Purpose:** Store OTP codes for email verification

```sql
CREATE TABLE otps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(120) NOT NULL,
    otp_code VARCHAR(10) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME NOT NULL,
    is_used BOOLEAN DEFAULT FALSE,
    
    INDEX idx_email (email),
    INDEX idx_expires_at (expires_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique OTP record ID |
| email | VARCHAR(120) | NOT NULL | Email for verification |
| otp_code | VARCHAR(10) | NOT NULL | 6-digit OTP code |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | OTP generation time |
| expires_at | DATETIME | NOT NULL | OTP expiry time (5 min) |
| is_used | BOOLEAN | DEFAULT FALSE | Whether OTP is used |

**Business Logic:**
- OTP expires after 5 minutes
- One-time use only
- Automatically cleaned up after use

---

### 3.3 CART_ITEMS Table

**Purpose:** Store shopping cart items

```sql
CREATE TABLE cart_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(200) NOT NULL,
    item_price FLOAT NOT NULL,
    quantity INT DEFAULT 1,
    category VARCHAR(100),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_added_at (added_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique cart item ID |
| user_id | INT | FOREIGN KEY, NOT NULL | Reference to users.id |
| item_name | VARCHAR(200) | NOT NULL | Food item name |
| item_price | FLOAT | NOT NULL | Price per item |
| quantity | INT | DEFAULT 1 | Number of items |
| category | VARCHAR(100) | NULL | Food category |
| added_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | When added to cart |

**Foreign Key:**
- `user_id` → `users(id)` ON DELETE CASCADE
- When user is deleted, their cart items are automatically deleted

---

### 3.4 ORDERS Table

**Purpose:** Store order information

```sql
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
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique order ID |
| user_id | INT | FOREIGN KEY, NOT NULL | Reference to users.id |
| total_amount | FLOAT | NOT NULL | Total order value |
| status | VARCHAR(50) | DEFAULT 'Pending' | Order status |
| delivery_address | TEXT | NULL | Delivery location |
| phone_number | VARCHAR(20) | NULL | Contact number |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Order placement time |
| updated_at | DATETIME | ON UPDATE CURRENT_TIMESTAMP | Last update time |

**Status Values:**
- `Pending` - Order placed, awaiting confirmation
- `Confirmed` - Order confirmed by restaurant
- `Delivered` - Order delivered to customer
- `Cancelled` - Order cancelled

**Foreign Key:**
- `user_id` → `users(id)` ON DELETE CASCADE

---

### 3.5 ORDER_ITEMS Table

**Purpose:** Store items in each order

```sql
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    item_name VARCHAR(200) NOT NULL,
    item_price FLOAT NOT NULL,
    quantity INT NOT NULL,
    category VARCHAR(100),
    
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    INDEX idx_order_id (order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

**Columns:**
| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique item ID |
| order_id | INT | FOREIGN KEY, NOT NULL | Reference to orders.id |
| item_name | VARCHAR(200) | NOT NULL | Food item name |
| item_price | FLOAT | NOT NULL | Price at order time |
| quantity | INT | NOT NULL | Number ordered |
| category | VARCHAR(100) | NULL | Food category |

**Foreign Key:**
- `order_id` → `orders(id)` ON DELETE CASCADE
- When order is deleted, all its items are deleted

---

## 4. Relationships & Constraints

### 4.1 Primary Keys
All tables have AUTO_INCREMENT primary keys:
- Ensures unique identification
- Automatic value generation
- Efficient indexing

### 4.2 Foreign Keys

#### users → cart_items (1:M)
```sql
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
```
- One user can have many cart items
- Deleting user deletes their cart

#### users → orders (1:M)
```sql
FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
```
- One user can place many orders
- Deleting user deletes their orders

#### orders → order_items (1:M)
```sql
FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
```
- One order contains many items
- Deleting order deletes its items

### 4.3 Referential Integrity

**CASCADE DELETE:**
- Maintains data consistency
- Prevents orphan records
- Automatic cleanup

**Example:**
```
Delete User (id=1)
    ↓
Automatically deletes:
    - cart_items where user_id=1
    - orders where user_id=1
        ↓
    - order_items where order_id IN (user's orders)
```

---

## 5. Normalization

### Current Normalization Level: **3NF (Third Normal Form)**

### 5.1 First Normal Form (1NF) ✅
- All columns contain atomic values
- No repeating groups
- Each column has unique name

**Example:**
```
❌ Bad: items = "Gulab Jamun, Paneer Tikka"
✅ Good: Separate rows in order_items table
```

### 5.2 Second Normal Form (2NF) ✅
- Meets 1NF
- No partial dependencies
- All non-key attributes depend on entire primary key

**Example:**
```
order_items table:
- item_name depends on id (full key)
- item_price depends on id (full key)
- No partial dependencies
```

### 5.3 Third Normal Form (3NF) ✅
- Meets 2NF
- No transitive dependencies
- Non-key attributes depend only on primary key

**Example:**
```
users table:
- email depends on id (not on name)
- password_hash depends on id (not on email)
- No transitive dependencies
```

### Why Not Higher Normalization?

**BCNF/4NF not needed because:**
- No multi-valued dependencies
- No complex functional dependencies
- Current design balances normalization with performance

---

## 6. SQL Queries

### 6.1 Basic Queries (CRUD Operations)

#### CREATE (INSERT)
```sql
-- Insert new user
INSERT INTO users (name, email, password_hash, is_verified)
VALUES ('John Doe', 'john@example.com', '$2b$12$...', TRUE);

-- Insert cart item
INSERT INTO cart_items (user_id, item_name, item_price, quantity, category)
VALUES (1, 'Gulab Jamun', 50, 2, 'Desserts');

-- Insert order
INSERT INTO orders (user_id, total_amount, status, delivery_address, phone_number)
VALUES (1, 350, 'Pending', '123 Street, City', '9876543210');
```

#### READ (SELECT)
```sql
-- Get all users
SELECT * FROM users;

-- Get user by email
SELECT * FROM users WHERE email = 'john@example.com';

-- Get user's cart items
SELECT * FROM cart_items WHERE user_id = 1;

-- Get user's orders
SELECT * FROM orders WHERE user_id = 1 ORDER BY created_at DESC;
```

#### UPDATE
```sql
-- Update user verification status
UPDATE users SET is_verified = TRUE WHERE id = 1;

-- Update cart item quantity
UPDATE cart_items SET quantity = 3 WHERE id = 1;

-- Update order status
UPDATE orders SET status = 'Confirmed' WHERE id = 1;
```

#### DELETE
```sql
-- Delete cart item
DELETE FROM cart_items WHERE id = 1;

-- Delete order (cascades to order_items)
DELETE FROM orders WHERE id = 1;

-- Clear user's cart
DELETE FROM cart_items WHERE user_id = 1;
```

---

### 6.2 Advanced Queries (JOINS)

#### INNER JOIN - Orders with User Details
```sql
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
```

#### LEFT JOIN - Users with Order Count
```sql
SELECT 
    u.id,
    u.name,
    u.email,
    COUNT(o.id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

#### Multiple JOINS - Complete Order Details
```sql
SELECT 
    o.id AS order_id,
    u.name AS customer_name,
    u.email,
    oi.item_name,
    oi.item_price,
    oi.quantity,
    (oi.item_price * oi.quantity) AS item_total,
    o.total_amount AS order_total,
    o.status,
    o.created_at
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN order_items oi ON o.id = oi.order_id
ORDER BY o.created_at DESC, oi.id;
```

---

### 6.3 Aggregate Functions

#### COUNT
```sql
-- Total users
SELECT COUNT(*) AS total_users FROM users;

-- Total orders
SELECT COUNT(*) AS total_orders FROM orders;

-- Orders per user
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id;
```

#### SUM
```sql
-- Total revenue
SELECT SUM(total_amount) AS total_revenue FROM orders;

-- Revenue by status
SELECT status, SUM(total_amount) AS revenue
FROM orders
GROUP BY status;

-- Revenue excluding cancelled
SELECT SUM(total_amount) AS net_revenue
FROM orders
WHERE status != 'Cancelled';
```

#### AVG
```sql
-- Average order value
SELECT AVG(total_amount) AS avg_order_value FROM orders;

-- Average items per order
SELECT AVG(item_count) AS avg_items
FROM (
    SELECT order_id, COUNT(*) AS item_count
    FROM order_items
    GROUP BY order_id
) AS subquery;
```

#### MAX/MIN
```sql
-- Highest order value
SELECT MAX(total_amount) AS highest_order FROM orders;

-- Lowest order value
SELECT MIN(total_amount) AS lowest_order FROM orders;

-- Most recent order
SELECT MAX(created_at) AS latest_order FROM orders;
```

---

### 6.4 Subqueries

#### Scalar Subquery
```sql
-- Users who spent more than average
SELECT name, email
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
    GROUP BY user_id
    HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM orders)
);
```

#### Correlated Subquery
```sql
-- Users with their latest order
SELECT 
    u.name,
    u.email,
    (SELECT MAX(created_at) FROM orders WHERE user_id = u.id) AS last_order
FROM users u;
```

---

### 6.5 GROUP BY & HAVING

```sql
-- Orders grouped by status
SELECT status, COUNT(*) AS count, SUM(total_amount) AS total
FROM orders
GROUP BY status;

-- Users with more than 2 orders
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 2;

-- Most ordered items
SELECT item_name, SUM(quantity) AS times_ordered
FROM order_items
GROUP BY item_name
ORDER BY times_ordered DESC
LIMIT 10;
```

---

## 7. Transactions

### 7.1 Order Placement Transaction

**Scenario:** Place order (atomic operation)

```sql
START TRANSACTION;

-- Step 1: Create order
INSERT INTO orders (user_id, total_amount, status, delivery_address, phone_number)
VALUES (1, 350, 'Pending', '123 Street', '9876543210');

SET @order_id = LAST_INSERT_ID();

-- Step 2: Copy cart items to order_items
INSERT INTO order_items (order_id, item_name, item_price, quantity, category)
SELECT @order_id, item_name, item_price, quantity, category
FROM cart_items
WHERE user_id = 1;

-- Step 3: Clear cart
DELETE FROM cart_items WHERE user_id = 1;

-- If all successful
COMMIT;

-- If any error
-- ROLLBACK;
```

### 7.2 Why Transactions?

**ACID Properties Ensured:**
- **Atomicity:** All steps succeed or all fail
- **Consistency:** Database remains in valid state
- **Isolation:** Concurrent transactions don't interfere
- **Durability:** Committed changes are permanent

---

## 8. Indexing

### 8.1 Existing Indexes

#### Primary Key Indexes (Automatic)
```sql
users.id
otps.id
cart_items.id
orders.id
order_items.id
```

#### Unique Indexes
```sql
users.email (UNIQUE)
```

#### Foreign Key Indexes (Automatic)
```sql
cart_items.user_id
orders.user_id
order_items.order_id
```

#### Custom Indexes
```sql
users.created_at
otps.email
otps.expires_at
cart_items.added_at
orders.status
orders.created_at
```

### 8.2 Index Benefits

**Query Performance:**
```sql
-- Without index: Full table scan
SELECT * FROM users WHERE email = 'john@example.com';
-- Time: O(n)

-- With index: Direct lookup
-- Time: O(log n)
```

**Join Performance:**
```sql
-- Foreign key indexes speed up joins
SELECT * FROM orders o
INNER JOIN users u ON o.user_id = u.id;
-- Fast because user_id is indexed
```

---

## 9. Database Operations

### 9.1 User Registration Flow

```sql
-- 1. Check if email exists
SELECT id FROM users WHERE email = 'new@example.com';

-- 2. Generate OTP
INSERT INTO otps (email, otp_code, expires_at)
VALUES ('new@example.com', '123456', DATE_ADD(NOW(), INTERVAL 5 MINUTE));

-- 3. Verify OTP
SELECT * FROM otps 
WHERE email = 'new@example.com' 
AND otp_code = '123456'
AND expires_at > NOW()
AND is_used = FALSE;

-- 4. Create user
INSERT INTO users (name, email, password_hash, is_verified)
VALUES ('New User', 'new@example.com', '$2b$12$...', TRUE);

-- 5. Mark OTP as used
UPDATE otps SET is_used = TRUE WHERE id = 1;
```

### 9.2 Shopping Cart Operations

```sql
-- Add to cart (check if exists)
INSERT INTO cart_items (user_id, item_name, item_price, quantity, category)
VALUES (1, 'Gulab Jamun', 50, 2, 'Desserts')
ON DUPLICATE KEY UPDATE quantity = quantity + 2;

-- View cart with total
SELECT 
    item_name,
    item_price,
    quantity,
    (item_price * quantity) AS subtotal
FROM cart_items
WHERE user_id = 1;

SELECT SUM(item_price * quantity) AS cart_total
FROM cart_items
WHERE user_id = 1;

-- Update quantity
UPDATE cart_items 
SET quantity = 3 
WHERE id = 1 AND user_id = 1;

-- Remove item
DELETE FROM cart_items 
WHERE id = 1 AND user_id = 1;
```

### 9.3 Order Management

```sql
-- Place order (transaction shown in section 7)

-- View order history
SELECT 
    id,
    total_amount,
    status,
    created_at
FROM orders
WHERE user_id = 1
ORDER BY created_at DESC;

-- View order details
SELECT 
    oi.item_name,
    oi.item_price,
    oi.quantity,
    (oi.item_price * oi.quantity) AS item_total
FROM order_items oi
WHERE oi.order_id = 1;

-- Cancel order
UPDATE orders 
SET status = 'Cancelled' 
WHERE id = 1 AND user_id = 1 AND status = 'Pending';
```

---

## 10. ACID Properties

### 10.1 Atomicity
**All or Nothing**

```sql
START TRANSACTION;
-- Multiple operations
-- Either all succeed or all fail
COMMIT; -- or ROLLBACK;
```

**Example:** Order placement
- Create order record
- Copy cart items
- Clear cart
- All must succeed together

### 10.2 Consistency
**Valid State Always**

**Constraints ensure consistency:**
- Foreign keys prevent orphan records
- NOT NULL prevents missing data
- UNIQUE prevents duplicates
- CHECK constraints (if used)

### 10.3 Isolation
**Concurrent Transactions**

**Isolation Levels:**
```sql
-- Default: REPEATABLE READ
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

**Prevents:**
- Dirty reads
- Non-repeatable reads
- Phantom reads

### 10.4 Durability
**Permanent Changes**

**InnoDB ensures:**
- Committed transactions survive crashes
- Write-ahead logging
- Transaction logs
- Data recovery

---

## 📊 Database Statistics

### Current Data (Sample):
- **Users:** 3
- **Cart Items:** 3
- **Orders:** 3
- **Order Items:** 7
- **OTPs:** Variable (cleaned up)

### Storage:
- **Engine:** InnoDB
- **Approximate Size:** ~100 KB (with sample data)
- **Growth Rate:** ~10 KB per 100 orders

---

## 🔒 Security Features

### 1. Password Security
```sql
-- Passwords stored as hashes (bcrypt)
password_hash VARCHAR(255) -- $2b$12$...
```

### 2. SQL Injection Prevention
```python
# Using ORM (SQLAlchemy)
User.query.filter_by(email=email).first()
# Parameterized queries prevent injection
```

### 3. Data Isolation
```sql
-- User-specific queries
SELECT * FROM cart_items WHERE user_id = ?
SELECT * FROM orders WHERE user_id = ?
```

---

## 📈 Performance Optimization

### 1. Indexes
- Primary keys
- Foreign keys
- Frequently queried columns

### 2. Query Optimization
- Use EXPLAIN to analyze queries
- Avoid SELECT *
- Use appropriate JOINs

### 3. Connection Pooling
- Reuse database connections
- Reduce connection overhead

---

## ✅ Database Best Practices Implemented

1. ✅ Proper normalization (3NF)
2. ✅ Foreign key constraints
3. ✅ Indexes on frequently queried columns
4. ✅ CASCADE DELETE for referential integrity
5. ✅ Transactions for atomic operations
6. ✅ Appropriate data types
7. ✅ Default values where applicable
8. ✅ Timestamps for audit trail
9. ✅ UTF-8 character encoding
10. ✅ InnoDB storage engine

---

**This is a complete DBMS implementation following industry standards!** 🎉
