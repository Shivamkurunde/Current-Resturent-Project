"""
Add Sample Data to Database
Run this to quickly populate database with test data for demonstration
"""
from app import app, db
from models import User, CartItem, Order, OrderItem
from datetime import datetime, timedelta

def add_sample_data():
    """Add sample users, cart items, and orders"""
    
    with app.app_context():
        print("=" * 60)
        print("Adding Sample Data to Database")
        print("=" * 60)
        
        # Check if data already exists
        existing_users = User.query.count()
        if existing_users > 0:
            print(f"\n⚠️  Database already has {existing_users} users.")
            response = input("Do you want to add more sample data? (yes/no): ")
            if response.lower() != 'yes':
                print("Cancelled. No data added.")
                return
        
        print("\n📝 Creating sample users...")
        
        # Create sample users
        users_data = [
            {"name": "Rahul Kumar", "email": "rahul@example.com", "password": "rahul123"},
            {"name": "Priya Sharma", "email": "priya@example.com", "password": "priya123"},
            {"name": "Amit Patel", "email": "amit@example.com", "password": "amit123"},
        ]
        
        users = []
        for user_data in users_data:
            # Check if user already exists
            existing = User.query.filter_by(email=user_data['email']).first()
            if existing:
                print(f"   ⚠️  User {user_data['email']} already exists, skipping...")
                users.append(existing)
                continue
            
            user = User(
                name=user_data['name'],
                email=user_data['email'],
                is_verified=True
            )
            user.set_password(user_data['password'])
            db.session.add(user)
            users.append(user)
            print(f"   ✓ Created user: {user_data['name']} ({user_data['email']})")
        
        db.session.commit()
        print(f"\n✅ {len(users)} users ready!")
        
        # Add cart items for first user
        print("\n🛒 Adding cart items for Rahul...")
        cart_items_data = [
            {"item_name": "Gulab Jamun", "item_price": 50, "quantity": 2, "category": "Desserts"},
            {"item_name": "Paneer Tikka", "item_price": 120, "quantity": 1, "category": "Veg"},
            {"item_name": "Pav Bhaji", "item_price": 80, "quantity": 1, "category": "Street Chaat"},
        ]
        
        for item_data in cart_items_data:
            cart_item = CartItem(
                user_id=users[0].id,
                item_name=item_data['item_name'],
                item_price=item_data['item_price'],
                quantity=item_data['quantity'],
                category=item_data['category']
            )
            db.session.add(cart_item)
            print(f"   ✓ Added to cart: {item_data['item_name']} x{item_data['quantity']}")
        
        db.session.commit()
        print("✅ Cart items added!")
        
        # Create sample orders
        print("\n📦 Creating sample orders...")
        
        # Order 1 - Delivered
        order1 = Order(
            user_id=users[1].id,  # Priya
            total_amount=350,
            status='Delivered',
            delivery_address='123 MG Road, Mumbai, Maharashtra - 400001',
            phone_number='9876543210',
            created_at=datetime.utcnow() - timedelta(days=5)
        )
        db.session.add(order1)
        db.session.flush()
        
        order1_items = [
            {"item_name": "Chocolate Ice Cream", "item_price": 100, "quantity": 2, "category": "Desserts"},
            {"item_name": "Veg Biryani", "item_price": 150, "quantity": 1, "category": "Veg"},
        ]
        
        for item_data in order1_items:
            order_item = OrderItem(
                order_id=order1.id,
                item_name=item_data['item_name'],
                item_price=item_data['item_price'],
                quantity=item_data['quantity'],
                category=item_data['category']
            )
            db.session.add(order_item)
        
        print(f"   ✓ Order #{order1.id} - Priya Sharma - ₹350 (Delivered)")
        
        # Order 2 - Pending
        order2 = Order(
            user_id=users[2].id,  # Amit
            total_amount=280,
            status='Pending',
            delivery_address='456 Park Street, Pune, Maharashtra - 411001',
            phone_number='9876543211',
            created_at=datetime.utcnow() - timedelta(hours=2)
        )
        db.session.add(order2)
        db.session.flush()
        
        order2_items = [
            {"item_name": "Pani Puri", "item_price": 40, "quantity": 2, "category": "Street Chaat"},
            {"item_name": "Protein Shake", "item_price": 200, "quantity": 1, "category": "Gym Food"},
        ]
        
        for item_data in order2_items:
            order_item = OrderItem(
                order_id=order2.id,
                item_name=item_data['item_name'],
                item_price=item_data['item_price'],
                quantity=item_data['quantity'],
                category=item_data['category']
            )
            db.session.add(order_item)
        
        print(f"   ✓ Order #{order2.id} - Amit Patel - ₹280 (Pending)")
        
        # Order 3 - Confirmed
        order3 = Order(
            user_id=users[1].id,  # Priya (second order)
            total_amount=450,
            status='Confirmed',
            delivery_address='123 MG Road, Mumbai, Maharashtra - 400001',
            phone_number='9876543210',
            created_at=datetime.utcnow() - timedelta(hours=6)
        )
        db.session.add(order3)
        db.session.flush()
        
        order3_items = [
            {"item_name": "Paneer Butter Masala", "item_price": 180, "quantity": 1, "category": "Veg"},
            {"item_name": "Dal Makhani", "item_price": 150, "quantity": 1, "category": "Veg"},
            {"item_name": "Gulab Jamun", "item_price": 60, "quantity": 2, "category": "Desserts"},
        ]
        
        for item_data in order3_items:
            order_item = OrderItem(
                order_id=order3.id,
                item_name=item_data['item_name'],
                item_price=item_data['item_price'],
                quantity=item_data['quantity'],
                category=item_data['category']
            )
            db.session.add(order_item)
        
        print(f"   ✓ Order #{order3.id} - Priya Sharma - ₹450 (Confirmed)")
        
        db.session.commit()
        print("✅ Sample orders created!")
        
        # Summary
        print("\n" + "=" * 60)
        print("✅ Sample Data Added Successfully!")
        print("=" * 60)
        print("\n📊 Summary:")
        print(f"   • Users: {User.query.count()}")
        print(f"   • Cart Items: {CartItem.query.count()}")
        print(f"   • Orders: {Order.query.count()}")
        print(f"   • Order Items: {OrderItem.query.count()}")
        
        print("\n🔐 Login Credentials:")
        print("   Email: rahul@example.com | Password: rahul123")
        print("   Email: priya@example.com | Password: priya123")
        print("   Email: amit@example.com  | Password: amit123")
        
        print("\n🌐 Next Steps:")
        print("   1. Run your app: python app.py")
        print("   2. Login with any of the above credentials")
        print("   3. View data in phpMyAdmin: http://localhost/phpmyadmin")
        print("   4. Check 'restaurant_db' database")
        
        print("\n" + "=" * 60)

def clear_all_data():
    """Clear all data from database (use with caution!)"""
    with app.app_context():
        print("\n⚠️  WARNING: This will delete ALL data from database!")
        response = input("Are you sure? Type 'DELETE ALL' to confirm: ")
        
        if response == 'DELETE ALL':
            print("\n🗑️  Deleting all data...")
            
            OrderItem.query.delete()
            print("   ✓ Deleted order items")
            
            Order.query.delete()
            print("   ✓ Deleted orders")
            
            CartItem.query.delete()
            print("   ✓ Deleted cart items")
            
            User.query.delete()
            print("   ✓ Deleted users")
            
            db.session.commit()
            print("\n✅ All data deleted!")
        else:
            print("Cancelled. No data deleted.")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Sample Data Management")
    print("=" * 60)
    print("\nOptions:")
    print("1. Add sample data")
    print("2. Clear all data (dangerous!)")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1/2/3): ")
    
    if choice == '1':
        add_sample_data()
    elif choice == '2':
        clear_all_data()
    else:
        print("Exiting...")
