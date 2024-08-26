from typing import Dict, List
from app.utils.schema.user_validation_schema import User_Validation_Schema


class User_Validations_Manager(User_Validation_Schema):

    def __init__(self, user):
        super().__init__(user=user);

    async def validate_login(self) -> Dict[str, bool | List[str]]:
        email_is_valid = await super().email_validation();
        password_valid = super().password_validation();
        password_two_valid = super().password_two_validation();
        compare_valid = super().compare_password();
    
        if not email_is_valid["success"]:
            return email_is_valid;

        if not password_valid["success"]:
            return password_valid;

        if not password_two_valid["success"]:
            return password_two_valid;
        if not compare_valid["success"]:
            return compare_valid;

        return {
            "success": True,
        };

    

    async def validate_register(self) -> Dict[str, bool | List[str]]:

        user_name_is_valid = super().user_name_validation();
        email_is_valid = await super().email_validation(True);
        password_is_valid = super().password_validation();

        if not user_name_is_valid["success"]:
            return user_name_is_valid;

        if not email_is_valid["success"]:
            return email_is_valid;

        if not password_is_valid["success"]:
            return password_is_valid;

        return {
            "success": True,
        };