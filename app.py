import os
from flask import Flask, render_template, url_for, request, redirect, flash, session, jsonify
from dotenv import load_dotenv
from models import db, User, OTP, CartItem, Order, OrderItem
from sendgrid_otp_service import SendGridOTPService
from functools import wraps

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# MySQL Database Configuration
# Change these values after installing XAMPP
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://root:@localhost/restaurant_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
otp_service = SendGridOTPService()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page.', 'error')
            return redirect(url_for('auth_login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/desserts')
def desserts():
    return render_template('Desserts.html')

@app.route('/ice-cream')
def ice_cream():
    return render_template('ice-cream.html')

@app.route('/Dessert-Icream')
def dessert_icecream():
    return render_template('Dessert-Icream.html')

@app.route('/gym-food')
def gym_food():
    return render_template('gym-food.html')

@app.route('/gym-protein')
def gym_protein():
    return render_template('gym-protein.html')

@app.route('/gym-detox')
def gym_detox():
    return render_template('gym-detox.html')

@app.route('/gym-shakes')
def gym_shakes():
    return render_template('gym-shakes.html')

@app.route('/street-chaat')
def street_chaat():
    return render_template('street-chaat.html')

@app.route('/veg')
def veg():
    return render_template('veg.html')

@app.route('/cart')
@login_required
def cart():
    user_id = session.get('user_id')
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    
    total = sum(item.get_total() for item in cart_items)
    
    return render_template('cart.html', cart_items=cart_items, total=total)

# Authentication Routes
@app.route('/register', methods=['GET', 'POST'])
def auth_register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not all([name, email, password, confirm_password]):
            flash('All fields are required.', 'error')
            return render_template('auth/register.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('auth/register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return render_template('auth/register.html')
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please login instead.', 'error')
            return render_template('auth/register.html')
        
        # Store user data in session temporarily
        session['temp_user'] = {
            'name': name,
            'email': email,
            'password': password
        }
        
        # Send OTP
        if otp_service.send_registration_otp(email):
            flash('OTP sent to your email! Please check your inbox.', 'success')
            return redirect(url_for('verify_otp', email=email))
        else:
            flash('Failed to send OTP. Please try again.', 'error')
            return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@app.route('/verify-otp')
def verify_otp():
    email = request.args.get('email')
    if not email or 'temp_user' not in session:
        flash('Invalid access. Please register again.', 'error')
        return redirect(url_for('auth_register'))
    
    return render_template('auth/verify_otp.html', email=email)

@app.route('/verify-otp', methods=['POST'])
def verify_otp_post():
    if 'temp_user' not in session:
        flash('Session expired. Please register again.', 'error')
        return redirect(url_for('auth_register'))
    
    otp_code = request.form.get('otp')
    temp_user = session['temp_user']
    email = temp_user['email']
    
    if not otp_code or len(otp_code) != 6:
        flash('Please enter a valid 6-digit OTP.', 'error')
        return render_template('auth/verify_otp.html', email=email)
    
    # Verify OTP
    if otp_service.verify_otp(email, otp_code):
        # Create user account
        try:
            new_user = User(
                name=temp_user['name'],
                email=temp_user['email'],
                is_verified=True
            )
            new_user.set_password(temp_user['password'])
            
            db.session.add(new_user)
            db.session.commit()
            
            # Clear temporary session data
            session.pop('temp_user', None)
            
            flash('Registration successful! Please login with your credentials.', 'success')
            return redirect(url_for('auth_login'))
            
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            return render_template('auth/verify_otp.html', email=email)
    else:
        flash('Invalid or expired OTP. Please try again.', 'error')
        return render_template('auth/verify_otp.html', email=email)

@app.route('/resend-otp', methods=['POST'])
def resend_otp():
    email = request.form.get('email')
    if not email:
        flash('Invalid request.', 'error')
        return redirect(url_for('auth_register'))
    
    if otp_service.send_registration_otp(email):
        flash('New OTP sent to your email!', 'success')
    else:
        flash('Failed to send OTP. Please try again.', 'error')
    
    return redirect(url_for('verify_otp', email=email))

# Update old login route to redirect to new auth login
@app.route('/login')
def login():
    return redirect(url_for('auth_login'))

@app.route('/auth/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('remember')
        
        if not email or not password:
            flash('Please enter both email and password.', 'error')
            return render_template('auth/login.html')
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            if not user.is_verified:
                flash('Please verify your email first.', 'error')
                return render_template('auth/login.html')
            
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_email'] = user.email
            session.permanent = bool(remember)
            
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')
            return render_template('auth/login.html')
    
    return render_template('auth/login.html')

@app.route('/logout')
def auth_logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('home'))

# Cart Management Routes
@app.route('/add-to-cart', methods=['POST'])
@login_required
def add_to_cart():
    user_id = session.get('user_id')
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price'))
    quantity = int(request.form.get('quantity', 1))
    category = request.form.get('category', '')
    
    # Check if item already exists in cart
    existing_item = CartItem.query.filter_by(user_id=user_id, item_name=item_name).first()
    
    if existing_item:
        existing_item.quantity += quantity
    else:
        new_item = CartItem(
            user_id=user_id,
            item_name=item_name,
            item_price=item_price,
            quantity=quantity,
            category=category
        )
        db.session.add(new_item)
    
    db.session.commit()
    flash(f'{item_name} added to cart!', 'success')
    return redirect(request.referrer or url_for('home'))

@app.route('/update-cart/<int:item_id>', methods=['POST'])
@login_required
def update_cart(item_id):
    user_id = session.get('user_id')
    cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first()
    
    if cart_item:
        quantity = int(request.form.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            db.session.commit()
            flash('Cart updated!', 'success')
        else:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Item removed from cart!', 'success')
    
    return redirect(url_for('cart'))

@app.route('/remove-from-cart/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    user_id = session.get('user_id')
    cart_item = CartItem.query.filter_by(id=item_id, user_id=user_id).first()
    
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed from cart!', 'success')
    
    return redirect(url_for('cart'))

@app.route('/clear-cart', methods=['POST'])
@login_required
def clear_cart():
    user_id = session.get('user_id')
    CartItem.query.filter_by(user_id=user_id).delete()
    db.session.commit()
    flash('Cart cleared!', 'success')
    return redirect(url_for('cart'))

# Order Management Routes
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    user_id = session.get('user_id')
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    
    if not cart_items:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('cart'))
    
    if request.method == 'POST':
        delivery_address = request.form.get('delivery_address')
        phone_number = request.form.get('phone_number')
        
        if not delivery_address or not phone_number:
            flash('Please provide delivery address and phone number.', 'error')
            return render_template('checkout.html', cart_items=cart_items)
        
        # Calculate total
        total_amount = sum(item.get_total() for item in cart_items)
        
        # Create order
        new_order = Order(
            user_id=user_id,
            total_amount=total_amount,
            delivery_address=delivery_address,
            phone_number=phone_number,
            status='Pending'
        )
        db.session.add(new_order)
        db.session.flush()  # Get order ID
        
        # Create order items
        for cart_item in cart_items:
            order_item = OrderItem(
                order_id=new_order.id,
                item_name=cart_item.item_name,
                item_price=cart_item.item_price,
                quantity=cart_item.quantity,
                category=cart_item.category
            )
            db.session.add(order_item)
        
        # Clear cart
        CartItem.query.filter_by(user_id=user_id).delete()
        
        db.session.commit()
        
        flash(f'Order placed successfully! Order ID: {new_order.id}', 'success')
        return redirect(url_for('order_details', order_id=new_order.id))
    
    total = sum(item.get_total() for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/my-orders')
@login_required
def my_orders():
    user_id = session.get('user_id')
    orders = Order.query.filter_by(user_id=user_id).order_by(Order.created_at.desc()).all()
    return render_template('my_orders.html', orders=orders)

@app.route('/order/<int:order_id>')
@login_required
def order_details(order_id):
    user_id = session.get('user_id')
    order = Order.query.filter_by(id=order_id, user_id=user_id).first()
    
    if not order:
        flash('Order not found!', 'error')
        return redirect(url_for('my_orders'))
    
    return render_template('order_details.html', order=order)

@app.route('/cancel-order/<int:order_id>', methods=['POST'])
@login_required
def cancel_order(order_id):
    user_id = session.get('user_id')
    order = Order.query.filter_by(id=order_id, user_id=user_id).first()
    
    if order and order.status == 'Pending':
        order.status = 'Cancelled'
        db.session.commit()
        flash('Order cancelled successfully!', 'success')
    else:
        flash('Cannot cancel this order!', 'error')
    
    return redirect(url_for('my_orders'))

if __name__ == '__main__':
    app.run(debug=True)
