import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Logger(ABC):
    def log(self, text: str):

        print(
            f"""
_________________
{self.formattedDate()}
{text}
            """
        )

    def formattedDate(self, date: datetime = "") -> str:
        formatted_date = ""
        if date is None:
            formatted_date = datetime.datetime.strptime(
                date, "%Y-%m-%d %H:%M:%S")
        else:
            formatted_date = datetime.datetime.now() .strftime("%Y-%m-%d %H:%M:%S")

        return formatted_date

    @abstractmethod
    def ping(self, text: str):
        pass
