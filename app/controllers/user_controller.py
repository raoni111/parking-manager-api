from flask.views import View
from flask import request, jsonify
from app.models.user import User
from app.utils.validations_manger import Validations_manager

class UserController(View):

    async def dispatch_request(self):
        
        if request.method == "POST":
            jsonData = request.get_json()

            validations_manager = Validations_manager(jsonData)

            validations_response = await validations_manager.validate()

            if not validations_response["success"]:
                return jsonify(validations_response), 400
            
            register_response = await User.add_user(jsonData);

            return jsonify(register_response), 200

        return "error"