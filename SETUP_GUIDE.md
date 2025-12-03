# Restaurant Project - MySQL Setup Guide

## 📋 What You Need to Show Your Teacher

1. **XAMPP** - Software that gives you MySQL database + phpMyAdmin
2. **MySQL Database** - Where all data is stored (users, cart, orders)
3. **phpMyAdmin** - Web interface to view database tables and data
4. **Working Application** - Sign up, login, add to cart, place orders

---

## 🔧 Step-by-Step Installation

### Step 1: Install XAMPP

1. Download XAMPP from: https://www.apachefriends.org/
2. Install it (default location: `C:\xampp`)
3. Open **XAMPP Control Panel**
4. Click **Start** button for:
   - ✅ Apache (web server)
   - ✅ MySQL (database)

**Both should show green "Running" status**

---

### Step 2: Install Python Dependencies

Open Command Prompt in your project folder and run:

```cmd
pip install -r requirements.txt
```

This installs:
- Flask (web framework)
- pymysql (MySQL connector)
- Other required packages

---

### Step 3: Create MySQL Database

Run the database initialization script:

```cmd
python init_mysql_db.py
```

This will:
- Create database named `restaurant_db`
- Create 5 tables: users, otps, cart_items, orders, order_items

---

### Step 4: Run Your Application

```cmd
python app.py
```

Open browser and go to: http://localhost:5000

---

## 🎯 How to Show Data to Your Teacher

### Method 1: Using phpMyAdmin (RECOMMENDED)

1. Open browser → http://localhost/phpmyadmin
2. Click on `restaurant_db` database (left sidebar)
3. You'll see all tables:
   - **users** - All registered users
   - **cart_items** - Items in shopping carts
   - **orders** - All placed orders
   - **order_items** - Details of items in each order
   - **otps** - OTP verification codes

4. Click any table name to view data
5. Click "Browse" tab to see all records

### Method 2: Using SQL Queries in phpMyAdmin

Click "SQL" tab and run these queries:

```sql
-- View all users
SELECT * FROM users;

-- View all orders with user details
SELECT o.id, u.name, u.email, o.total_amount, o.status, o.created_at 
FROM orders o 
JOIN users u ON o.user_id = u.id;

-- View order items with details
SELECT oi.*, o.status, u.name as customer_name
FROM order_items oi
JOIN orders o ON oi.order_id = o.id
JOIN users u ON o.user_id = u.id;

-- View cart items
SELECT c.*, u.name as customer_name
FROM cart_items c
JOIN users u ON c.user_id = u.id;

-- Count total orders
SELECT COUNT(*) as total_orders FROM orders;

-- Total revenue
SELECT SUM(total_amount) as total_revenue FROM orders WHERE status != 'Cancelled';
```

---

## 📊 Database Structure Explanation

### Table: users
Stores user account information
- `id` - Unique user ID
- `name` - User's full name
- `email` - Login email (unique)
- `password_hash` - Encrypted password
- `is_verified` - Email verification status
- `created_at` - Registration date

### Table: cart_items
Stores items in user's shopping cart
- `id` - Cart item ID
- `user_id` - Which user's cart
- `item_name` - Food item name
- `item_price` - Price per item
- `quantity` - Number of items
- `category` - Food category
- `added_at` - When added to cart

### Table: orders
Stores order information
- `id` - Order ID
- `user_id` - Customer who placed order
- `total_amount` - Total bill amount
- `status` - Pending/Confirmed/Delivered/Cancelled
- `delivery_address` - Where to deliver
- `phone_number` - Contact number
- `created_at` - Order date/time

### Table: order_items
Stores individual items in each order
- `id` - Item ID
- `order_id` - Which order
- `item_name` - Food item name
- `item_price` - Price at time of order
- `quantity` - Number ordered
- `category` - Food category

---

## 🎬 Demo Flow for Teacher

### 1. Show Database in phpMyAdmin
- Open http://localhost/phpmyadmin
- Show `restaurant_db` database
- Show all 5 tables

