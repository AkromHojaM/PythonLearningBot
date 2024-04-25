from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def menu_btn():
    design = [
        [InlineKeyboardButton(text="String",callback_data="string"),
             InlineKeyboardButton(text="Integer",callback_data="integer")],
        [InlineKeyboardButton(text="Boolean",callback_data="boolean"),
         InlineKeyboardButton(text="Set",callback_data="set")],
        [InlineKeyboardButton(text="Float",callback_data="float"),
         InlineKeyboardButton(text="List",callback_data="list")],
    ]
    reply_murkup = InlineKeyboardMarkup(inline_keyboard=design)
    return reply_murkup

def menu():
    design1 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
         InlineKeyboardButton(text="Set",callback_data="set")],
         [InlineKeyboardButton(text="Boolean",callback_data="boolean"),
         InlineKeyboardButton(text="Float",callback_data="float")],
        [InlineKeyboardButton(text="List",callback_data="list"),
         ]
    ]
    reply_murkup1 = InlineKeyboardMarkup(inline_keyboard=design1)
    return reply_murkup1
def menu1():
    design2 = [
        [InlineKeyboardButton(text="Set",callback_data="set"),
         InlineKeyboardButton(text="String",callback_data="string")],
         [InlineKeyboardButton(text="Boolean",callback_data="boolean"),
         InlineKeyboardButton(text="Float",callback_data="float")],
        [InlineKeyboardButton(text="List",callback_data="list"),]
    ]
    reply_murkup2 = InlineKeyboardMarkup(inline_keyboard=design2)
    return reply_murkup2
def menu2():
    design3 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
         InlineKeyboardButton(text="String",callback_data="string")],
         [InlineKeyboardButton(text="Boolean",callback_data="boolean"),
         InlineKeyboardButton(text="Float",callback_data="float")],
        [InlineKeyboardButton(text="List",callback_data="list"),]
    ]
    reply_murkup3 = InlineKeyboardMarkup(inline_keyboard=design3)
    return reply_murkup3
def menu3():
    design4 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
         InlineKeyboardButton(text="String",callback_data="string")],
         [InlineKeyboardButton(text="Set",callback_data="set"),
         InlineKeyboardButton(text="Boolean",callback_data="boolean")],
        [InlineKeyboardButton(text="List",callback_data="list"),]
    ]
    reply_murkup4 = InlineKeyboardMarkup(inline_keyboard=design4)
    return reply_murkup4

def menu4():
    design5 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
         InlineKeyboardButton(text="String",callback_data="string")],
         [InlineKeyboardButton(text="Set",callback_data="set"),
         InlineKeyboardButton(text="Float",callback_data="float")],
        [InlineKeyboardButton(text="List",callback_data="list"),]
    ]
    reply_murkup5 = InlineKeyboardMarkup(inline_keyboard=design5)
    return reply_murkup5
def menu5():
    design6 = [
        [InlineKeyboardButton(text="Integer",callback_data="integer"),
         InlineKeyboardButton(text="String",callback_data="string")],
         [InlineKeyboardButton(text="Set",callback_data="set"),
         InlineKeyboardButton(text="Float",callback_data="float")],
        [InlineKeyboardButton(text="Boolean",callback_data="boolean"),]
    ]
    reply_murkup6 = InlineKeyboardMarkup(inline_keyboard=design6)
    return reply_murkup6

# def menu6():
#     design7 = [
#         [InlineKeyboardButton(text="Souma",callback_data="souma")]]
#     reply_murkup7 = InlineKeyboardMarkup(inline_keyboard=design7)
#     return reply_murkup7