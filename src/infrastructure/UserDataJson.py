
import json

from src.domain.UserData import UserData


class UserDataJson(UserData):
    def __init__(self):
        with open("user_data.json", "r", -1, "utf-8") as file:
            data = json.load(file)

        self.user_id = data["user_id"]
        self.name = data["name"]
        self.start_date = data["start_date"]
        self.start_balance = data["start_balance"]
        self.api_key = data["api_key"]
        self.api_secret = data["api_secret"]
        self.max_risk_percent = data["max_risk_percent"]
