

from src.domain.Stages import Stages
from src.domain.UserData import UserData


class Trade:
    def __init__(self, user_data: UserData):
        # Stages
        self.stage: Stages = Stages.start

        # User Data
        self.user_data = user_data
        self.user_data.validate_fields()

        print(self)

    def __str__(self) -> str:
        return f"Trade: stage {self.stage} - {self.user_data.name}"

    user_data: UserData = None
