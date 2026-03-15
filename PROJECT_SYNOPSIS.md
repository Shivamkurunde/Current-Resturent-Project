# RESTAURANT MANAGEMENT SYSTEM
## Project Synopsis

---

## 📋 PROJECT INFORMATION

**Project Title:** Restaurant Management System with Online Food Ordering

**Student Name:** Shivam Kurunde

**Roll Number:** 123

**Class:** TY CSE A

**Academic Year:** 2025-2026

**College:** [Your College Name]

**Guide:** [Guide Name]

---

## 🎯 PROJECT DEFINITION

The Restaurant Management System is a comprehensive web-based application designed to streamline restaurant operations and provide customers with a seamless online food ordering experience. The system enables users to browse menus, add items to cart, place orders, and track order history while providing restaurant administrators with tools to manage inventory, orders, and customer data.

---

## 💡 MOTIVATION BEHIND PROJECT

In the modern digital era, restaurants need efficient systems to manage operations and serve customers effectively. Traditional manual ordering systems are time-consuming and prone to errors. This project addresses these challenges by:

- **Eliminating Manual Errors:** Automated order processing reduces human errors
- **Improving Customer Experience:** Easy-to-use interface for browsing and ordering
- **Streamlining Operations:** Centralized system for managing orders and inventory
- **Data-Driven Insights:** Track customer preferences and order patterns
- **Contactless Ordering:** Modern solution for post-pandemic dining preferences

---

## 📖 PROJECT OVERVIEW

The Restaurant Management System is a full-stack web application built using Python Flask framework with MySQL database backend. The system provides a user-friendly interface for customers to:

- Register and create accounts with email verification
- Browse categorized food menus (Vegetarian, Street Chaat, Desserts, Gym Food)
- Add items to shopping cart
- Place orders with delivery details
- Track order history and status
- Manage user profiles

The system architecture follows the MVC (Model-View-Controller) pattern, ensuring clean separation of concerns and maintainable code structure.

---

## 🎯 PROJECT SCOPE

### **In Scope:**
- User registration and authentication system
- Email-based OTP verification
- Menu browsing with multiple categories
- Shopping cart management
- Order placement and tracking
- Order history and details view
- User profile management
- Database-driven dynamic content
- Responsive web design
- Admin dashboard for data viewing (phpMyAdmin)

### **Out of Scope:**
- Payment gateway integration
- Real-time order tracking with GPS
- Mobile application development
- Multi-restaurant support
- Delivery personnel management
- Advanced analytics and reporting
- Third-party API integrations

---

## 🎯 OBJECTIVES

1. **Primary Objectives:**
   - Develop a functional online food ordering system
   - Implement secure user authentication and authorization
   - Create an intuitive user interface for menu browsing
   - Enable seamless cart and order management
   - Maintain comprehensive order history

2. **Secondary Objectives:**
   - Demonstrate proficiency in full-stack web development
   - Apply database design principles (normalization, relationships)
   - Implement secure coding practices
   - Create comprehensive project documentation
   - Showcase modern web technologies

3. **Learning Objectives:**
   - Understand MVC architecture pattern
   - Master Flask framework for web development
   - Learn database design and SQL operations
   - Implement user authentication and session management
   - Practice version control with Git/GitHub

---

## 👥 USER ROLES & ACCOUNT HANDLING

### **1. Regular Users (Customers)**
**Capabilities:**
- Register new account with email verification
- Login with email and password
- Browse food menu by categories
- Add/remove items from cart
- Update cart quantities
- Place orders with delivery information
- View order history
- View order details and status
- Update profile information
- Logout securely

**Access Level:** Limited to personal data and ordering functions

### **2. Administrator**
**Capabilities:**
- Access database through phpMyAdmin
- View all user accounts
- Monitor all orders
- View cart items across users
- Execute SQL queries for data analysis
- Manage database tables
- Export data for reporting

**Access Level:** Full database access and system monitoring

