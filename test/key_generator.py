import secrets

secret_key = secrets.token_hex(32)
print(secret_key)

from import_bridge import bcrypt
print(bcrypt.generate_password_hash("testpasswordcriptata").decode("utf-8"))