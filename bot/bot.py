from colorama import Fore  # для изменения цвета в консоли
from aiogram import Bot , types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor
from config import TOKEN
from parserCart import parse_videocart

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello")


@dp.message_handler(commands=['videocart'])
async def process_video_command(message: types.Message):
    video_cart = message.text.split()[1]
    await bot.send_message(message.from_user.id , parse_videocart(video_cart))


print(Fore.LIGHTYELLOW_EX + "Bot started!")

if __name__ == '__main__':
    executor.start_polling(dp)
