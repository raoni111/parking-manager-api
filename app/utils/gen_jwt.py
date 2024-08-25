from typing import Dict
from dotenv import dotenv_values
import jwt
import os

config = dotenv_values("./.env");

def gen_jwt(user: Dict[str, str]):
    return jwt.encode(user, config["JWT_TOKEN"], algorithm="HS256");