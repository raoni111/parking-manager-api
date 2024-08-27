from validation import validate_text, validate_int
from typing import Dict;

class Validation_Schema():
    
    def __init__(self, object_valid: Dict[str, str]):
        self.object_valid = object_valid;

    def text_validation(self, key: str, error_messages: str, min_length=1):
        try:
            validate_text(
                self.object_valid[key], 
                min_length=min_length
            );
            return {
                "success": True,
            }
        
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "valor invalido.",
                ]
            };
        except: 
            return {
                "success": False,
                "messages": [error_messages],
            };

    def text_validation_required(self, key: str, error_messages: str, min_length=1):
        try:
            validate_text(
                self.object_valid[key], 
                min_length=min_length,
                required=True,
            );
            return {
                "success": True,
            }
        
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "valor invalido.",
                ]
            };
        except: 
            return {
                "success": False,
                "messages": [error_messages],
            };

    def int_validation_required(self, key: str, error_message: str):
        try:
            validate_int(self.object_valid[key], required=True);

            return {
                "success": True,
            };
        
        except KeyError:
            return {
                "success": False,
                "messages": [
                    "valo invalido."
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    error_message,
                ]
            };
