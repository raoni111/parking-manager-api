from validation import (
    validate_email_address,
    validate_structure,
    validate_text,
)


class Validations_manager():

    def __init__(self, user_name, email, password):
        self.user = {
            "user_name": user_name,
            "email": email,
            "password": password,
        }

    def validate(self):
        user_name_is_valid = self.user_name_validation();
        email_is_valid = self.email_validation();
        password_is_valid = self.password_validation();

        if (user_name_is_valid["success"] == False):
            return user_name_is_valid;
        
        if (email_is_valid["success"] == False):
            return email_is_valid;
        
        if (password_is_valid["success"] == False):
            return password_is_valid;
        
        return {
            "success": True,
        };

    def user_name_validation(self):
        try:
            validate_text(self.user["user_name"], min_length=8)
        except:
            return {
                "success": False,
                "messages": [
                    "nome precisa ter no mínimo 8 caracteres"
                ]
            };
    
        return {
                "success": True,
        };

    def email_validation(self):
        try:
            validate_email_address(self.user["email"], required=True)
        except:
            return {
                "success": False,
                "messages": [
                    "email não e valido"
                ]
            };

        return {
            "success": True,
        };

    def password_validation(self):
        try:
            validate_text(self.user["password"], min_length=8)
        except:
            return {
                "success": False,
                "messages": [
                    "senha precisa ter no mínimo 8 caracteres"
                ]
            };
        
        return {
                "success": True,
        };
