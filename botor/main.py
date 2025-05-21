import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from botor.static import(
  ABOUT_US,
  ADDRESS,
  COURSE,
  CONTACT,
  My_CONTACT,
  MY_LOCATION,ANSWER,FAQ,ANSWER_2,ANSWER_3,ANSWER_4,ANSWER_5,TELEGRAPH_LINK,QUESTION
)
load_dotenv()
# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")


dp = Dispatcher()




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [
            KeyboardButton(text=ABOUT_US),
            KeyboardButton(text=ADDRESS),
            KeyboardButton(text=CONTACT),
            KeyboardButton(text=COURSE),

        ],
        [
            KeyboardButton(text=My_CONTACT,request_contact=True),
            KeyboardButton(text=MY_LOCATION,request_location=True)
        ],
        [
           KeyboardButton(text=FAQ)
        ]



    ])
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard)

@dp.message(F.text == ABOUT_US)
async  def about_us(message:Message):
     file_id ='AgACAgIAAxkBAVmz62d-nh-ymfRuMWE9wxjjCp-73YbIAALF6DEbiPL5S5O9tmeAmHHFAQADAgADcwADNgQ'

     await message.answer_photo(photo=file_id, caption='Biz ziyo school maktabida IT sohasini o`rgatamiz')


@dp.message(F.text == ADDRESS)
async def about_us(message:Message):
    Latitude=41.409436
    Longitude=69.307917
    await message.answer_location(latitude=Latitude,longitude=Longitude)
    await message.answer('ziyo o`quv markazi')


@dp.message(F.location)
async def handle_location(message:Message):
    lat ,long=message.location.latitude,message.location.longitude
    await (f"{lat},{long}")



@dp.message(F.text == CONTACT)
async def about_num(message:Message):
    contact='+998882909709'
    await message.answer_contact(phone_number=contact,first_name='Admin',last_name='Asil')


@dp.message(F.text == COURSE)
async def send_coourse_data(message:Message):
    filem_id='AgACAgIAAxkBAVmzAmd-mEM485XnB4Jvmv9ke9ix6-cqAAKP6DEbiPL5SxS29AuSeg9NAQADAgADcwADNgQ'
    keybooard=InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Telegram',url='https://t.me/@ziyo_school'),
            InlineKeyboardButton(text='Instagram',url='https://instagram.com/@ziyo_school')
        ]
    ])
    await message.answer_photo(photo=filem_id,caption='ziyo school kurslari!',reply_markup=keybooard)



@dp.message(F.contact | F.location)
async  def about_us(message:Message):
   await message.answer('👍️️️️Qabul qilindi rahmat!')


@dp.message(F.text == FAQ)
async def send_faq(message:Message):
    await message.answer(text=QUESTION)
    await message.answer(text=TELEGRAPH_LINK)

@dp.message(Command("quiz_1"))
async def send_answer_one(message:Message):
    await  message.answer(text=ANSWER)

@dp.message(Command("quiz_2"))
async def send_answer_one(message: Message):
        await  message.answer(text=ANSWER_2)
@dp.message(Command("quiz_3"))
async def send_answer_one(message:Message):
    await  message.answer(text=ANSWER_3)
@dp.message(Command("quiz_4"))
async def send_answer_one(message:Message):
    await  message.answer(text=ANSWER_4)
@dp.message(Command("quiz_5"))
async def send_answer_one(message:Message):
    await  message.answer(text=ANSWER_5)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())