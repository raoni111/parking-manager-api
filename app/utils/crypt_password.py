from bcrypt import (
    hashpw,
    gensalt,
);

def crypt_password(password: str):
    return hashpw(password.encode("utf-8"), gensalt());