### **3. Guest Users**
**Capabilities:**
- Browse menu items
- View food categories
- Access registration page
- Access login page

**Access Level:** Read-only access to public pages

---

## 🛠️ TECHNOLOGIES USED

### **Backend Technologies:**
- **Python 3.13:** Core programming language
- **Flask 2.3.3:** Web application framework
- **Flask-SQLAlchemy 3.0.5:** ORM for database operations
- **Flask-Mail 0.9.1:** Email functionality for OTP
- **Werkzeug 2.3.7:** WSGI utility library

### **Database:**
- **MySQL:** Primary database (via XAMPP)
- **SQLite:** Alternative lightweight database
- **phpMyAdmin:** Database management interface

### **Frontend Technologies:**
- **HTML5:** Structure and content
- **CSS3:** Styling and layout
- **JavaScript:** Client-side interactivity
- **Responsive Design:** Mobile-friendly interface

### **Development Tools:**
- **Git:** Version control
- **GitHub:** Code repository and collaboration
- **VS Code:** Integrated development environment
- **XAMPP:** Local development server

### **Security:**
- **Password Hashing:** Werkzeug security
- **Session Management:** Flask sessions
- **OTP Verification:** Email-based authentication
- **SQL Injection Prevention:** SQLAlchemy ORM

---

## 💻 SOFTWARE & HARDWARE REQUIREMENTS

### **Software Requirements:**
- **Operating System:** Windows 10/11, macOS, or Linux
- **Python:** Version 3.8 or higher
- **XAMPP:** Version 8.0 or higher (for MySQL)
- **Web Browser:** Chrome, Firefox, Safari, or Edge (latest versions)
- **Text Editor/IDE:** VS Code, PyCharm, or similar
- **Git:** Version control system

### **Hardware Requirements:**
- **Processor:** Intel Core i3 or equivalent (minimum)
- **RAM:** 4GB (minimum), 8GB (recommended)
- **Storage:** 500MB free disk space
- **Internet Connection:** Required for package installation and email features

---

## 📊 DATABASE SCHEMA

### **Tables (5):**

#### **1. users**
Stores user account information
- `id` (Primary Key)
- `name` (VARCHAR)
- `email` (VARCHAR, Unique)
- `password` (VARCHAR, Hashed)
- `created_at` (TIMESTAMP)

#### **2. otps**
Manages email verification codes
- `id` (Primary Key)
- `email` (VARCHAR)
- `otp` (VARCHAR)
- `created_at` (TIMESTAMP)
- `expires_at` (TIMESTAMP)

#### **3. cart_items**
Stores shopping cart data
- `id` (Primary Key)
- `user_id` (Foreign Key → users.id)
- `item_name` (VARCHAR)
- `price` (DECIMAL)
- `quantity` (INTEGER)
- `image_url` (VARCHAR)
- `created_at` (TIMESTAMP)

#### **4. orders**
Maintains order information
- `id` (Primary Key)
- `user_id` (Foreign Key → users.id)
- `total_amount` (DECIMAL)
- `delivery_address` (TEXT)
- `phone` (VARCHAR)
- `status` (VARCHAR)
- `created_at` (TIMESTAMP)

#### **5. order_items**
Stores individual items in each order
- `id` (Primary Key)
- `order_id` (Foreign Key → orders.id)
- `item_name` (VARCHAR)
- `price` (DECIMAL)
- `quantity` (INTEGER)
- `created_at` (TIMESTAMP)

### **Relationships:**
- One-to-Many: users → cart_items
- One-to-Many: users → orders
- One-to-Many: orders → order_items

---

## 🎨 SYSTEM FEATURES

### **1. User Authentication**
- Secure registration with email verification
- OTP-based account activation
- Password hashing for security
- Session-based login system
- Logout functionality

### **2. Menu Management**
- Categorized food items:
  - Vegetarian Dishes
  - Street Chaat
  - Desserts & Ice Cream
  - Gym Food (High Protein, Detox Drinks, Shakes)
