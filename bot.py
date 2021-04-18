from aiogram import Bot , types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from config import TOKEN  # bot token
from parserCart import parse_videocart
from parserCart import r

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello! type /help for more information.")


@dp.message_handler(commands=['help'])
async def help_message(message: types.message):
    await message.reply("Type /s [GPU name] ")


@dp.message_handler(commands=['s'])
async def process_video_command(message: types.Message):
    video_cart = message.text.split()[1]
    await bot.send_message(message.from_user.id , parse_videocart(video_cart))


print("Status code = ", r.status_code)
print("Bot started!")

if __name__ == '__main__':
    executor.start_polling(dp)
