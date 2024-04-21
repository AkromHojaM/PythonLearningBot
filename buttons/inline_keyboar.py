from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu_btn():
    design = [
        [InlineKeyboardButton(text="String",callback_data="string"),
             InlineKeyboardButton(text="Integer",callback_data="integer"),
             ]]
    reply_murkup = InlineKeyboardMarkup(inline_keyboard=design)
    return reply_murkup

def menu():
    design1 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
    ]]
    reply_murkup1 = InlineKeyboardMarkup(inline_keyboard=design1)
    return reply_murkup1