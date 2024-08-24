from app.firebase.firebase_config import db;
from app.utils.crypt_password import crypt_password;

class User():
    
    @staticmethod
    async def add_user(user):
        user_ref = db.collection("users");

        user["password"] = crypt_password(user["password"]).decode("utf-8");

        try:
            user_ref.add(user);
            return {
                "success": True,
                "message": [
                    "registro efetuado com sucesso.",
                ]
            }
        except:
            return {
                "success": False,
                "message": [
                    "não foi possível registrar o seu dados.",
                ]
            }

