import telebot
import config
from database import get_user_id, get_user_balance, get_bot_messages
import keyboards
import logic

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)


@bot.callback_query_handler(func=lambda c: '' in c.data)
def buttons_init(data):
    logic.main(bot, data)


@bot.message_handler()
def message_init(message):
    messages_db = get_bot_messages.main(message.text)
    if messages_db is not None:
        if messages_db['u_id'] == '1':
            balance = get_user_balance.main(get_user_id.main(message))
            bot.send_message(message.chat.id, f'{messages_db["text"].replace("{balance}", str(balance))}',
                             reply_markup=[keyboards.button_to_menu(messages_db["buttons"])])
        elif messages_db['u_id'] == '2':
            bot.send_message(message.chat.id, f'{messages_db["text"]}',
                             reply_markup=[keyboards.menu(messages_db["buttons"])])


bot.polling(none_stop=True)
