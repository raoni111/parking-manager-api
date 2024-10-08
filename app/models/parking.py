from app.firebase.firebase_config import db;
from datetime import datetime;
from typing import Dict;

class Parking():

    @staticmethod
    async def create(parking: Dict[str, str], user: Dict[str, str]):
        parking_ref = db.collection("parking");

        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S");

        parking["created_at"] = date; 
        parking["updated_at"] = date;

        parking["issuer"] = {
            "id": user["id"],
            "user_name": user["user_name"],
        }

        try:
            parking_ref.add(parking);

            return {
                "success": True,
                "messages": [
                    "Dados do estacionamento registrado com sucesso."
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    "Não foi possível registrar os dados do estacionamento."
                ]
            };
