from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import asyncio, os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
r = Router(); dp.include_router(r)

@r.message(CommandStart())
async def start(m):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🚀 Launch App",
            web_app=WebAppInfo(url="https://denispeh-maker.github.io/tgk-Web-app/")  # твій Pages-URL
        )
    ]])
    await m.answer("Відкрий WebApp:", reply_markup=kb)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
