
import os
from src.infrastructure.UserDataFirebase import UserDataFirebase
from src.domain.Trade import Trade

user_id = os.environ.get('USER_ID')
user_data = UserDataFirebase(user_id)

trade = Trade(user_data)
