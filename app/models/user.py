from app.firebase.firebase_config import db;
from app.utils.crypt_password import crypt_password;
from typing import Dict, List
from google.cloud.firestore_v1 import FieldFilter
from datetime import datetime

class User():
    
    @staticmethod
    async def add_user(user: str) -> Dict[str, bool | List[str]]:
        user_ref = db.collection("users");

        user["password"] = crypt_password(user["password"]).decode("utf-8");
        
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        user["created_at"] = date;
        user["update_at"] = date;

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
    
    @staticmethod
    async def email_already_exists(email: str) -> bool:

        user_ref = db.collection("users");
        
        try:
            user_query = user_ref.where(filter=FieldFilter("email", "==", email));
            docs = user_query.get();
            return docs[0].exists;
        except:
            return False;
