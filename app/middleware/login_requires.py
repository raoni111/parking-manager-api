from functools import wraps;
from flask import request, abort, make_response;
from app.utils.gen_jwt import get_user_by_jwt;
import json

def login_required(func):
    @wraps(func)
    def inner_function(*args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1];

        jwt_response = get_user_by_jwt(token);
        
        if not jwt_response["success"]:
            return abort(401);
    
        kwargs["user"] = jwt_response["user"];

        return func(*args, **kwargs);

    return inner_function