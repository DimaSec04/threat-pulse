import hashlib
import re
from database import (
    add_user,
    get_user,
    get_reset_code,
    update_password,
    mark_code_used
)
from database import get_connection
from database import hash_password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_password(password):

    if len(password) < 12:
        return "Password must be at least 12 characters"

    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter"

    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter"

    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number"

    if not re.search(r'[@$!%*?&#+_=.-]', password):
        return "Password must contain at least one special character"

    return True

def register(username, email, password):

    validation = is_valid_password(password)

    if validation != True:
        return validation

    if get_user(username):
        return "Username already exists"

    hashed = hash_password(password)

    add_user(username, email, hashed)

    return "User registered successfully"

def login(email, password):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM users
        WHERE email = ?
        """, (email,))

        user = cursor.fetchone()

    if not user:
        return "User not found"

    hashed = hash_password(password)

    if user[3] == hashed:

        return {
            "message": "Login successful",
            "username": user[1]
        }

    return "Wrong password"

def reset_password(code, new_password):

    reset_data = get_reset_code(code)

    if not reset_data:
        return "Invalid code"

    validation = is_valid_password(new_password)

    if validation != True:
        return validation

    user_id = reset_data[1]

    hashed = hash_password(new_password)

    update_password(user_id, hashed)

    mark_code_used(code)

    return "Password updated successfully"