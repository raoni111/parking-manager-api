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
                    "Dados do estacionamento registrado com sucesso.",
                ]
            };
        except:
            return {
                "success": False,
                "messages": [
                    "Não foi possível registrar os dados do estacionamento.",
                ]
            };

    async def update(parking: Dict[str, str], parkingId: str):
        parking_ref = db.collection('parking').document(parkingId);

        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S");
        
        parking["updated_at"] = date;
    
        try:
            parking_ref.update(parking);
        
            return {
                "success": True,
                "messages": [
                    "Dados do estacionamento editado com sucesso.",
                ]
            }
        except: 
            return {
                "success": False,
                "messages": [
                    "Não foi possível editar os dados do estacionamento.",
                ]
            }

    async def delete(parkingId: str):
        parking_ref = db.collection('parking').document(parkingId);

        try:
            parking_ref.delete();
    
            return {
                "success": True,
                "messages": [
                    "Dados deletado com sucesso",
                ]
            }
        except: 
            return {
                "success": False,
                "messages": [
                    "Não foi possível deletar os dados do parking"
                ]
            }

    async def getOne(parkingId: str): 
        parking_ref = db.collection("parking").document(parkingId);
    
        try:
            response = parking_ref.get();
    
            return response;
        except:
            return {
                "success": False,
                "messages": [
                    "Não foi possível encontrar os dados do estacionamento"
                ]
            }

    @staticmethod
    async def get():
        parking_ref = db.collection("parking");

        try:
            response = parking_ref.get();
        
            return response;
        except:
            return {
                "success": False,
                "messages": [
                    "Não foi possível encontrar estacionamentos"
                ]
            }
