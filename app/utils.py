# from passlib.context import CryptContext
#
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
#
#
# def hashed_password(password: str):
#     return pwd_context.hash(password)
#
#
# def verify(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

import bcrypt


# Hash a password using bcrypt
def hashed_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hashed = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return password_hashed


# Check if the provided password matches the stored password (hashed)
def verify(plain_password, hashed_password):
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password_bytes)
