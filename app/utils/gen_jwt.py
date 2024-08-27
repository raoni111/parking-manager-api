from typing import Dict
from dotenv import dotenv_values
import jwt
import os

config = dotenv_values("./.env");

def gen_jwt(user: Dict[str, str]) -> str:
    return jwt.encode(user, config["JWT_TOKEN"], algorithm="HS256");

def get_user_by_jwt(token: str):
    try: 
        user_data = jwt.decode(token, config["JWT_TOKEN"], algorithms="HS256");

        return {
            "success": True,
            "user": user_data,
        }
    except:
        return {
            "success": False
        }