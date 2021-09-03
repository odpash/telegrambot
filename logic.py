from database import get_bot_messages
from keyboards import menu
from steps import agreement, products, profile, sms


def answer_edit_message(bot, call, text, menu=None, callback=''):
    try:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              text=text,
                              message_id=call.message.message_id,
                              reply_markup=[menu],
                              parse_mode='HTML')
    except:
        pass
    bot.answer_callback_query(callback_query_id=call.id, text=callback)



def main(bot, data):
    print(data.data)
    if data.data == 'to_menu':
        messages_db = get_bot_messages.main_by_u_id('2')
        answer_edit_message(bot, data, messages_db['text'], menu(messages_db['buttons']))
    if 'personal_area' in data.data:
        profile.main(bot, data)
    elif 'sms_buy' in data.data:
        sms.main(data)
    elif 'products' in data.data:
        products.main(data)
    elif 'agreement' in data.data:
        agreement.main(bot, data)
    else:
        pass
