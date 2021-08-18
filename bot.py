import logging
from aiogram import Bot, Dispatcher, executor, types

from checkWord import checkWord


API_TOKEN = 'Bot-Token'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    
    await message.reply(f"<b>Assalomu alaykum {message.from_user.first_name} \nBizni tanlaganingiz uchun raxmat 😊\nimlo_uzb Botiga Xush Kelibsiz!</b> ",parse_mode='HTML')

@dp.message_handler(commands='help')
async def help_user(message: types.Message):
    await message.reply(f"<b>{message.from_user.first_name} \nBotdan foydalanish uchun so'z yuboring. \nXozircha faqat kirilcha so'zlar mavjud </b>😊 ",parse_mode='HTML')


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

            

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)