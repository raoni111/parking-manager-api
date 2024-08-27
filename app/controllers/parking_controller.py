from flask.views import View;
from flask import request;
from app.utils.parking_validation import Parking_Validation;
from app.models.parking import Parking;
import json;

class Parking_Controller(View):

    async def dispatch_request(self, user):
        if (request.method == "POST"):
            parking_json = request.get_json();

            parking_validation = Parking_Validation(parking_json);

            parking_validation_response = parking_validation.parking_is_valid();
            
            if not parking_validation_response["success"]:
                return parking_validation_response, 400;

            parking_create_response = await Parking.create(parking_json, user);

            if not parking_create_response["success"]:
                return parking_create_response, 400;

            return parking_create_response, 200;

        return "error"