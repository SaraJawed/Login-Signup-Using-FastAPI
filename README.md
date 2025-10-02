**FastAPI User Auth Project
**
This project is a step-by-step implementation of User Authentication with FastAPI, following a Day-by-Day learning plan.

**Day 2 – REST Basics**

Implemented user signup endpoint → POST /auth/signup

Used Pydantic models for validation (UserCreate, UserOut)

Explored Swagger UI at /docs and Redoc at /redoc

**Day 3 – Database Intro**

Connected to SQLite using SQLAlchemy

Created User model in app/models/user.py

Persisted users in the database instead of in-memory dict

Signup endpoint now stores data in SQLite

**Day 4 – Authentication**

Implemented JWT login → POST /auth/login

Added JWT token generation with python-jose

Hashed passwords using passlib (bcrypt)

Protected route /users/me → only accessible with a valid token

**Day 5 – Project Structuring**

Refactored into:

routers/ → all route definitions

models/ → SQLAlchemy models

schemas/ → Pydantic schemas

services/ → authentication utilities

Implemented logout endpoint → POST /auth/logout

Added /users/ endpoint:

Requires admin privileges

Normal users → 403 Not enough permissions

Admins → can see full user list

**How to Run**
uvicorn app.main:app --reload


**Open browser:**

Swagger UI → http://127.0.0.1:8000/docs

Redoc → http://127.0.0.1:8000/redoc

Frontend → http://127.0.0.1:8000/

**Admin Access
**
To test /users/ list:

Create a user via /auth/signup

In the DB, set is_admin = true for that user

Login with that user → /users/ will now return all users
