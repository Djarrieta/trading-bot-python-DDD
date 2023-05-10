
import os
from src.infrastructure.LoggerTelegram import LoggerTelegram
from src.domain.Trade import Trade
from src.infrastructure.UserDataFirestore import UserDataFirestore

user_id = os.environ.get('USER_ID')
user_data = UserDataFirestore(user_id)
logger = LoggerTelegram()

trade = Trade(user_data, logger)
