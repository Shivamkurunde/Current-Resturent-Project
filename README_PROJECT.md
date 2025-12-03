# 🍽️ Restaurant Management System

A complete restaurant management system with user authentication, shopping cart, and order management built with Python Flask and MySQL.

---

## 📌 Project Overview

This project demonstrates a full-stack web application for restaurant management with:
- User registration and authentication with OTP verification
- Shopping cart functionality
- Order placement and tracking
- MySQL database for data persistence
- phpMyAdmin for database visualization

---

## 🛠️ Technology Stack

### Backend
- **Python 3.x** - Programming language
- **Flask** - Web framework
- **SQLAlchemy** - ORM for database operations
- **MySQL** - Relational database
- **PyMySQL** - MySQL connector for Python

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity

### Tools
- **XAMPP** - Local server environment (Apache + MySQL + phpMyAdmin)
- **SendGrid** - Email service for OTP delivery

---

## 📊 Database Schema

### Tables

#### 1. users
Stores user account information
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- name (VARCHAR(100))
- email (VARCHAR(120), UNIQUE)
- password_hash (VARCHAR(255))
- is_verified (BOOLEAN)
- created_at (DATETIME)
```

#### 2. otps
Stores OTP codes for email verification
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- email (VARCHAR(120))
- otp_code (VARCHAR(10))
- created_at (DATETIME)
- expires_at (DATETIME)
- is_used (BOOLEAN)
```

#### 3. cart_items
Stores shopping cart items
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY → users.id)
- item_name (VARCHAR(200))
- item_price (FLOAT)
- quantity (INT)
- category (VARCHAR(100))
- added_at (DATETIME)
```

#### 4. orders
Stores order information
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY → users.id)
- total_amount (FLOAT)
- status (VARCHAR(50))
- delivery_address (TEXT)
- phone_number (VARCHAR(20))
- created_at (DATETIME)
- updated_at (DATETIME)
```

#### 5. order_items
Stores items in each order
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- order_id (INT, FOREIGN KEY → orders.id)
- item_name (VARCHAR(200))
- item_price (FLOAT)
- quantity (INT)
- category (VARCHAR(100))
```

---

## 🚀 Features

### User Management
- ✅ User registration with email validation
- ✅ OTP-based email verification
- ✅ Secure password hashing
- ✅ Login/Logout functionality
- ✅ Session management

### Shopping Cart
- ✅ Add items to cart
- ✅ Update item quantities
- ✅ Remove items from cart
- ✅ Clear entire cart
- ✅ Real-time total calculation

### Order Management
- ✅ Place orders with delivery details
- ✅ View order history
- ✅ View detailed order information
- ✅ Cancel pending orders
- ✅ Order status tracking (Pending, Confirmed, Delivered, Cancelled)

### Menu Categories
- 🍰 Desserts & Ice Cream
- 🥗 Veg Items
- 🍟 Street Chaat
- 💪 Gym Food (Protein, Detox, Shakes)

---

## 📁 Project Structure

```
restaurant-project/
│
├── app.py                          # Main Flask application
├── models.py                       # Database models
├── init_mysql_db.py               # Database initialization script
├── otp_service.py                 # OTP service (base)
├── sendgrid_otp_service.py        # SendGrid OTP implementation
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
│
├── templates/                     # HTML templates
│   ├── auth/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── verify_otp.html
│   ├── home.html
│   ├── cart.html
│   ├── checkout.html
│   ├── my_orders.html
│   ├── order_details.html
│   └── [menu pages...]
│
├── static/                        # Static files
│   ├── Experiment.css
│   ├── Experiment.js
│   └── images/
│
├── instance/                      # Database files
│   └── restaurant.db (SQLite - old)
│
└── Documentation/
    ├── SETUP_GUIDE.md            # Detailed setup instructions
    ├── HINDI_GUIDE.md            # Hindi language guide
    ├── SQL_QUERIES_REFERENCE.sql # SQL queries for demo
    └── PRESENTATION_CHECKLIST.md # Presentation guide
```

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- XAMPP (for MySQL and phpMyAdmin)

### Step 1: Install XAMPP
1. Download from https://www.apachefriends.org/
2. Install to default location (C:\xampp)
3. Open XAMPP Control Panel
4. Start Apache and MySQL services

### Step 2: Clone/Download Project
```bash
cd path/to/your/project
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
Edit `.env` file with your settings:
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

This will:
- Create `restaurant_db` database
- Create all required tables
- Set up proper relationships

### Step 6: Run Application
```bash
python app.py
```

Open browser: http://localhost:5000

---

## 🌐 Accessing phpMyAdmin

1. Make sure Apache and MySQL are running in XAMPP
2. Open browser: http://localhost/phpmyadmin
3. Click on `restaurant_db` database
4. View all tables and data

---

## 📖 Usage Guide

### For Users

1. **Register Account**
   - Go to Register page
   - Fill in name, email, password
   - Verify email with OTP
   - Account created!

2. **Login**
   - Enter email and password
   - Access full features

3. **Browse Menu**
   - Navigate through different categories
   - View items with prices

4. **Add to Cart**
   - Click "Add to Cart" on any item
   - Adjust quantities as needed

5. **Checkout**
   - Review cart items
   - Enter delivery address and phone
   - Place order

6. **Track Orders**
   - View "My Orders"
   - See order status
   - View order details

### For Developers

