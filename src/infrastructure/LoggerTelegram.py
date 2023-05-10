from src.domain.Logger import Logger


class LoggerTelegram(Logger):
    def __init__(self, token: str, chat_id: str) -> None:
        print(token, chat_id)

    def ping(self, text):
        print(text)
