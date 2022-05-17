from telegram.ext import CommandHandler
from bot import AUTHORIZED_CHATS, dispatcher
from bot.helper.ext_utils.bot_utils import new_thread
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage
from bot.helper.ext_utils.parser import get_gp_link

@new_thread
def scrape_gp(update, context):
    try:
       query = update.message.text.split()[1]
    except:
       sendMessage('<b>Give a link! 👀</b>', context.bot, update)
       return
 
    if not query.startswith("https://gplinks") or query.startswith("gplinks"):
       sendMessage('<b>Sorry, all I do is scrape GPLinks URLs :(</b>', context.bot, update)
       return

    m = sendMessage('<b>Please wait...</b>', context.bot, update)
    link = get_gp_link(query)
    deleteMessage(context.bot, m)
    if not link:      
       sendMessage("Something went wrong\nTry again later..", context.bot, update)
    else:
       sendMessage(f"<b>Here is your direct link:\n\n{link}</b>", context.bot, update)


gplink_handler = CommandHandler("scrape", scrape_gp,
                               filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(gplink_handler)