- High-quality food images
- Detailed item descriptions
- Price display

### **3. Shopping Cart**
- Add items to cart
- Update quantities
- Remove items
- Real-time price calculation
- Persistent cart (database-stored)

### **4. Order Processing**
- Checkout with delivery details
- Order confirmation
- Order history view
- Order details with itemized list
- Order status tracking
- Cancel pending orders

### **5. User Profile**
- View account information
- Update profile details
- Order history access
- Secure password management

---

## 📈 LINES OF CODE (LOC)

| Component | Files | Lines of Code |
|-----------|-------|---------------|
| Backend (Python) | 5 | ~800 LOC |
| Frontend (HTML) | 15 | ~2,500 LOC |
| CSS Styling | 2 | ~600 LOC |
| JavaScript | 2 | ~400 LOC |
| Database Scripts | 3 | ~300 LOC |
| Documentation | 15 | ~3,000 LOC |
| **Total** | **42** | **~7,600 LOC** |

---

## 🔒 SECURITY FEATURES

1. **Password Security:**
   - Werkzeug password hashing (PBKDF2)
   - No plain-text password storage

2. **Session Management:**
   - Secure Flask sessions
   - Session timeout
   - CSRF protection

3. **Email Verification:**
   - OTP-based account activation
   - Time-limited verification codes

4. **SQL Injection Prevention:**
   - SQLAlchemy ORM (parameterized queries)
   - Input validation

5. **Data Protection:**
   - Environment variables for sensitive data
   - .gitignore for secrets
   - Secure database connections

---

## 🚀 INSTALLATION & SETUP

