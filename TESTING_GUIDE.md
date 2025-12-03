# 🧪 Testing Guide - Before Presentation

## Pre-Presentation Testing Checklist

Test everything before showing to your teacher to avoid surprises!

---

## 🔧 Environment Setup Test

### Test 1: XAMPP Services
```
✅ Open XAMPP Control Panel
✅ Apache shows GREEN/Running
✅ MySQL shows GREEN/Running
✅ No error messages
```

**If Failed:**
- Restart XAMPP
- Run as Administrator
- Check port conflicts

---

### Test 2: phpMyAdmin Access
```
✅ Open: http://localhost/phpmyadmin
✅ Page loads without errors
✅ Can see left sidebar with databases
✅ No "Cannot connect" errors
```

**If Failed:**
- Check Apache is running
- Check MySQL is running
- Clear browser cache

---

### Test 3: Database Exists
```
✅ In phpMyAdmin, click "restaurant_db"
✅ See 5 tables: users, otps, cart_items, orders, order_items
✅ Each table has correct structure
```

**If Failed:**
- Run: `python init_mysql_db.py`
- Check for error messages
- Verify MySQL is running

---

## 🌐 Application Tests

### Test 4: App Starts
```cmd
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

**Check:**
```
✅ No error messages
✅ Shows "Running on http://127.0.0.1:5000"
✅ No database connection errors
```

**If Failed:**
- Check requirements installed: `pip install -r requirements.txt`
- Check .env file exists
- Check DATABASE_URL in .env

---

### Test 5: Home Page Loads
```
✅ Open: http://localhost:5000
✅ Home page displays
✅ Navigation menu visible
✅ No 404 or 500 errors
```

---

### Test 6: Registration Flow

**Step 1: Access Registration**
```
✅ Click "Register" or go to /register
✅ Registration form displays
✅ All fields visible (Name, Email, Password, Confirm Password)
```

**Step 2: Submit Registration**
```
Test Data:
Name: Test User
Email: test@example.com
Password: test123
Confirm Password: test123

✅ Form submits successfully
✅ Redirects to OTP verification page
✅ Shows success message
```

**Step 3: Check Database**
```
✅ Open phpMyAdmin
✅ Go to restaurant_db → otps table
✅ See new OTP entry with email: test@example.com
✅ Note the OTP code (6 digits)
```

**Step 4: Verify OTP**
```
✅ Enter the OTP code from database
✅ Click Verify
✅ Redirects to login page
✅ Shows "Registration successful" message
```

**Step 5: Verify User Created**
```
✅ In phpMyAdmin → users table
✅ See new user: test@example.com
✅ is_verified = 1
✅ password_hash is encrypted (not plain text)
```

---

### Test 7: Login Flow

**Step 1: Access Login**
```
✅ Go to /auth/login
✅ Login form displays
✅ Email and Password fields visible
```

**Step 2: Login**
```
Email: test@example.com
Password: test123

✅ Form submits
✅ Redirects to home page
✅ Shows welcome message with user name
✅ Navigation shows user is logged in
```

**Step 3: Session Check**
```
✅ User stays logged in on page refresh
✅ Can access protected pages (cart, orders)
```

---

### Test 8: Shopping Cart

**Step 1: Add Items**
```
✅ Browse to any menu page (Desserts, Veg, etc.)
✅ Click "Add to Cart" on an item
✅ Shows success message
✅ Can add multiple items
```

**Step 2: View Cart**
```
✅ Go to /cart
✅ Cart page displays
✅ Shows all added items
✅ Shows correct prices
✅ Shows correct quantities
✅ Shows total amount
```

**Step 3: Check Database**
```
✅ phpMyAdmin → cart_items table
✅ See items with correct user_id
✅ Prices and quantities match
```

**Step 4: Update Quantity**
```
✅ Change quantity in cart
✅ Click update
✅ Quantity updates
✅ Total recalculates
✅ Database updates
```

**Step 5: Remove Item**
```
✅ Click remove on an item
✅ Item disappears from cart
✅ Total recalculates
✅ Database entry deleted
```

---

### Test 9: Order Placement

**Step 1: Checkout**
```
✅ Cart has items
✅ Click "Checkout"
✅ Checkout page displays
✅ Shows order summary
✅ Shows total amount
```

**Step 2: Fill Details**
```
Phone: 9876543210
Address: 123 Test Street, Mumbai

