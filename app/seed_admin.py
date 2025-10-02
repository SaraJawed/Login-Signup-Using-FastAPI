from sqlalchemy.orm import Session
from app.database import engine
from app.models.user import User
from app.services.auth_service import get_password_hash

# ✅ Create a DB session
session = Session(bind=engine)

# Admin credentials
admin_email = "admin@example.com"
admin_password = "admin123"

# Check if admin already exists
admin_user = session.query(User).filter(User.email == admin_email).first()

if admin_user:
    print("ℹ️ Admin already exists.")
else:
    # Hash the password before saving
    hashed_pw = get_password_hash(admin_password)

    new_admin = User(
        email=admin_email,
        hashed_password=hashed_pw,
        full_name="Super Admin",
        is_active=True,
        is_admin=True
    )

    session.add(new_admin)
    session.commit()
    print(f"✅ Admin user created: {admin_email} / {admin_password}")

session.close()
