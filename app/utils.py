from passlib.hash import pbkdf2_sha256 as hash_password

def hash(password: str):
    return hash_password.hash(password)


def verify(plain_password, hashed_password):
    return hash_password.verify(plain_password,hashed_password)