from abc import ABC, abstractmethod


class UserData(ABC):
    user_id: str
    name: str
    start_date: str
    start_balance: float
    api_key: str
    api_secret: str
    max_risk_percent: int

    @abstractmethod
    def get_user_data(self, user_id: str):
        pass
