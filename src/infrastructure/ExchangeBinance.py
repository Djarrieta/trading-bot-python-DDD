from src.domain.Exchange import Exchange


class ExchangeBinance(Exchange):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def mount(self):
        pass

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
