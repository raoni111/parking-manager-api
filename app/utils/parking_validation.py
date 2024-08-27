from app.utils.schema.validation_schema import Validation_Schema;
from typing import Dict;

class Parking_Validation(Validation_Schema):
    def __init__(self, parking: Dict[str, str]):
        super().__init__(object_valid=parking);

    def parking_is_valid(self):
        name_is_valid = super().text_validation_required(
            "name",
            "O campo nome não esta preenchido.",
        );

        street_is_valid = super().text_validation_required(
            "street",
            "O campo nome da rua deve ser preenchido",
        );
    
        number_is_valid = super().int_validation_required(
            "number",
            "O campo numero deve ser preenchido",
        );

        car_space = super().int_validation_required(
            "car_spaces",
            "O campo numero vagas precisa ser preenchido"
        );

        if not name_is_valid["success"]:
            return name_is_valid;

        if not street_is_valid["success"]:
            return street_is_valid;

        if not number_is_valid["success"]:
            return number_is_valid;

        if not car_space:
            return car_space;

        return {
            "success": True
        }