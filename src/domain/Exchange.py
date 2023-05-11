from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Exchange(ABC):
    @abstractmethod
    def mount(self):
        pass

    @abstractmethod
    async def set_entry(self):
        pass

    @abstractmethod
    async def set_stop_loss(self):
        pass

    @abstractmethod
    async def set_take_profit(self):
        pass

    @abstractmethod
    async def set_position(self):
        pass

    @abstractmethod
    async def close_all_orders(self):
        pass
