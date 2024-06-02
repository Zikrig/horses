from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram import html


from keyboards.simple_row import make_row_keyboard

import table.table_people.work_with_bd as tpeople
import table.get_my_horse as tglob

router = Router()

def make_horse_text(horses):
    res = f'''Есть несколько подходящих лошадей:\n'''
    for horse in horses:
        res += f'''-------------------------------------------\n
{horse[1]} c конюшни {horse[6]} - {horse[5]} р\n
поднимает {horse[3]} кг и управляется {horse[4].lower()}\n
'''
    return res
     

@router.message(Command("gimme_horse"))
async def get_me(message: Message, state: FSMContext):
    tg_id=message.from_user.id
    me = tpeople.get_person_by_tg_id(tg_id)
    if me == None:
        await message.answer(
            text='Кажется мы не знакомы. Может, зарегистрируетесь /reg ?'
        )
    else:
        hrs = tglob.get_horses_by_id(tg_id)
        if hrs == None:
            await message.answer(
                text='Боюсь, у меня нет подходящих лошадей'
            )
        # print(r)
        else:
                await message.answer(
                    make_horse_text(hrs)
                )
        #     await message.answer(
        #         text=f'''
        # Вы успешно зарегистрированы!\n
        # Ваш id: {tg_id}\n
        # Имя:   {html.bold(me[2])}\n
        # Возраст:  {html.bold(me[3])}\n
        # Пол:      {html.bold(me[4])}\n
        # Ваш вес:   {html.bold(me[5])}\n
        # Опыт:     {html.bold(me[6])}\n
        # Сопровождающие:   {html.bold(me[7])}\n''',
                # parse_mode=ParseMode.HTML,
                # reply_markup=make_row_keyboard(available_food_names)
            # )