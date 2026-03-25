import hashlib
import os
import hmac

def make_password(password):
    salt = os.urandom(16)
    pwd_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return salt, pwd_hash


def check_password(saved_salt, saved_hash, user_input):
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        user_input.encode(),
        saved_salt,
        100000
    )
    return hmac.compare_digest(saved_hash, new_hash)


# -------- main --------
pwd = input("Set your password: ")

salt, pwd_hash = make_password(pwd)
print("Password saved.\n")

login_pwd = input("Enter password to login: ")

if check_password(salt, pwd_hash, login_pwd):
    print("Login successful")
else:
    print("Wrong password")