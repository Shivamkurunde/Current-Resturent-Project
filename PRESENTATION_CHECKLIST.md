# 📋 Presentation Checklist

## Before Starting (Presentation से पहले)

### ✅ Installation Check
- [ ] XAMPP installed at `C:\xampp`
- [ ] XAMPP Control Panel opens
- [ ] Apache service starts (shows green)
- [ ] MySQL service starts (shows green)
- [ ] Python installed (check: `python --version`)
- [ ] All packages installed (`pip install -r requirements.txt`)

### ✅ Database Check
- [ ] Run `python init_mysql_db.py` successfully
- [ ] Open http://localhost/phpmyadmin
- [ ] Database `restaurant_db` exists
- [ ] All 5 tables visible:
  - [ ] users
  - [ ] otps
  - [ ] cart_items
  - [ ] orders
  - [ ] order_items

### ✅ Application Check
- [ ] Run `python app.py` without errors
- [ ] Open http://localhost:5000
- [ ] Home page loads
- [ ] All menu pages work (Desserts, Veg, Street Chaat, etc.)

---

## During Presentation (Presentation के दौरान)

### Part 1: Introduction (2 minutes)
- [ ] Explain project purpose: "Restaurant Management System"
- [ ] Mention technologies: Python Flask + MySQL
- [ ] Show project features list

### Part 2: Show Database Structure (3 minutes)
- [ ] Open phpMyAdmin: http://localhost/phpmyadmin
- [ ] Click on `restaurant_db`
- [ ] Show all 5 tables
- [ ] Click on each table and explain:
  - [ ] **users** - "Stores customer accounts"
  - [ ] **otps** - "For email verification"
  - [ ] **cart_items** - "Shopping cart data"
  - [ ] **orders** - "Order information"
  - [ ] **order_items** - "Items in each order"

### Part 3: Live Demo - Registration (3 minutes)
- [ ] Open app: http://localhost:5000
- [ ] Click "Register" or go to http://localhost:5000/register
- [ ] Fill form with test data:
  - Name: Test User
  - Email: test@example.com
  - Password: test123
- [ ] Submit form
- [ ] **Switch to phpMyAdmin**
- [ ] Open `otps` table → Show OTP code
- [ ] Copy OTP code
- [ ] **Back to app** → Enter OTP
- [ ] Complete registration
- [ ] **Back to phpMyAdmin**
- [ ] Open `users` table → Show new user added
- [ ] Point out: email, name, password_hash, is_verified=1

### Part 4: Live Demo - Login (2 minutes)
- [ ] Go to login page
- [ ] Enter credentials (test@example.com / test123)
- [ ] Login successfully
- [ ] Show welcome message with user name

### Part 5: Live Demo - Shopping Cart (4 minutes)
- [ ] Browse to Desserts page
- [ ] Add "Gulab Jamun" to cart (if available)
- [ ] Browse to Veg page
- [ ] Add "Paneer Tikka" to cart (if available)
- [ ] **Switch to phpMyAdmin**
- [ ] Open `cart_items` table
- [ ] Show items added with:
  - user_id
  - item_name
  - item_price
  - quantity
- [ ] **Back to app**
- [ ] Go to Cart page
- [ ] Show cart items
- [ ] Update quantity (optional)

### Part 6: Live Demo - Place Order (4 minutes)
- [ ] Click "Checkout" from cart
- [ ] Fill delivery details:
  - Phone: 9876543210
  - Address: "123 Test Street, Mumbai"
- [ ] Click "Place Order"
- [ ] Note the Order ID shown
- [ ] **Switch to phpMyAdmin**
- [ ] Open `orders` table
- [ ] Show new order with:
  - order_id
  - user_id
  - total_amount
  - status (Pending)
  - delivery_address
  - phone_number
- [ ] Open `order_items` table
- [ ] Show items in the order
- [ ] Open `cart_items` table
- [ ] Show cart is now empty

### Part 7: Live Demo - Order History (2 minutes)
- [ ] Go to "My Orders" page
- [ ] Show order list
- [ ] Click on order to view details
- [ ] Show complete order information

### Part 8: SQL Queries Demo (5 minutes)
- [ ] Open phpMyAdmin → SQL tab
- [ ] Run Query 1: Show all users
  ```sql
  SELECT * FROM users;
  ```
- [ ] Run Query 2: Show orders with customer names
  ```sql
  SELECT o.id, u.name, o.total_amount, o.status 
  FROM orders o 
  JOIN users u ON o.user_id = u.id;
  ```
- [ ] Run Query 3: Total revenue
  ```sql
  SELECT SUM(total_amount) as total_revenue FROM orders;
  ```
- [ ] Run Query 4: Most ordered items
  ```sql
  SELECT item_name, SUM(quantity) as times_ordered
  FROM order_items
  GROUP BY item_name
  ORDER BY times_ordered DESC;
  ```

