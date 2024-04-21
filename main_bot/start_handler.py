from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types.bot_command import BotCommand
from buttons.inline_keyboar import menu_btn, menu
from DB.Db import PG
from aiogram.fsm.context import FSMContext
from states.state import RegisterStates
from buttons.reply_keyboard import types_btn

dp = Dispatcher()



@dp.message(CommandStart())
async def start_handler(msg: types.Message,state:FSMContext):
    obj = PG()
    full_name = msg.from_user.full_name
    user_id = msg.from_user.id
    if obj.checked_user(user_id):
        await msg.answer(f"*Hello {full_name} Welcome to my bot you can learn what you don't know in python with this bot*\n"
        "\n"
        '*Enter Your Name*',parse_mode='Markdown')
        await state.set_state(RegisterStates.lastname)
    else:await msg.answer(text = "*You are already registered*",parse_mode='Markdown')
@dp.message(RegisterStates.lastname)
async def last_name_handler(msg: types.Message,state:FSMContext):
    lastname = msg.text
    await state.update_data(lastname=lastname)
    await state.set_state(RegisterStates.firstname)
    await msg.answer("Enter Your LastName",parse_mode='Markdown')

@dp.message(RegisterStates.firstname)
async def firstname_handler(msg: types.Message,state:FSMContext):
    obj = PG()
    firstname = msg.text
    await state.update_data(firstname=firstname)
    data = await state.get_data()
    lastname = data.get('lastname')
    firstname = data.get('firstname')
    user_id = msg.from_user.id
    obj.add(user_id,lastname,firstname)
    await msg.answer("Successfully registered",parse_mode='Markdown')
types_command = BotCommand(command = "types",description="Python Types")
@dp.message(Command(types_command))
async def types_command(msg:types.Message):

    await msg.answer(text = 'Select Your Type',reply_markup=menu_btn())

last_message_ids = { }
@dp.callback_query(lambda call:call.data == "string")
async def string_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_messages(call.message.chat.id, last_message_ids[call.message.chat.id])
    messages = await call.message.answer(text = "String Button Selected",parse_mode="Markdown")
    last_message_ids[call.message.chat.id] = messages.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu())

@dp.callback_query(lambda call:call.data == "integer")
async def integer_handler(call:types.CallbackQuery):
    if call.message.chat.id in last_message_ids:
        await call.bot.delete_messages(call.message.chat.id, last_message_ids[call.message.chat.id])
    messages = await call.message.answer(text = "Integer Button Selected",parse_mode="Markdown")
    last_message_ids[call.message.chat.id] = messages.message_id
    await call.bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=call.message.message_id,reply_markup=menu1())
