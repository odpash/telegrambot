import keyboards
from database import get_bot_messages, get_user_balance


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
    if 'from_menu' in data.data:
        messages_db = get_bot_messages.main_by_u_id('3')
        balance = get_user_balance.main(data.from_user.id)
        answer_edit_message(bot, data, messages_db['text'].replace('{balance}', str(balance)),
                            keyboards.profile(messages_db['buttons']))
    elif 'personal_area' in data.data:
        if 'from_add_balance' in data.data:
            data.data = 'from_menu'
            main(bot, data)





        elif 'back' in data.data:
            messages_db = get_bot_messages.main_by_u_id('2')
            answer_edit_message(bot, data, messages_db['text'], keyboards.menu(messages_db['buttons']))
        elif 'add_balance' in data.data:
            messages_db = get_bot_messages.main_by_u_id('3.1')
            answer_edit_message(bot, data, messages_db['text'], keyboards.add_balance_1(messages_db['buttons']))
        elif 'buy_list' in data.data:
            messages_db = get_bot_messages.main_by_u_id('3.2')
