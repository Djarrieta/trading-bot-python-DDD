

from src.domain.Exchange import Exchange
from src.domain.Logger import Logger
from src.domain.Stage import Stage
from src.domain.UserData import UserData


class Trade:
    def __init__(self, user_data: UserData, logger: Logger, exchange: Exchange):
        # Stage
        self.stage: Stage = Stage.start

        # User Data
        self.user_data = user_data
        self.user_data.validate_fields()

        # Logger
        self.logger = logger
        self.logger.log("This is a good start")

        # Exchange
        self.exchange = exchange

        # Mount Websockets
        self.logger.mount()
        self.exchange.mount()

    def __str__(self) -> str:
        return f"Trade: stage {self.stage} - {self.user_data.name}"

    user_data: UserData = None
    logger: Logger = None
    exchange: Exchange = None
