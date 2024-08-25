from validation import (
    validate_email_address,
    validate_text,
);
from typing import Dict, List
from app.models.user import User


class Validations_manager():

    def __init__(self, user):
        self.user: Dict[str, str] = user;

    async def validate_login(self) -> Dict[str, bool | List[str]]:
        email_is_valid = await self.email_validation();
        password_valid = self.password_validation();
        password_two_valid = self.password_two_validation();
        compare_valid = self.compare_password();
    
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

    

    async def validate(self) -> Dict[str, bool | List[str]]:

        user_name_is_valid = self.user_name_validation();
        email_is_valid = await self.email_validation(True);
        password_is_valid = self.password_validation();

        if not user_name_is_valid["success"]:
            return user_name_is_valid;

        if not email_is_valid["success"]:
            return email_is_valid;

        if not password_is_valid["success"]:
            return password_is_valid;

        return {
            "success": True,
        };

    def user_name_validation(self) -> Dict[str, bool | List[str]]:

        try:
            validate_text(self.user["user_name"], min_length=8);
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "nome tem um valor invalido!"
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    "nome precisa ter no mínimo 8 caracteres."
                ]
            };

        return {
                "success": True,
        };

    async def email_validation(self, validate_email_already_exists=False) -> Dict[str, bool | List[str]]:

        try:
            validate_email_address(self.user["email"], required=True);
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "email tem um valor invalido!"
                ]
            };

        except:
            return {
                "success": False,
                "messages": [
                    "email não e valido."
                ]
            };
    
        if not validate_email_already_exists:
            return {
                "success": True,
            }

        email_existis = await User.email_already_exists(self.user["email"]);

        if (email_existis):
             return {
                "success": False,
                "messages": [
                    "email ja esta em uso."
                ]
            };

        return {
            "success": True,
        };

    def password_validation(self) -> Dict[str, bool | List[str]]:

        try:
            validate_text(self.user["password"], min_length=8);
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "senha tem um valor invalido!"
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    "senha precisa ter no mínimo 8 caracteres."
                ]
            };

        return {
                "success": True,
        };

    def password_two_validation(self) -> Dict[str, bool | List[str]]:

        try:
            validate_text(self.user["password_two"], min_length=8);
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "senha tem um valor invalido!"
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    "senha precisa ter no mínimo 8 caracteres."
                ]
            };
        
        return {
            "success": True,
        };

    def compare_password(self) -> Dict[str, bool | List[str]]:
        try:
            if self.user["password"] != self.user["password_two"]:
                return {
                    "success": False,
                    "messages": [
                        "as senhas não são iguais."
                    ]
            }
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "as senhas tem um valor invalido!"
                ]
            };
        
        return {
            "success": True
        }