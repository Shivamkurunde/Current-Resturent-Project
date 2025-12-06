# 🍽️ Restaurant Management System

**Student Name:** Shivam Kurunde  
**Roll No:** 123  
**Class:** TYCSEA  
**Project Title:** Restaurant Management System  

---

## 📋 Project Overview

A complete Restaurant Management System built with Python Flask and MySQL database. This project demonstrates database management concepts including user authentication, shopping cart functionality, and order management.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python 3.x, Flask |
| Database | MySQL (via XAMPP) |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, JavaScript |
| Database Interface | phpMyAdmin |

---

## 📊 Database Schema

### Tables (5 Total):

1. **users** - User accounts and authentication
2. **otps** - Email verification codes
3. **cart_items** - Shopping cart items
4. **orders** - Order information
5. **order_items** - Items in each order

---

## ✨ Features

- ✅ User Registration with OTP Verification
- ✅ User Login/Logout
- ✅ Password Hashing (Security)
- ✅ Shopping Cart (Add, Update, Remove items)
- ✅ Order Placement
- ✅ Order History & Tracking
- ✅ Order Cancellation
- ✅ MySQL Database Integration
- ✅ phpMyAdmin for Data Visualization

---

## 🚀 Setup Instructions

### Prerequisites

1. **Python 3.7+** installed
2. **XAMPP** installed (for MySQL and phpMyAdmin)

### Step 1: Install XAMPP

1. Download from: https://www.apachefriends.org/
2. Install XAMPP
3. Open XAMPP Control Panel
4. Start **Apache** and **MySQL** services (both should be GREEN)

### Step 2: Clone Repository

```bash
git clone https://github.com/Shivamkurunde/Shivamkurende_123_TYCSEA_ResturantManagementSystem.git
cd Shivamkurende_123_TYCSEA_ResturantManagementSystem
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment

1. Copy `.env.example` to `.env`
2. Update the values in `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=mysql+pymysql://root:@localhost/restaurant_db
SENDGRID_API_KEY=your-sendgrid-api-key
MAIL_DEFAULT_SENDER=your-email@example.com
```

### Step 5: Initialize Database

```bash
python init_mysql_db.py
```

This creates:
- Database: `restaurant_db`
- All 5 tables with proper relationships

### Step 6: Add Sample Data (Optional)

```bash
python add_sample_data.py
```

### Step 7: Run Application

```bash
python app.py
```

### Step 8: Access Application

- **Application:** http://localhost:5000
- **phpMyAdmin:** http://localhost/phpmyadmin
- **Database:** restaurant_db

---

## 📖 Usage Guide

### For Users:

1. **Register** - Create account with email verification
2. **Login** - Access your account
3. **Browse Menu** - View food items by category
4. **Add to Cart** - Select items and quantities
5. **Checkout** - Enter delivery details
6. **Place Order** - Confirm and submit order
7. **Track Orders** - View order history and status

### For Database Viewing:

1. Open phpMyAdmin: http://localhost/phpmyadmin
2. Select `restaurant_db` database
3. View tables and data
4. Run SQL queries

---

## 📊 Sample SQL Queries

```sql
-- View all users
SELECT * FROM users;

-- View all orders with customer details
SELECT o.id, u.name, u.email, o.total_amount, o.status 
FROM orders o 
JOIN users u ON o.user_id = u.id;

-- Calculate total revenue
SELECT SUM(total_amount) as total_revenue FROM orders;

-- Most ordered items
SELECT item_name, SUM(quantity) as times_ordered 
FROM order_items 
GROUP BY item_name 
ORDER BY times_ordered DESC;
```

---

## 📁 Project Structure

```
├── app.py                    # Main Flask application
├── models.py                 # Database models
├── init_mysql_db.py          # Database initialization
├── add_sample_data.py        # Sample data generator
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
├── README.md                 # This file
│
├── templates/                # HTML templates
│   ├── auth/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── verify_otp.html
│   ├── home.html
│   ├── cart.html
│   ├── checkout.html
│   ├── my_orders.html
│   └── order_details.html
│
├── static/                   # CSS, JS, Images
│   ├── Experiment.css
│   ├── Experiment.js
│   └── images/
│
└── Documentation/            # Project documentation
    ├── SETUP_GUIDE.md
    ├── HINDI_GUIDE.md
    ├── SQL_QUERIES_REFERENCE.sql
    └── PRESENTATION_CHECKLIST.md
```

---

## 📚 Documentation Files

| File | Description |
|------|-------------|
| `SETUP_GUIDE.md` | Detailed setup instructions |
| `HINDI_GUIDE.md` | Complete guide in Hindi |
| `SQL_QUERIES_REFERENCE.sql` | 34 ready-to-use SQL queries |
| `PRESENTATION_CHECKLIST.md` | Demo preparation guide |
| `TESTING_GUIDE.md` | Testing procedures |
| `ARCHITECTURE_DIAGRAM.txt` | System architecture |

---

## 🔐 Security Features

- Password hashing using Werkzeug
- Session-based authentication
- SQL injection prevention (ORM)
- Environment variables for secrets
- OTP-based email verification

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **Database Design** - Relational tables with foreign keys
2. **SQL Operations** - CRUD operations, JOINs, aggregations
3. **Web Development** - Flask framework, routing, templates
4. **Authentication** - User registration, login, sessions
5. **E-commerce Logic** - Cart, checkout, order management

---

## 📞 Troubleshooting

### MySQL won't start:
- Restart XAMPP
- Check port 3306 is free
- Run XAMPP as Administrator

### Database connection error:
- Verify MySQL is running
- Check DATABASE_URL in .env
- Run `python init_mysql_db.py`

### App won't run:
- Install dependencies: `pip install -r requirements.txt`
- Check .env file exists
- Verify Python version

---

## 📄 Submission Details

- **Student:** Shivam Kurunde
- **Roll No:** 123
- **Class:** TYCSEA
- **Project:** Restaurant Management System
- **Submission Date:** December 2024

### Submission Contents:
- ✅ Complete Project Code
- ✅ requirements.txt
- ✅ README.md
- ✅ Documentation files
- ✅ SQL queries reference

---

## 📝 License

This project is created for academic purposes as part of Database Management System coursework.

---

## 🙏 Acknowledgments

- Flask Documentation
- SQLAlchemy Documentation
- MySQL Documentation
- XAMPP Community

---

**Made with ❤️ by Shivam Kurunde**
