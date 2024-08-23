from app.controllers.user_controller import UserController
from flask import Flask

app = Flask(__name__);

@app.route("/")
def home():
    return "Hello World"

app.add_url_rule(
    "/user",
    view_func=UserController.as_view("user_post"),
    methods=["POST"]
)