✅ Form accepts input
✅ Validation works (required fields)
```

**Step 3: Place Order**
```
✅ Click "Place Order"
✅ Order submits successfully
✅ Redirects to order details page
✅ Shows order ID
✅ Shows success message
```

**Step 4: Check Database**
```
✅ phpMyAdmin → orders table
✅ New order entry exists
✅ Correct user_id
✅ Correct total_amount
✅ Status = 'Pending'
✅ Phone and address saved

✅ phpMyAdmin → order_items table
✅ Items from cart copied here
✅ Correct order_id
✅ All items present

✅ phpMyAdmin → cart_items table
✅ Cart is now empty for this user
```

---

### Test 10: Order History

**Step 1: View Orders**
```
✅ Go to /my-orders
✅ Order list displays
✅ Shows recent order
✅ Shows order details (ID, date, amount, status)
```

**Step 2: View Order Details**
```
✅ Click on an order
✅ Order details page displays
✅ Shows all items in order
✅ Shows delivery address
✅ Shows phone number
✅ Shows total amount
✅ Shows status
```

**Step 3: Cancel Order**
```
✅ For pending order, "Cancel" button visible
✅ Click cancel
✅ Confirmation prompt appears
✅ Confirm cancellation
✅ Order status changes to "Cancelled"
✅ Database updates (status = 'Cancelled')
```

---

### Test 11: Logout

```
✅ Click "Logout"
✅ Redirects to home page
✅ Shows logout success message
✅ User no longer logged in
✅ Cannot access protected pages
✅ Redirects to login if trying to access cart/orders
```

---

## 📊 SQL Queries Test

### Test 12: Run Sample Queries

Open phpMyAdmin → SQL tab, test these:

**Query 1: All Users**
```sql
SELECT * FROM users;
```
```
✅ Query runs without error
✅ Shows user data
```

**Query 2: Orders with User Details**
```sql
SELECT o.id, u.name, o.total_amount, o.status 
FROM orders o 
JOIN users u ON o.user_id = u.id;
```
```
✅ Query runs
✅ Shows joined data
✅ User names appear with orders
```

**Query 3: Total Revenue**
```sql
SELECT SUM(total_amount) as total_revenue FROM orders;
```
```
✅ Query runs
✅ Shows numeric result
```

**Query 4: Order Items Details**
```sql
SELECT * FROM order_items;
```
```
✅ Query runs
✅ Shows order items
```

---

## 🎯 Sample Data Test

### Test 13: Add Sample Data

```cmd
python add_sample_data.py
```

**Choose Option 1: Add sample data**

```
✅ Script runs without errors
✅ Creates 3 sample users
✅ Adds cart items
✅ Creates 3 sample orders
✅ Shows summary at end
```

**Verify in phpMyAdmin:**
```
✅ users table has 3+ users
✅ cart_items table has items
✅ orders table has 3+ orders
✅ order_items table has items
```

**Test Login with Sample Users:**
```
Email: rahul@example.com
Password: rahul123

