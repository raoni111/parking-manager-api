from app.firebase.firebase_config import db;
from app.utils.crypt_password import crypt_password, check_password;
from app.utils.gen_jwt import gen_jwt;
from typing import Dict, List;
from google.cloud.firestore_v1 import FieldFilter;
from datetime import datetime;

class User():

    @staticmethod
    async def add_user(user: Dict[str, str]) -> Dict[str, bool | List[str]]:
        user_ref = db.collection("users");

        user["password"] = crypt_password(user["password"]).decode("utf-8");
        
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S");

        user["created_at"] = date;
        user["update_at"] = date;

        try:
            user_ref.add(user);

            return  {
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
    async def login_user(user: Dict[str, str]):

        user_ref = db.collection("users");

        try:
            doc = user_ref.where(filter=FieldFilter("email", "==", user["email"])).get()[0];
        except IndexError:
            return  {
                "success": False,
                "messages": [
                    "email ou senha invalido!"
                ]
            }

        if not doc.exists:
            return {
                "success": False,
                "message": [
                    "usuário não encontrado.",
                ],
            }
    
        doc_dict = doc.to_dict();

        password_valid = check_password(user["password"], doc_dict["password"]);
    
        if not password_valid:
            return {
                "success": False,
                "messages": [
                    "email ou senha invalido!"
                ]
            }
    
        database_user = {
            "id": doc.id,
            "user_name": doc_dict["user_name"],
            "email": doc_dict["email"],
            "created_at": doc_dict["created_at"],
            "update_at": doc_dict["update_at"],
        };
    
        user_token = gen_jwt(database_user);

        database_user["token"] = user_token;
    
        return {
            "success": True,
            "message": [
                "login efetuado com sucesso"
            ],
            "user": database_user,
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
