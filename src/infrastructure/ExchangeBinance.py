from binance import ThreadedWebsocketManager
from binance.client import Client

from src.domain.Exchange import Exchange


class ExchangeBinance(Exchange):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(self.api_key, self.api_secret)
        self.twm = ThreadedWebsocketManager(
            self.api_key, self.api_secret)

        # self.twm.start_futures_user_socket(self.socket_handler_user)

        self.get_balance()
        # self.subscribe_to_ticker()

    def socket_handler_user(self, msg):
        print("started")
        print(msg)

    def subscribe_to_ticker(self):
        self.twm.start()
        streams = ['btcusdt@miniTicker', 'ethusdt@miniTicker']
        self.twm.start_multiplex_socket(
            callback=self.socket_handler_ticker, streams=streams)

        self.twm.join()

    def socket_handler_ticker(self, msg):
        print(msg["data"]["s"], msg["data"]["c"])

    def mount(self):
        pass

        # print(cm_futures_client.account())
    def get_balance(self):
        response = self.client.futures_account_balance()
        balance = list(filter(lambda x: x["asset"] == 'USDT', response))

        print(balance[0]["balance"])

    def message_handler(self, message):
        print(message)

    async def set_entry(self):
        pass

    async def set_stop_loss(self):
        pass

    async def set_take_profit(self):
        pass

    async def set_position(self):
        pass

    async def close_all_orders(self):
        pass
