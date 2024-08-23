from flask.views import View
from flask import request

from app.utils.validations_manger import Validations_manager

class UserController(View):

    def dispatch_request(self):


        if (request.method == "POST"):

            jsonData = request.get_json();

            validations_manager = Validations_manager(
                jsonData["user_name"],
                jsonData["email"],
                jsonData["password"]
            );

            validations_response = validations_manager.validate();

            if (validations_response["success"] == False):
                return validations_response;


            return validations_response;

        return 'error'
