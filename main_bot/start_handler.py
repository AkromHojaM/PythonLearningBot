import os

from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types.bot_command import BotCommand
from buttons.inline_keyboar import menu_btn, menu,menu1,menu2,menu3,menu4,menu5
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from states.state import RegisterStates
#from DB.Db import PG


dp = Dispatcher()



@dp.message(CommandStart())
async def start_handler(msg: types.Message,state:FSMContext):
    #obj = PG()
    print(msg.message_id)
    #print(msg.chat.id)
    full_name = msg.from_user.full_name
    user_id = msg.from_user.id
    #obj.checked_user(user_id):
    await msg.answer(f"*Hello {full_name} Welcome to my bot you can learn what you don't know in python with this bot*\n"
    "\n"
    '*Enter Your Name*',parse_mode='Markdown')
    await state.set_state(RegisterStates.lastname)
    await msg.answer(text = "*You are already registered*",parse_mode='Markdown')
@dp.message(RegisterStates.lastname)
async def last_name_handler(msg: types.Message,state:FSMContext):
    lastname = msg.text
    await state.update_data(lastname=lastname)
    await state.set_state(RegisterStates.firstname)
    await msg.answer("Enter Your LastName",parse_mode='Markdown')

@dp.message(RegisterStates.firstname)
async def firstname_handler(msg: types.Message,state:FSMContext):
    #obj = PG()
    firstname = msg.text
    await state.update_data(firstname=firstname)
    data = await state.get_data()
    lastname = data.get('lastname')
    firstname = data.get('firstname')
    user_id = msg.from_user.id
    #obj.add(user_id,lastname,firstname)
    await msg.answer("Successfully registered",parse_mode='Markdown')
types_command = BotCommand(command = "types",description="Python Types")
@dp.message(Command(types_command))
async def types_command(msg:types.Message):

    await msg.answer(text = 'Select Your Type',reply_markup=menu_btn())

last_message_ids = {}
last_message_ids1 = {}
@dp.callback_query(lambda call:call.data == "string")
async def string_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "Types of Strings in Python:  Python has three types of strings: strings of type str, strings of type unicode and strings of type bytes. The difference between these types is in the way they store characters in memory. "
                                               "String and memory:In Python, we represent strings in memory as a null-terminated sequence of characters. "
                                               "This means that to store a string in a variable, you must include a null character at the end of the string. "
                                               "Sign of String(this("") and this(''))"
                                               "🤔If you don't understand the message information, you can look at the Video Information",parse_mode="Markdown")
    await call.message.answer("<a href='https://youtu.be/yqGcoWlekME?list=PLIHume2cwmHehcxQE1XZieL21syR3m3tR'>Yazilim Bilimlerini Derslerini Linke Tiklayarak Izleyebilirsiniz</a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu())

@dp.callback_query(lambda call:call.data == "integer")
async def integer_handler(call:types.CallbackQuery):
    if call.message.chat.id  in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "Integer data type in python is used to represent the whole numbers like 0, 1, 2, 3, 4 or negative integers such -1, -2, -3 etc. To define an integer variable, you can simply define a variable and assign a number to it as follows. "
                                               "Output: Unlike other programming languages, "
                                               "There is no limit on values of integer data types in python. You can define a number as large as per your wish but it is limited by the capability of your computer. "
                                               "🤔If you don't understand the message information, you can look at the Video Information",parse_mode="Markdown")
    mesages1 = await call.message.answer("<a href='https://youtu.be/EabKlNAN3LQ'>Pythona Giris Derslerini Linke Tiklayarak Izleyebilirsiniz</a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu1())

@dp.callback_query(lambda call:call.data == "set")
async def set_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "Sets are mutable, which means that they can be modified after they have been defined. "
                                               "According to the Python Documentation:"
                                               "The set type is mutable — the contents can be changed using methods like add() and remove(). Since it is mutable, it has no hash value and cannot be used as either a dictionary key or as an element of another set"
                                               " This Set {} sign"
                                               "🤔If you don't understand the message information, you can look at the Video Information",parse_mode="Markdown")
    await call.message.answer("<a href='https://youtu.be/OlSyO4O-GM8'>Yakin Kampus Derslerini Linke Tiklayarak Izleyebilirisniz </a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu2())

@dp.callback_query(lambda call:call.data == "float")
async def set_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "The float type in Python represents the floating point number. Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts. "
                                               "For example, 97.98, 32.3+e18, -32.54e100 all are floating point numbers. "
                                               "Python float values are represented as 64-bit double-precision values. The maximum value any floating-point number can be is approx 1.8 x 10 308. "
                                               "🤔If you don't understand the message information, you can look at the Video Information",parse_mode="Markdown")
    await call.message.answer("<a href='https://youtu.be/EabKlNAN3LQ'>Pythona Giris Derslerini Linke Tiklayarak Izleyebilirsiniz</a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu3())


@dp.callback_query(lambda call:call.data == "boolean")
async def set_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "Python boolean type is one of the built-in data types provided by Python, which represents one of the two values i.e. True or False. Generally, it is used to represent the truth values of the expressions. "
                                               "For example, 1==1 is True whereas 2<1 is False. "
                                               "Python Boolean Type. The boolean value can be of two types only i.e. either True or False. The output <class ‘bool’> indicates the variable is a boolean data type."
                                               "🤔If you don't understand the message information, you can look at the Video Information")
    await call.message.answer("<a href='https://youtu.be/IRRSXv0zWEs'>Yakin Kampus Derslerini Linke Tiklayarak Izleyebilirsiniz</a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu4())


@dp.callback_query(lambda call:call.data == "list")
async def set_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_message(call.message.chat.id, last_message_ids[call.message.chat.id])
    message = await call.message.answer(text = "There are many types of lists in python, like negative indexing, index range, beginning range, ending range, interchanging elements, length of a list, a loop of the list, and addition of elements."
                                               " Types of Python Lists with Example. "
                                               "In Python, the list data structure is used when the sequence of items has to be in the ordered form or needs to change for some operation. "
                                               "This List [] sign"
                                               "🤔If you don't understand the message information, you can look at the Video Information")
    await call.message.answer("<a href='https://youtu.be/OlSyO4O-GM8'>Yakin Kampus Derslerini Linke Tiklayarak Izleyebilirsiniz</a>", parse_mode=ParseMode.HTML)
    last_message_ids[call.message.chat.id] = message.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu5())

# @dp.callback_query(lambda call:call.data == "souma")
# async def souma_handler(call:types.CallbackQuery):
#     group_id = os.getenv("GROUP_ID")
#     await call.bot.copy_message(chat_id=call.message.chat.id,from_chat_id=group_id,message_id=866)
