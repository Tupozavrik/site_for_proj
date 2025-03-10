import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command

# Используйте свой токен бота
bot = Bot('7736606067:AAH15fIuJvJXx12oDxFF-jnYlLmk7DdNt4U')
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    keyboard = [
        [KeyboardButton(text='Открыть веб страницу', web_app=WebAppInfo(url='https://tupozavrik.github.io/site_for_proj/'))]
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer('Добро пожаловать в игру Mindgame! Нажмите на кнопку ниже, чтобы сыграть.', reply_markup=markup)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
