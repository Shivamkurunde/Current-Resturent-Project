from app import app, db
from models import User, CartItem, Order, OrderItem, OTP

with app.app_context():
    print('Adding more sample data...\n')
    
    # Add more users
    users_data = [
        {'name': 'Neha Singh', 'email': 'neha@example.com', 'password': 'neha123'},
        {'name': 'Vikram Patel', 'email': 'vikram@example.com', 'password': 'vikram123'},
        {'name': 'Anjali Verma', 'email': 'anjali@example.com', 'password': 'anjali123'},
    ]
    
    for user_data in users_data:
        existing = User.query.filter_by(email=user_data['email']).first()
        if not existing:
            user = User(name=user_data['name'], email=user_data['email'], is_verified=True)
            user.set_password(user_data['password'])
            db.session.add(user)
            print(f"✓ Added user: {user_data['name']}")
    
    db.session.commit()
    
    # Add more cart items for different users
    print('\nAdding cart items...')
    cart_data = [
        (2, 'Veg Biryani', 150, 1, 'Veg'),
        (2, 'Raita', 30, 2, 'Veg'),
        (3, 'Protein Shake', 200, 1, 'Gym Food'),
        (3, 'Detox Juice', 80, 2, 'Gym Food'),
        (4, 'Samosa', 20, 3, 'Street Chaat'),
        (4, 'Chai', 10, 2, 'Street Chaat'),
        (5, 'Vanilla Ice Cream', 80, 1, 'Desserts'),
        (5, 'Rasmalai', 60, 2, 'Desserts'),
    ]
    
    for user_id, item_name, price, qty, category in cart_data:
        existing = CartItem.query.filter_by(user_id=user_id, item_name=item_name).first()
        if not existing:
            cart_item = CartItem(user_id=user_id, item_name=item_name, item_price=price, quantity=qty, category=category)
            db.session.add(cart_item)
            print(f'✓ Added to cart: {item_name} (User {user_id})')
    
    db.session.commit()
    
    # Add more orders
    print('\nAdding orders...')
    orders_data = [
        (4, 280, 'Delivered', '789 Park Avenue, Bangalore', '9876543213'),
        (5, 320, 'Confirmed', '321 Main Street, Hyderabad', '9876543214'),
        (1, 420, 'Pending', '654 Oak Road, Pune', '9876543215'),
        (4, 150, 'Delivered', '789 Park Avenue, Bangalore', '9876543213'),
    ]
    
    for user_id, amount, status, address, phone in orders_data:
        order = Order(user_id=user_id, total_amount=amount, status=status, delivery_address=address, phone_number=phone)
        db.session.add(order)
        db.session.flush()
        print(f'✓ Added order #{order.id}: {status} - Rs{amount}')
    
    db.session.commit()
    
    # Add order items for new orders
    print('\nAdding order items...')
    order_items_data = [
        (4, 'Veg Biryani', 150, 1, 'Veg'),
        (4, 'Raita', 30, 2, 'Veg'),
        (5, 'Protein Shake', 200, 1, 'Gym Food'),
        (5, 'Detox Juice', 80, 2, 'Gym Food'),
        (6, 'Samosa', 20, 3, 'Street Chaat'),
        (6, 'Chai', 10, 2, 'Street Chaat'),
        (7, 'Vanilla Ice Cream', 80, 1, 'Desserts'),
        (7, 'Rasmalai', 60, 2, 'Desserts'),
    ]
    
    for order_id, item_name, price, qty, category in order_items_data:
        order_item = OrderItem(order_id=order_id, item_name=item_name, item_price=price, quantity=qty, category=category)
        db.session.add(order_item)
        print(f'✓ Added item to order #{order_id}: {item_name}')
    
    db.session.commit()
    
    # Add OTP records
    print('\nAdding OTP records...')
    otp_data = [
        ('test1@example.com', '111111'),
        ('test2@example.com', '222222'),
        ('test3@example.com', '333333'),
    ]
    
    for email, code in otp_data:
        otp = OTP(email=email, otp_code=code, expiry_minutes=5)
        db.session.add(otp)
        print(f'✓ Added OTP for: {email}')
    
    db.session.commit()
    
    print('\n' + '='*50)
    print('✅ All sample data added successfully!')
    print('='*50)
    
    # Show summary
    print('\n📊 Database Summary:')
    print(f'  Users: {User.query.count()}')
    print(f'  Cart Items: {CartItem.query.count()}')
    print(f'  Orders: {Order.query.count()}')
    print(f'  Order Items: {OrderItem.query.count()}')
    print(f'  OTPs: {OTP.query.count()}')
    
    print('\n🔐 New Login Credentials:')
    print('  neha@example.com / neha123')
    print('  vikram@example.com / vikram123')
    print('  anjali@example.com / anjali123')