1. **Database Operations**
   ```python
   from app import app, db
   from models import User, Order, CartItem
   
   with app.app_context():
       # Query users
       users = User.query.all()
       
       # Create new user
       user = User(name="Test", email="test@example.com")
       db.session.add(user)
       db.session.commit()
   ```

2. **Running SQL Queries**
   - Open phpMyAdmin
   - Go to SQL tab
   - Paste query from SQL_QUERIES_REFERENCE.sql
   - Click "Go"

---

## 🔐 Security Features

- **Password Hashing**: Using Werkzeug's secure password hashing
- **Session Management**: Flask sessions with secret key
- **OTP Verification**: Time-limited OTP codes
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **Login Required Decorator**: Protected routes

---

## 📊 Sample SQL Queries

### View all orders with customer details
```sql
SELECT o.id, u.name, u.email, o.total_amount, o.status, o.created_at 
FROM orders o 
JOIN users u ON o.user_id = u.id;
```

### Calculate total revenue
```sql
SELECT SUM(total_amount) as total_revenue 
FROM orders 
WHERE status != 'Cancelled';
```

### Most ordered items
```sql
SELECT item_name, SUM(quantity) as times_ordered
FROM order_items
GROUP BY item_name
ORDER BY times_ordered DESC;
```

More queries available in `SQL_QUERIES_REFERENCE.sql`

---

## 🎯 Key Concepts Demonstrated

### Database Concepts
- **Relational Database Design**: Proper table relationships
- **Foreign Keys**: Maintaining referential integrity
- **CRUD Operations**: Create, Read, Update, Delete
- **Joins**: Combining data from multiple tables
- **Aggregation**: SUM, COUNT, AVG functions
- **Transactions**: Atomic operations

### Web Development Concepts
- **MVC Pattern**: Model-View-Controller architecture
- **RESTful Routes**: Standard HTTP methods
- **Session Management**: User state persistence
- **Form Validation**: Input sanitization
- **Flash Messages**: User feedback
- **Template Rendering**: Dynamic HTML generation

### Software Engineering Concepts
- **ORM**: Object-Relational Mapping with SQLAlchemy
- **Environment Variables**: Configuration management
- **Decorators**: Login required functionality
- **Error Handling**: Try-catch blocks
- **Code Organization**: Separation of concerns

---

## 🐛 Troubleshooting

### MySQL won't start
- Check if port 3306 is available
- Stop other MySQL services
- Restart XAMPP

### Database connection error
- Verify MySQL is running
- Check DATABASE_URL in .env
- Run init_mysql_db.py again

### OTP not sending
- Check SENDGRID_API_KEY in .env
- Verify email address
- Check SendGrid account status

### App won't run
- Install all requirements: `pip install -r requirements.txt`
- Check Python version: `python --version`
- Look for error messages in console

---

## 📚 Documentation Files

- **SETUP_GUIDE.md** - Detailed English setup guide
- **HINDI_GUIDE.md** - Hindi language guide for easy understanding
- **SQL_QUERIES_REFERENCE.sql** - Ready-to-use SQL queries
- **PRESENTATION_CHECKLIST.md** - Step-by-step presentation guide

---

## 🎓 Learning Outcomes

After completing this project, you will understand:

1. **Database Management**
   - MySQL database creation and management
   - Table design and relationships
   - SQL queries and operations
   - phpMyAdmin usage

2. **Web Development**
   - Flask framework basics
   - Routing and views
   - Template rendering
   - Form handling

3. **Authentication**
   - User registration and login
   - Password hashing
   - Session management
   - OTP verification

4. **E-commerce Basics**
   - Shopping cart implementation
   - Order processing
   - Order tracking
   - Payment flow (structure)

---

## 🔄 Future Enhancements

Possible improvements:
- [ ] Payment gateway integration
- [ ] Admin panel for order management
- [ ] Real-time order status updates
- [ ] Email notifications for orders
- [ ] User profile management
- [ ] Order rating and reviews
- [ ] Discount codes and offers
- [ ] Multiple delivery addresses
- [ ] Order history export (PDF)
- [ ] Analytics dashboard

---

## 👨‍💻 Developer

**Project Type**: Academic/Learning Project  
**Purpose**: Demonstrate database integration with web application  
**Technologies**: Python, Flask, MySQL, HTML, CSS, JavaScript

---

## 📄 License

This is an educational project created for learning purposes.

---

## 🙏 Acknowledgments

- Flask documentation
- SQLAlchemy documentation
- MySQL documentation
- XAMPP community
- SendGrid API

---

## 📞 Support

For issues or questions:
1. Check SETUP_GUIDE.md
2. Check HINDI_GUIDE.md
3. Review error messages carefully
4. Check XAMPP services are running
5. Verify database connection

---

## ✅ Project Checklist

- [x] User registration with OTP
- [x] User login/logout
- [x] Shopping cart functionality
- [x] Order placement
- [x] Order tracking
- [x] MySQL database integration
- [x] phpMyAdmin access
- [x] Comprehensive documentation
- [x] SQL queries reference
- [x] Presentation guide

---

**Status**: ✅ Complete and Ready for Presentation

**Last Updated**: December 2024

---

## 🎉 Quick Start Summary

```bash
# 1. Start XAMPP (Apache + MySQL)
# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize database
python init_mysql_db.py

# 4. Run application
python app.py

# 5. Open browser
http://localhost:5000

# 6. View database
http://localhost/phpmyadmin
```

---

**Happy Coding! 🚀**
