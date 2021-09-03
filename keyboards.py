from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton


def button_to_menu(a):
    button_hi = KeyboardButton(a[0])
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    greet_kb.add(button_hi)
    return greet_kb


def menu(a):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton(a[0], callback_data='personal_area_from_menu'))
    markup.row(InlineKeyboardButton(a[1], callback_data='sms_buy_from_menu'))
    markup.row(InlineKeyboardButton(a[2], callback_data='products_from_menu'))
    markup.row(InlineKeyboardButton(a[3], callback_data='agreement_from_menu'))
    markup.row(InlineKeyboardButton(a[4], url='https://t.me/maqqaz'))
    return markup


def profile(a):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton(a[0], callback_data='add_balance_from_personal_area'))
    markup.row(InlineKeyboardButton(a[1], callback_data='buy_list_from_personal_area'))
    markup.row(InlineKeyboardButton(a[2], callback_data='back_from_personal_area'))
    return markup


def add_balance_1(a):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton(a[0], callback_data='balance_1_from_add_balance_from_personal_area'))
    return markup


def to_menu(a):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.row(InlineKeyboardButton(a[0], callback_data='to_menu'))
    return markup