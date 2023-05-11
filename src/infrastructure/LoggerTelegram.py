from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from src.domain.Commands import Commands

from src.domain.Logger import Logger


class LoggerTelegram(Logger):
    def __init__(self, token: str, chat_id: str) -> None:
        self.chat_id = chat_id
        self.token = token

    async def ping(self, text):
        bot = Bot(token=self.token)
        await bot.sendMessage(self.chat_id, text)

    def mount_telegram(self) -> None:
        app = ApplicationBuilder().token(self.token).build()

        app.add_handler(CommandHandler(
            Commands.info, self.info_handler))
        app.add_handler(CommandHandler(
            Commands.pnl, self.pnl_handler))

        app.run_polling()

    async def info_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # pylint: disable=W0613
        response = f'Hello {update.effective_user.first_name}, the info will be right here.'
        await update.message.reply_text(response)

    async def pnl_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:  # pylint: disable=W0613
        response = f'Hello {update.effective_user.first_name}, the pnl info will be right here.'
        await update.message.reply_text(response)
