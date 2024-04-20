from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
