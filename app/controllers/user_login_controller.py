from flask.views import View;
from flask import request;
from app.utils.user_validation_manager import User_Validations_Manager;
from app.models.user import User;

class UserLoginController(View):

    async def dispatch_request(self):

        if (request.method == "POST"):

            jsonData = request.get_json();
            
            validations_manager = User_Validations_Manager(jsonData);
            validation_response = await validations_manager.validate_login();

            if not validation_response["success"]:
                return validation_response, 400;
        
            login_response = await User.login_user(jsonData);

            if not login_response["success"]:
                return login_response, 400;

            return login_response, 200;


        return "error", 400
