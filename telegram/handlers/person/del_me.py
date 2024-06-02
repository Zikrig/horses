from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from aiogram import html

from re import fullmatch

from keyboards.simple_row import make_row_keyboard

# from telegram.table import table_horse, table_horsehouse, table_people
import table.table_people.work_with_bd as tpeople

router = Router()


@router.message(Command("del_me"))
async def cmd_your_name(message: Message, state: FSMContext):
    tg_id=message.from_user.id
    tpeople.delete_person(tg_id)
    tpeople.get_person_by_tg_id(tg_id)
    # print(r)
    await message.answer(
        text="Ваш аккаунт был успешно удален",
        # reply_markup=make_row_keyboard(available_food_names)
    )
