from aiogram import Router, F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo

from keyboards.for_questions import get_yes_no_kb

router = Router()  


@router.message(Command("web"))
async  def webb(message: Message):
    urll = 'https://rpa-bot.ru/'
    web_appp=WebAppInfo(url=urll)
    open_button = KeyboardButton(text='hi', web_app=web_appp)

    # markup = ReplyKeyboardMarkup(keyboard=[open_button])
    
    # await message.answer('хеллоу', reply_markup=markup)

    await message.answer(
        text="Хеллоу",
        reply_markup=ReplyKeyboardMarkup(keyboard=[[open_button]])
    )
    # await message.answer(
    #     text="Я не знаю такого блюда.\n\n"
    #          "Пожалуйста, выберите одно из названий из списка ниже:",
    #     reply_markup=ReplyKeyboardMarkup(keyboard=open_button)
    #     # reply_markup=make_row_keyboard(available_food_names)
    # )