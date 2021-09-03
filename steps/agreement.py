from database import get_bot_messages
from keyboards import to_menu

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
    if data.data == 'agreement_from_menu':
        messages_db = get_bot_messages.main_by_u_id('4')
        answer_edit_message(bot, data, messages_db['text'], to_menu(messages_db['buttons']))