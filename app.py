
from src.domain.Trade import Trade
from src.services.UserDataJson import UserDataJson


user_data = UserDataJson()
trade = Trade(user_data)
trade.run()
