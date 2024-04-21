from aiogram.filters.state import StatesGroup, State

class RegisterStates(StatesGroup):
    firstname = State()
    lastname = State()
    call = State()