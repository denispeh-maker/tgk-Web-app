import asyncio
from aiogram import Bot, Dispatcher, types, F

from aiogram.types import Message
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command


dp = Dispatcher()

bot = Bot(token='8335517289:AAE-VK6UsaFgoZWtIyNQQUbfBTtnyQJKAIE')



# --- Inline клавіатура ---
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Site", url="https://altseting-token.vercel.app/")],
        [InlineKeyboardButton(text="Натисни мене", callback_data="btn1")]
    ]
)


# --- Обробка команд /start та /help ---
@dp.message(Command(commands=["start", "help"]))
async def cmd_start(message: Message):
    await message.answer("А тут inline-кнопки 👇", reply_markup=inline_kb)


# --- Обробка callback від inline-кнопок ---
@dp.callback_query(F.data == "btn1")
async def process_callback(callback: types.CallbackQuery):
    await callback.answer("Ти натиснув inline-кнопку!")












async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())