from app.controllers.user_register_controller import UserRegisterController;
from app.controllers.user_login_controller import UserLoginController;
from app.controllers.parking_controller import Parking_Controller;

from app.middleware.login_requires import login_required;

from flask import Flask

app = Flask(__name__);

if (__name__ == "__main__"):
    app.run(debug=True);

@app.route("/")
def home():
    return "Hello World";

app.add_url_rule(
    "/user/register",
    view_func=UserRegisterController.as_view("user_post"),
    methods=["POST"],
);

app.add_url_rule(
    "/user/login",
    view_func=UserLoginController.as_view("user_login"),
    methods=["POST"],
);


app.add_url_rule(
    "/parking",
    view_func=login_required(Parking_Controller.as_view("parking_post")),
    methods=["POST"],
);


