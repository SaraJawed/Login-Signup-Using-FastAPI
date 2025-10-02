from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.database import Base, engine, SessionLocal
from app.routers import auth, user
from app.models.user import User
from app.services.auth_service import get_password_hash

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Serve index.html
@app.get("/")
def root():
    return FileResponse(Path("app/static/index.html"))

# ---------------------------------------------------
# Create default admin (only if no admin exists)
# ---------------------------------------------------
def create_default_admin():
    db = SessionLocal()
    try:
        admin_exists = db.query(User).filter(User.is_admin == True).first()
        if not admin_exists:
            admin = User(
                email="admin@example.com",
                full_name="Super Admin",
                hashed_password=get_password_hash("admin123"),
                is_admin=True
            )
            db.add(admin)
            db.commit()
            print("Default admin created: email=admin@example.com / password=admin123")
        else:
            print(" Admin already exists, skipping seeding.")
    finally:
        db.close()

# Call function at startup
create_default_admin()
