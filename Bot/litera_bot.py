from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from litera_keyboard import *
from litera_messages import *
from litera_config import *


bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def go(message):
    await message.answer(
        f'Привет, {message.from_user.username}! {start}',
        reply_markup=go_kb)


@dp.callback_query_handler(text='description')
async def descript(call):
    await call.message.answer(description, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='book')
async def descript_book(call):
    await call.message.answer(book, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='joyrnal')
async def descript_joyrnal(call):
    await call.message.answer(joyrnal, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='conference')
async def descript_conference(call):
    await call.message.answer(conference, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='newspaper')
async def descript_newspaper(call):
    await call.message.answer(newspaper, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='law')
async def descript_law(call):
    await call.message.answer(law, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='thesis')
async def descript_thesis(call):
    await call.message.answer(thesis, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='abstract')
async def descript_abstract(call):
    await call.message.answer(abstract, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='URL')
async def descript_url(call):
    await call.message.answer(URL, reply_markup=descrip_tip_litera_kb)
    await call.answer()


@dp.callback_query_handler(text='go')
async def start_inline(call):
    await call.message.answer('Выберите нужный вам тип:', reply_markup=tip_litera_kb)
    await call.answer()


@dp.message_handler(text='Начать')
async def start_keyboard(message):
    await message.answer('Выберите нужный вам тип:', reply_markup=tip_litera_kb)


@dp.message_handler(text='Книга')
async def set_author_book(message):
    await message.answer(book, reply_markup=kb_remove)
    await message.answer(author_)
    await BookState.author.set()


@dp.message_handler(state=BookState.author)
async def set_name_father_book(message, state):
    await state.update_data(author=message.text)
    await message.answer(name_father_)
    await BookState.name_father_Author.set()


@dp.message_handler(state=BookState.name_father_Author)
async def set_title_book(message, state):
    await state.update_data(name_father_Author=message.text)
    await message.answer(title_)
    await BookState.title.set()


@dp.message_handler(state=BookState.title)
async def set_publisher_book(message, state):
    await state.update_data(title=message.text)
    await message.answer(publisher_)
    await BookState.publisher.set()


@dp.message_handler(state=BookState.publisher)
async def set_city_book(message, state):
    await state.update_data(publisher=message.text)
    await message.answer(city_)
    await BookState.city.set()


@dp.message_handler(state=BookState.city)
async def set_year_book(message, state):
    await state.update_data(city=message.text)
    await message.answer(year_)
    await BookState.year.set()


@dp.message_handler(state=BookState.year)
async def set_pages_book(message, state):
    await state.update_data(year=message.text)
    await message.answer(pages_)
    await BookState.pages.set()


@dp.message_handler(state=BookState.pages)
async def book_finish(message, state):
    await state.update_data(pages=message.text)
    data = await state.get_data()
    author = data['author']
    name_father_Author = data['name_father_Author']
    title = data['title']
    publisher = data['publisher']
    city = data['city']
    year = data['year']
    pages = data['pages']
    await message.answer(f'{author}, {name_father_Author} {title} / {name_father_Author} {author}. — {city} : {publisher}, {year}. — {pages} с. — Текст : непосредственный')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать оформление вашего списка литературы')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
