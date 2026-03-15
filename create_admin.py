from app import app, db
from models import User

with app.app_context():
    existing = User.query.filter_by(email='admin').first()
    if existing:
        existing.set_password('admin123')
        existing.is_verified = True
        db.session.commit()
        print("Admin password updated: admin / admin123")
    else:
        user = User(name='Admin', email='admin', is_verified=True)
        user.set_password('admin123')
        db.session.add(user)
        db.session.commit()
        print("Admin created: email=admin | password=admin123")
