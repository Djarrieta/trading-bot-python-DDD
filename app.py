import os

from src.domain.Trade import Trade
from src.infrastructure.ExchangeBinance import ExchangeBinance
from src.infrastructure.LoggerTelegram import LoggerTelegram
from src.infrastructure.UserDataFirestore import UserDataFirestore

user_id = os.environ.get('USER_ID')
user_data = UserDataFirestore(user_id)
logger = LoggerTelegram(token=user_data.token, chat_id=user_data.chat_id)
exchange = ExchangeBinance(api_key=user_data.api_key,
                           api_secret=user_data.api_secret)


trade = Trade(user_data, logger, exchange)