### 2. Register New User
- Go to http://localhost:5000
- Click Register
- Fill form and submit
- Show OTP in `otps` table (phpMyAdmin)
- Complete registration
- Show new user in `users` table

### 3. Login
- Login with registered credentials
- Show session is active

### 4. Add Items to Cart
- Browse menu pages (Desserts, Veg, Street Chaat, etc.)
- Add items to cart
- Show cart items in `cart_items` table (phpMyAdmin)

### 5. Place Order
- Go to Cart
- Click Checkout
- Fill delivery details
- Place order
- Show new order in `orders` table
- Show order items in `order_items` table
- Show cart is now empty

### 6. View Orders
- Click "My Orders"
- Show order history
- Click on order to view details

---

## 🔍 Key Terms Explained

### XAMPP
- **X** = Cross-platform
- **A** = Apache (web server)
- **M** = MySQL (database)
- **P** = PHP (programming language)
- **P** = Perl (programming language)

**Purpose**: Installs everything needed to run web applications with databases

### MySQL
- Database management system
- Stores data in tables (like Excel sheets)
- Uses SQL language to query data
- Industry standard for web applications

### phpMyAdmin
- Web-based interface for MySQL
- View/edit database without writing code
- Visual way to manage tables and data
- Comes free with XAMPP

### SQL (Structured Query Language)
- Language to communicate with databases
- Commands: SELECT, INSERT, UPDATE, DELETE
- Used to retrieve and manipulate data

### How They Connect
```
XAMPP (installs) → MySQL (database) + phpMyAdmin (interface)
                ↓
Your Flask App (connects to) → MySQL (stores data)
                ↓
phpMyAdmin (shows) → Data in MySQL
```

---

## 🐛 Troubleshooting

### MySQL won't start in XAMPP
- Port 3306 might be busy
- Stop any other MySQL services
- Click "Config" → "my.ini" → change port to 3307
- Update app.py: `localhost:3307/restaurant_db`

### Can't connect to database
- Make sure MySQL is running (green in XAMPP)
- Check database name is `restaurant_db`
- Default username: `root`
- Default password: (empty)

### Tables not created
- Run `python init_mysql_db.py` again
- Check for error messages
- Make sure MySQL is running

---

## 📝 What to Tell Your Teacher

"Sir/Ma'am, I have created a restaurant management system using:

1. **Backend**: Python Flask framework
2. **Database**: MySQL (via XAMPP)
3. **Features**: 
   - User registration with email verification
   - Login/Logout system
   - Shopping cart functionality
   - Order placement and tracking
   - Order history

4. **Database Tables**: 5 tables storing all data
   - Users table for accounts
   - Cart table for shopping cart
   - Orders table for order details
   - Order items table for item details
   - OTP table for verification

5. **Data Viewing**: Using phpMyAdmin to show all stored data in MySQL database

6. **SQL Queries**: Can run SQL queries to fetch and display data"

---

## 🎓 Additional SQL Queries for Demonstration

```sql
-- Show users who placed orders
SELECT DISTINCT u.name, u.email, COUNT(o.id) as total_orders
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id;

-- Show most ordered items
SELECT item_name, SUM(quantity) as times_ordered, SUM(item_price * quantity) as revenue
FROM order_items
GROUP BY item_name
ORDER BY times_ordered DESC;

-- Show pending orders
SELECT o.id, u.name, o.total_amount, o.created_at
FROM orders o
JOIN users u ON o.user_id = u.id
WHERE o.status = 'Pending';

-- Show revenue by category
SELECT category, SUM(item_price * quantity) as revenue
FROM order_items
GROUP BY category;
```

---

## ✅ Checklist Before Presentation

- [ ] XAMPP installed and running
- [ ] MySQL service is green/running
- [ ] Database `restaurant_db` created
- [ ] All 5 tables exist
- [ ] Flask app runs without errors
- [ ] Can register new user
- [ ] Can login
- [ ] Can add items to cart
- [ ] Can place order
- [ ] Can view orders
- [ ] phpMyAdmin shows all data
- [ ] Know how to run SQL queries

---

Good luck with your presentation! 🎉
