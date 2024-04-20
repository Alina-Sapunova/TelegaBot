from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton  # для клавиатуры пользователя
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton  # онлайн кнопочки

TOKEN = '7104176976:AAEYebrJlRY13xGBOPWApKLdXTTZrqH005s'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def starting(message: types.Message):
    sp_buttons = [
        [
            types.KeyboardButton(text='Давай начнём'),
            types.KeyboardButton(text='Нет, спасибо')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=sp_buttons)

    await message.reply('Привет!\nЯ SurpriseBot\nПомогу тебе с выбором подарка на праздник!',
                        reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def helping(message: types.Message):
    await message.reply('Напиши мне одну из команд...ляляляля')


@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    links_button = InlineKeyboardMarkup(row_width=1)
    button_pozdravok = InlineKeyboardButton(text='Перейти на сайт <Поздравок>',
                                            url='https://pozdravok.com/pozdravleniya/den-rozhdeniya/')
    button_kartinki = InlineKeyboardButton(text='Перейти на сайт <Открытки>',
                                           url='https://yandex.ru/images/search?from=tabbar&text=%D0%BF%D0%BE%D0%B7%D0%B4%D1%80%D0%B0%D0%B2%D0%BE%D0%BA')
    links_button.add(button_pozdravok, button_kartinki)

    await message.answer('Полезные ссылки:', reply_markup=links_button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