### **Step 1: Clone Repository**
```bash
git clone https://github.com/Shivamkurunde/Shivamkurende_123_TYCSEA_ResturantManagementSystem.git
cd Shivamkurende_123_TYCSEA_ResturantManagementSystem
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Setup Database**
**Option A: MySQL (with XAMPP)**
```bash
# Start XAMPP (Apache + MySQL)
python init_mysql_db.py
```

**Option B: SQLite (No XAMPP needed)**
```bash
# Database file created automatically
```

### **Step 4: Configure Environment**
```bash
# Copy .env.example to .env
# Update database credentials if needed
```

### **Step 5: Run Application**
```bash
python app.py
```

### **Step 6: Access Application**
- **Application:** http://localhost:5000
- **phpMyAdmin:** http://localhost/phpmyadmin (if using MySQL)

---

## 📱 USAGE GUIDE

### **For Customers:**
1. Register account with email
2. Verify email with OTP
3. Login to system
4. Browse menu categories
5. Add items to cart
6. Proceed to checkout
7. Enter delivery details
8. Place order
9. View order history

### **For Administrators:**
1. Access phpMyAdmin
2. View database tables
3. Monitor orders
4. Analyze customer data
5. Run SQL queries
6. Export reports

---

## 📊 SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────┐
│         User Interface (Browser)        │
│     HTML5 | CSS3 | JavaScript           │
└─────────────────┬───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│      Flask Application (Backend)        │
│  ┌──────────────────────────────────┐   │
│  │  Routes & Controllers            │   │
│  │  - Authentication                │   │
│  │  - Menu Management               │   │
│  │  - Cart Operations               │   │
│  │  - Order Processing              │   │
│  └──────────────┬───────────────────┘   │
│                 │                        │
│  ┌──────────────▼───────────────────┐   │
│  │  Business Logic Layer            │   │
│  │  - User Management               │   │
│  │  - OTP Verification              │   │
│  │  - Order Validation              │   │
│  └──────────────┬───────────────────┘   │
│                 │                        │
│  ┌──────────────▼───────────────────┐   │
│  │  Data Access Layer (ORM)         │   │
│  │  - SQLAlchemy Models             │   │
│  │  - Database Queries              │   │
│  └──────────────┬───────────────────┘   │
└─────────────────┼───────────────────────┘
                  │
                  ↓
┌─────────────────────────────────────────┐
│      MySQL Database (XAMPP)             │
│  ┌──────────────────────────────────┐   │
│  │  Tables:                         │   │
│  │  - users                         │   │
│  │  - otps                          │   │
│  │  - cart_items                    │   │
│  │  - orders                        │   │
│  │  - order_items                   │   │
│  └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## 🎓 LEARNING OUTCOMES

### **Technical Skills Acquired:**
1. Full-stack web development with Python Flask
2. Database design and normalization
3. SQL query writing and optimization
4. User authentication and session management
5. RESTful API design principles
6. Frontend development (HTML/CSS/JavaScript)
7. Version control with Git/GitHub
8. Security best practices

### **Soft Skills Developed:**
1. Project planning and management
2. Problem-solving and debugging
3. Documentation writing
4. Time management
5. Self-learning and research

---

## 🐛 KNOWN ISSUES & LIMITATIONS

1. **Email Configuration:** Requires SendGrid API key for OTP functionality
2. **Payment Integration:** Not implemented (future enhancement)
3. **Real-time Updates:** No WebSocket support for live order tracking
4. **Mobile App:** Web-only, no native mobile application
5. **Multi-language:** English only interface

---

## 🔮 FUTURE ENHANCEMENTS

1. **Payment Gateway Integration:**
   - Razorpay/Stripe integration
   - Multiple payment options
   - Invoice generation

2. **Advanced Features:**
   - Real-time order tracking
   - Push notifications
   - Rating and review system
   - Loyalty points program

3. **Admin Panel:**
   - Dedicated admin dashboard
   - Menu item management
   - Order management interface
   - Analytics and reports

4. **Mobile Application:**
   - Native Android/iOS apps
   - Progressive Web App (PWA)

5. **AI Integration:**
   - Personalized recommendations
   - Chatbot support
   - Demand forecasting

---

## 📚 REFERENCES

1. Flask Documentation: https://flask.palletsprojects.com/
2. SQLAlchemy Documentation: https://docs.sqlalchemy.org/
3. MySQL Documentation: https://dev.mysql.com/doc/
4. Python Official Documentation: https://docs.python.org/
5. MDN Web Docs: https://developer.mozilla.org/
6. Stack Overflow: https://stackoverflow.com/
7. GitHub Guides: https://guides.github.com/

---

## 📞 CONTACT INFORMATION

**Student:** Shivam Kurunde  
**Email:** [Your Email]  
**GitHub:** https://github.com/Shivamkurunde  
**Repository:** https://github.com/Shivamkurunde/Shivamkurende_123_TYCSEA_ResturantManagementSystem

---

## 📄 PROJECT DELIVERABLES

✅ Complete source code  
✅ Database schema and scripts  
✅ User documentation  
✅ Technical documentation  
✅ Installation guide  
✅ Testing guide  
✅ Project synopsis  
✅ README file  
✅ requirements.txt  

---

## 🏆 CONCLUSION

The Restaurant Management System successfully demonstrates the application of modern web development technologies to solve real-world business problems. The project showcases proficiency in full-stack development, database design, and software engineering principles. The system provides a solid foundation for future enhancements and can be extended to support additional features as needed.

This project has been an excellent learning experience, covering various aspects of software development from requirements gathering to deployment. The skills acquired during this project are directly applicable to industry scenarios and provide a strong foundation for future software development endeavors.

---

**Date:** February 2026  
**Version:** 1.0  
**Status:** Completed ✅

---

## 📋 ACKNOWLEDGEMENT

I would like to express my sincere gratitude to:

- **[Guide Name]** - Project Guide, for valuable guidance and support
- **[HOD Name]** - Head of Department, for providing necessary resources
- **College Faculty** - For their continuous encouragement
- **Family & Friends** - For their unwavering support
- **Open Source Community** - For excellent documentation and resources

---

*This project is submitted in partial fulfillment of the requirements for the degree of Bachelor of Science in Computer Science.*

---

**© 2026 Shivam Kurunde. All Rights Reserved.**
