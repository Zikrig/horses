from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram import html


from keyboards.simple_row import make_row_keyboard

# from telegram.table import table_horse, table_horsehouse, table_people
import table.table_people.work_with_bd as tpeople

router = Router()


@router.message(Command("gimme"))
async def get_me(message: Message, state: FSMContext):
    tg_id=message.from_user.id
    me = tpeople.get_person_by_tg_id(tg_id)
    if me == None:
        await message.answer(
            text='Кажется мы не знакомы. Может, зарегистрируетесь /reg ?'
        )
    # print(r)
    else:
        await message.answer(
            text=f'''
    Вы успешно зарегистрированы!\n
    Ваш id: {tg_id}\n
    Имя:   {html.bold(me[2])}\n
    Возраст:  {html.bold(me[3])}\n
    Пол:      {html.bold(me[4])}\n
    Ваш вес:   {html.bold(me[5])}\n
    Опыт:     {html.bold(me[6])}\n
    Сопровождающие:   {html.bold(me[7])}\n''',
            parse_mode=ParseMode.HTML,
            # reply_markup=make_row_keyboard(available_food_names)
        )