### Part 9: Explain Database Relationships (2 minutes)
- [ ] Draw/explain on board:
  ```
  users (1) -----> (many) orders
  orders (1) -----> (many) order_items
  users (1) -----> (many) cart_items
  ```
- [ ] Explain Foreign Keys:
  - cart_items.user_id → users.id
  - orders.user_id → users.id
  - order_items.order_id → orders.id

### Part 10: Conclusion (2 minutes)
- [ ] Summarize features:
  - User registration with OTP
  - Login system
  - Shopping cart
  - Order placement
  - Order tracking
- [ ] Mention data storage in MySQL
- [ ] Mention phpMyAdmin for data viewing
- [ ] Thank teacher

---

## Emergency Backup Plan

### If MySQL doesn't start:
1. Restart XAMPP
2. Check port 3306 is free
3. Use SQLite as backup (change .env)

### If phpMyAdmin doesn't open:
1. Check Apache is running
2. Try http://127.0.0.1/phpmyadmin
3. Restart XAMPP

### If app doesn't run:
1. Check all packages installed
2. Check .env file exists
3. Check MySQL is running
4. Run `python init_mysql_db.py` again

### If demo data needed quickly:
Run these in Python:
```python
from app import app, db
from models import User, CartItem, Order, OrderItem

with app.app_context():
    # Create test user
    user = User(name="Demo User", email="demo@test.com", is_verified=True)
    user.set_password("demo123")
    db.session.add(user)
    db.session.commit()
```

---

## Questions Teacher Might Ask

### Q1: "What is the difference between MySQL and SQLite?"
**Answer:** 
- SQLite: File-based, single user, good for development
- MySQL: Server-based, multi-user, good for production
- MySQL is industry standard for web applications

### Q2: "Why use XAMPP?"
**Answer:**
- Easy installation of MySQL + phpMyAdmin
- No complex configuration needed
- Industry standard for local development
- Free and open source

### Q3: "What is a Foreign Key?"
**Answer:**
- Links two tables together
- Example: cart_items.user_id references users.id
- Maintains data integrity
- Prevents orphan records

### Q4: "How is password stored?"
**Answer:**
- Not stored as plain text
- Hashed using werkzeug.security
- One-way encryption
- Secure against database breaches

### Q5: "Can you show me the SQL to create these tables?"
**Answer:**
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
(Show similar for other tables)

### Q6: "How does OTP verification work?"
**Answer:**
1. User registers
2. System generates 6-digit OTP
3. OTP stored in database with expiry time
4. OTP sent to email
5. User enters OTP
6. System verifies from database
7. If valid, account activated

### Q7: "What happens when order is placed?"
**Answer:**
1. Cart items fetched from database
2. New order created in orders table
3. Each cart item copied to order_items table
4. Cart items deleted
5. All in single transaction (atomic)

---

## Files to Keep Open During Presentation

1. **XAMPP Control Panel** - To show services running
2. **Browser Tab 1** - http://localhost:5000 (Your app)
3. **Browser Tab 2** - http://localhost/phpmyadmin (Database)
4. **Text Editor** - SQL_QUERIES_REFERENCE.sql (For copy-paste)
5. **Command Prompt** - In project folder (if needed to restart)

---

## Time Management

| Section | Time | Total |
|---------|------|-------|
| Introduction | 2 min | 2 min |
| Database Structure | 3 min | 5 min |
| Registration Demo | 3 min | 8 min |
| Login Demo | 2 min | 10 min |
| Cart Demo | 4 min | 14 min |
| Order Demo | 4 min | 18 min |
| Order History | 2 min | 20 min |
| SQL Queries | 5 min | 25 min |
| Relationships | 2 min | 27 min |
| Conclusion | 2 min | 29 min |
| Q&A Buffer | 1 min | 30 min |

---

## Final Check (5 minutes before presentation)

- [ ] XAMPP running (Apache + MySQL green)
- [ ] phpMyAdmin opens
- [ ] App runs (python app.py)
- [ ] Home page loads
- [ ] Database has some test data (or ready to create live)
- [ ] SQL_QUERIES_REFERENCE.sql file open
- [ ] Confident and ready!

---

## 🎯 Key Points to Remember

1. **Confidence is key** - You built this, you know it!
2. **Speak clearly** - Explain each step
3. **Show, don't just tell** - Live demo is powerful
4. **Connect theory to practice** - Show how SQL queries work on real data
5. **Be ready for questions** - It's okay to say "Let me check"
6. **Smile** - You've done great work!

---

## 🌟 Bonus Points

If time permits, show these impressive features:
- [ ] Order cancellation
- [ ] Cart quantity update
- [ ] Multiple users with different orders
- [ ] Revenue calculation query
- [ ] Category-wise sales report

---

**Good luck! You've got this! 🚀**
