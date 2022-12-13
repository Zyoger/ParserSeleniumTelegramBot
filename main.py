# pip freeze > requirements.txt
import logging
import time
from telegram import __version__ as TG_VER
from parser import get_prise
from dbms import add_task_in_tab, read_task, create_tab

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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    # chat_id = update.effective_message.chat_id
    user = update.effective_user
    await update.message.reply_html(rf"Привет {user.mention_html()}!")
    await update.message.reply_text("/help - помощь.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("/status - посмотреть текущие задачи.")
    await update.message.reply_text("/add - добавить задачу.")
    await update.message.reply_text("/check - проверить задачи.")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """"""
    list_tasks = read_task()
    await update.message.reply_text(f"Сейчас {len(list_tasks)} заданий:")
    for i in range(len(list_tasks)):
        await update.message.reply_text(f"{list_tasks[i][1]}")


async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_message.chat_id
    try:
        temp = context.args[0]
        task = temp.split("@")
        add_task_in_tab(task[0], task[1], task[2], task[3], task[4])
        due = float(task[4])*1
        context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)
        await update.message.reply_text("Задание добавлено!")
    except IndexError:
        await update.message.reply_text("Ошибка!!! Задание не добавлено! Не верное количество аргументов!")
        # /add https://bask.ru/catalog/kurtka-bask-vorgol-v2-20212/@span@@5@24


async def check_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    list_tasks = read_task()
    for task in list_tasks:
        # print(task[1], task[2], task[3], task[4])
        prise = get_prise(task[1], task[2], task[3], int(task[4]))
        await update.message.reply_text(f"{task[1]}\n ✅👉🏻 Текущая цена: {prise}👈🏻✅")
    # url, type_tag, name_tag, number_position, verification_period


async def alarm(context: ContextTypes.DEFAULT_TYPE):
    """Send the alarm message."""
    list_tasks = read_task()
    job = context.job
    await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")


def main() -> None:
    application = Application.builder().token("5889318762:AAFOo747AOquQaqesrhUzyLtBuH-EdadJXI").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("check", check_tasks))
    application.run_polling()


if __name__ == "__main__":
    main()

