"""
Database initialization script for MySQL
Run this after installing XAMPP and starting MySQL service
"""
import pymysql
from app import app, db

def create_database():
    """Create the database if it doesn't exist"""
    try:
        # Connect to MySQL server (without database)
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Default XAMPP MySQL password is empty
            charset='utf8mb4'
        )
        
        cursor = connection.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        print("✓ Database 'restaurant_db' created successfully!")
        
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"✗ Error creating database: {e}")
        return False
    
    return True

def create_tables():
    """Create all tables"""
    try:
        with app.app_context():
            db.create_all()
            print("✓ All tables created successfully!")
            print("\nTables created:")
            print("  - users (for user accounts)")
            print("  - otps (for email verification)")
            print("  - cart_items (for shopping cart)")
            print("  - orders (for order details)")
            print("  - order_items (for items in each order)")
            return True
    except Exception as e:
        print(f"✗ Error creating tables: {e}")
        return False

def main():
    print("=" * 60)
    print("MySQL Database Initialization for Restaurant Project")
    print("=" * 60)
    print("\nMake sure XAMPP MySQL service is running!")
    print("\nStep 1: Creating database...")
    
    if create_database():
        print("\nStep 2: Creating tables...")
        if create_tables():
            print("\n" + "=" * 60)
            print("✓ Database setup completed successfully!")
            print("=" * 60)
            print("\nYou can now:")
            print("1. Run the Flask app: python app.py")
            print("2. View database in phpMyAdmin: http://localhost/phpmyadmin")
            print("3. Database name: restaurant_db")
            print("\nAll tables are ready for storing:")
            print("  • User registrations and login data")
            print("  • Shopping cart items")
            print("  • Order details and history")
        else:
            print("\n✗ Failed to create tables!")
    else:
        print("\n✗ Failed to create database!")
        print("\nTroubleshooting:")
        print("1. Make sure XAMPP is installed")
        print("2. Start MySQL service in XAMPP Control Panel")
        print("3. Check if MySQL is running on port 3306")

if __name__ == '__main__':
    main()
