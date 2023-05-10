from dataclasses import dataclass

from src.common.Validate import Validate


@dataclass()
class UserData(Validate):
    user_id: str
    name: str
    start_date: str
    start_balance: float
    api_key: str
    api_secret: str
    max_risk_percent: int
