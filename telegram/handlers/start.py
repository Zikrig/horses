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


@router.message(Command("help", "start"))
async def cmd_start(message: Message, state: FSMContext):
    # print(r)
    await message.answer(
        text='''Привет!\nСейчас я поддерживаю такие команды, помимо /help:\n
/reg чтобы заполнить анкету\n
/alt чтобы изменить анкету\n
/del_me чтобы удалить анкету\n 
/gimme чтобы вывести свои данные\n
/gimme_horse чтобы получить список подходящих лошадей\n
Не забудьте, что вы можете получить список команд по команде /help !
''',
    )