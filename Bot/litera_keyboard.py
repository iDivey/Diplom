from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

kb_remove = ReplyKeyboardRemove()

tip_litera_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Книга'),
            KeyboardButton(text='Статья из журнала'),
            KeyboardButton(text='Статья из сборника конференции'),
            KeyboardButton(text='Статья из газеты'),
            KeyboardButton(text='Закон, нормативно-правовой акт и подобное'),
            KeyboardButton(text='Диссертация'),
            KeyboardButton(text='Автореферат'),
            KeyboardButton(text='Интернет-ресурс, электороное издание и т.д.')
        ]
    ], resize_keyboard=True, row_width=4)


descrip_tip_litera_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Книга', callback_data='book')],
        [InlineKeyboardButton(text='Статья из журнала', callback_data='joyrnal')],
        [InlineKeyboardButton(text='Статья из сборника конференции', callback_data='conference')],
        [InlineKeyboardButton(text='Статья из газеты', callback_data='newspaper')],
        [InlineKeyboardButton(text='Закон, нормативно-правовой акт и подобное', callback_data='law')],
        [InlineKeyboardButton(text='Диссертация', callback_data='thesis')],
        [InlineKeyboardButton(text='Автореферат', callback_data='abstract')],
        [InlineKeyboardButton(text='Интернет-ресурс, электороное издание и т.д.', callback_data='URL')],
        [InlineKeyboardButton(text='Начать', callback_data='go')]
    ]
)


years_litera_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Редакция 2008 года'),
            KeyboardButton(text='Редакция 2018 года'),
            KeyboardButton(text='Редакция 2018 года с учетом ГОСТ 7.0.80 2023 года')
        ]
    ], resize_keyboard=True)


go_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Описание', callback_data='description')],
        [InlineKeyboardButton(text='Начать', callback_data='go')]
    ]
)
