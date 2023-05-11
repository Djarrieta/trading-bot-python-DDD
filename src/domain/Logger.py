import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Logger(ABC):
    @abstractmethod
    def mount(self):
        pass

    @abstractmethod
    async def ping(self, text: str):
        pass

    def log(self, text: str):

        print(
            f"""
_________________
{self.formattedDate()}
{text}
            """
        )

    def formattedDate(self, date: str = None) -> str:
        formatted_date = ""
        if date is None:
            now = datetime.datetime.now()
            formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        else:
            formatted_date = datetime.datetime.strptime(
                date, "%y-%m-%d %H:%M:%S")

        return formatted_date
