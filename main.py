# pip freeze > requirements.txt
import logging
import time
from telegram import __version__ as TG_VER
from parser import get_prise
from dbms import add_task_in_db, read_task

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

URL = 'https://bask.ru/catalog/kurtka-bask-vorgol-v2-20212/'
tag = "span"
name = ""
number = 5
chat_id = 0


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global chat_id
    chat_id = update.effective_message.chat_id
    user = update.effective_user
    await update.message.reply_html(rf"Привет {user.mention_html()}!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("/status - узнать цену на текущие товары.")
    await update.message.reply_text("/addtask - добавить задачу.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """"""
    global URL, tag, name, number
    await update.message.reply_text(f"Цена: {get_prise(URL, tag, name, number)}")


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пример")
    temp = context.args[0]
    task = temp.split("@")
    id_task = 123456788
    add_task_in_db(id_task, task[0], task[1], task[2], task[3], task[4])
    # /addtask bask.ru/catalog/kurtka-bask-vorgol-v2-20212/@span@@5@24


async def check_tasks(update: Update):
    read_task()
    pass


def main() -> None:
    application = Application.builder().token("5889318762:AAGrWVxJJNllNZsbzdtdLf355mRf4hveOL4").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("addtask", add_task))
    application.run_polling()


if __name__ == "__main__":
    main()

