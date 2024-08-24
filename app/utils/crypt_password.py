from bcrypt import (
    hashpw,
    gensalt,
    checkpw
);

def crypt_password(password: str) -> bytes:
    return hashpw(password.encode("utf-8"), gensalt());

def check_password(password: str, passwordHashed: str) -> bool:
    return checkpw(
        password,
        passwordHashed
    );