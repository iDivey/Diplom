from aiogram.dispatcher.filters.state import State, StatesGroup
API = ''


class BookState(StatesGroup):
    author = State()
    name_father_Author = State()
    title = State()
    publisher = State()
    city = State()
    year = State()
    pages = State()
