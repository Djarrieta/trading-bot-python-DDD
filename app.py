
import os
from src.infrastructure.UserDataJson import UserDataJson
from src.domain.Trade import Trade

user_id = os.environ.get('USER_ID')
print(user_id)

user_data = UserDataJson()
trade = Trade(user_data)
