
import firebase_admin
from firebase_admin import credentials, firestore

from src.domain.UserData import UserData


class UserDataFirebase(UserData):
    def __init__(self, user_id: str):
        cred = credentials.Certificate(
            'src/infrastructure/firestore_cred.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        doc_ref = db.collection('clients').document(user_id)

        doc = doc_ref.get()
        if not doc.exists:
            print('No such user!')

        data = doc.to_dict()

        self.user_id = user_id
        self.name = data["name"]
        self.start_date = data["initialDate"]
        self.start_balance = data["initialBalance"]
        self.api_key = data["apiKey"]
        self.api_secret = data["apiSecret"]
        self.max_risk_percent = data["maxLostPerTradePercent"]
