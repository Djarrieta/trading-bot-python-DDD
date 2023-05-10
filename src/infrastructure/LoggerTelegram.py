from src.domain.Logger import Logger


class LoggerTelegram(Logger):

    def ping(self, text):
        print(text)
