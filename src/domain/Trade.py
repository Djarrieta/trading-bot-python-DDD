

from src.domain.Stages import Stages
from src.domain.UserData import UserData


class Trade:
    user_data: UserData

    def __init__(self, user_data: UserData):
        self.stage: Stages = Stages.start
        self.user_data = user_data

    def run(self):
        print(self.stage)
        self.user_data.get_user_data("")
        print(self.user_data.name)