✅ Can login
✅ Can see cart items (if any)
✅ Can see order history
```

---

## 🔄 Full Integration Test

### Test 14: Complete User Journey

**Scenario: New user orders food**

1. **Register** → test2@example.com
2. **Verify OTP** → Check database, enter code
3. **Login** → Use new credentials
4. **Browse Menu** → Go to Desserts page
5. **Add to Cart** → Add 2 items
6. **View Cart** → Check items and total
7. **Checkout** → Fill delivery details
8. **Place Order** → Submit order
9. **View Order** → Check order details
10. **Check Database** → Verify all data saved

```
✅ All steps complete without errors
✅ Data appears correctly in database
✅ User experience is smooth
```

---

## 📱 Browser Compatibility Test

### Test 15: Multiple Browsers

Test in:
- ✅ Google Chrome
- ✅ Mozilla Firefox
- ✅ Microsoft Edge

**Check:**
```
✅ Pages load correctly
✅ Forms work
✅ Styling looks good
✅ No console errors
```

---

## 🚨 Error Handling Test

### Test 16: Invalid Inputs

**Registration:**
```
✅ Empty fields → Shows error
✅ Invalid email → Shows error
✅ Password mismatch → Shows error
✅ Existing email → Shows error
```

**Login:**
```
✅ Wrong password → Shows error
✅ Non-existent email → Shows error
✅ Empty fields → Shows error
```

**Cart:**
```
✅ Access without login → Redirects to login
✅ Invalid quantity → Handles gracefully
```

**Checkout:**
```
✅ Empty cart → Shows error
✅ Missing phone → Shows error
✅ Missing address → Shows error
```

---

## 📋 Pre-Presentation Final Check

### 30 Minutes Before Presentation:

```
□ Restart computer (fresh start)
□ Open XAMPP Control Panel
□ Start Apache (wait for GREEN)
□ Start MySQL (wait for GREEN)
□ Open phpMyAdmin (verify it loads)
□ Check restaurant_db exists
□ Check all 5 tables exist
□ Run: python app.py
□ Open: http://localhost:5000
□ Test one complete registration
□ Test one complete order
□ Verify data in phpMyAdmin
□ Test 2-3 SQL queries
□ Close unnecessary programs
□ Charge laptop (if presenting on laptop)
□ Have backup: USB with project files
```

---

## 🎬 Demo Data Preparation

### Option A: Use Sample Data
```cmd
python add_sample_data.py
```
- Quick setup
- Multiple users and orders
- Good for showing variety

### Option B: Create Live During Demo
- More impressive
- Shows real-time database updates
- Teacher can see actual process

### Option C: Mix Both
- Have sample data as backup
- Create one new user live
- Show both old and new data

---

## 📊 Performance Check

### Test 17: Speed Test

```
✅ Pages load in < 2 seconds
✅ Database queries are fast
✅ No lag when adding to cart
✅ Order placement is quick
✅ phpMyAdmin responds quickly
```

---

## 🔐 Security Check

### Test 18: Security Features

```
✅ Passwords are hashed (not plain text in database)
✅ Cannot access cart without login
✅ Cannot access orders without login
✅ Cannot view other users' orders
✅ Session expires on logout
```

---

## ✅ Final Verification

### Everything Working Checklist:

**Infrastructure:**
- [x] XAMPP installed
- [x] Apache running
- [x] MySQL running
- [x] phpMyAdmin accessible

**Database:**
- [x] restaurant_db exists
- [x] All 5 tables created
- [x] Sample data loaded
- [x] SQL queries work

**Application:**
- [x] App starts without errors
- [x] Home page loads
- [x] Registration works
- [x] OTP verification works
- [x] Login works
- [x] Cart works
- [x] Order placement works
- [x] Order history works
- [x] Logout works

**Presentation Ready:**
- [x] Know how to start services
- [x] Know how to run app
- [x] Know how to access phpMyAdmin
- [x] Have SQL queries ready
- [x] Confident with demo flow

---

## 🎯 If Something Breaks During Demo

### Emergency Fixes:

**App crashes:**
```cmd
Ctrl+C (stop app)
python app.py (restart)
```

**Database connection lost:**
```
1. Check MySQL is running (XAMPP)
2. Restart MySQL
3. Restart app
```

**phpMyAdmin won't open:**
```
1. Check Apache is running
2. Restart Apache
3. Clear browser cache
```

**Can't login:**
```
Use sample data credentials:
Email: rahul@example.com
Password: rahul123
```

---

## 📝 Testing Log Template

Use this to track your testing:

```
Date: ___________
Time: ___________

[ ] XAMPP Services Running
[ ] phpMyAdmin Accessible
[ ] Database Created
[ ] App Starts
[ ] Registration Works
[ ] Login Works
[ ] Cart Works
[ ] Order Works
[ ] SQL Queries Work
[ ] Sample Data Loaded

Issues Found:
_______________________________
_______________________________

Issues Resolved:
_______________________________
_______________________________

Ready for Presentation: YES / NO
```

---

**Test everything at least once before the presentation!** 🚀

Good luck! 🎉
