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
import table.table_horse.work_with_bd as thorse
import table.table_horsehouse.work_with_bd as thorsehouse

router = Router()

# Эти значения далее будут подставляться в итоговый текст, отсюда
# такая на первый взгляд странная форма прилагательных
available_gender = ['Мужской', 'Женский']
available_exp = ['Меньше месяца', 'Менее полугода', 'Больше полугода']
available_esc = ['Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих']
# res = {
#     'tg_id': 0,
#     'name': '',
#     'age': '',
#     'gender': '',
#     'weight': '',
#     'exp': '',
#     'escort': ''
# }

def check_name(name):
    if(len(name) > 100):
        return False
    if(fullmatch(r'[а-яА-ЯёЁa-zA-Z\s\-]+',name)):
        return True
    return False

def check_age(age):
    if(not fullmatch(r'[\d \-]*',age)):
        return False
    if(int(age) > 110 or int(age) < 5):
        return False
    return True

def check_weight(weight):
    if(not fullmatch(r'[\d \-]*',weight)):
        return False
    if(int(weight) > 130 or int(weight) < 20):
        return False
    return True


class RegisterMe(StatesGroup):
    choosing_name = State()
    choosing_age = State()
    choosing_gender = State()
    choosing_weight = State()
    choosing_exp = State()
    choosing_escort = State()


@router.message(Command("alt"))
async def cmd_your_name(message: Message, state: FSMContext):
    await state.update_data(mode='alt')
    tg_id=message.from_user.id
    r = tpeople.get_person_by_tg_id(tg_id)
    if r == None:
        await message.answer(
        text="Вы еще не зарегестрированы. Попробуйте зарегистрироваться командой /reg ",
        )
    else:
        await message.answer(
            text="Как вас зовут?",
        )
        await state.set_state(RegisterMe.choosing_name)

@router.message(Command("reg"))
async def cmd_your_name(message: Message, state: FSMContext):
    await state.update_data(mode='reg')
    tg_id=message.from_user.id
    r = tpeople.get_person_by_tg_id(tg_id)
    if r != None:
        await message.answer(
        text="Вы уже зарегестрированы. Попробуйте изменить анкету командой /alt",
        )
    else:
        await message.answer(
            text="Как вас зовут?",
        )
        await state.set_state(RegisterMe.choosing_name)

# Этап выбора блюда #


@router.message(RegisterMe.choosing_name, lambda message: check_name(message.text))
async def name_chosen(message: Message, state: FSMContext):
    await state.update_data(name=message.text.capitalize())
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, укажите ваш возраст:",
        # reply_markup=make_row_keyboard(available_food_sizes)
    )
    await state.set_state(RegisterMe.choosing_age)


# В целом, никто не мешает указывать стейты полностью строками
# Это может пригодиться, если по какой-то причине 
# ваши названия стейтов генерируются в рантайме (но зачем?)
@router.message(StateFilter("RegisterMe:choosing_name"))
async def name_chosen_incorrectly(message: Message):
    print('Имя указано некорректно')
    await message.answer(
        text="Похоже, вы ввели имя длиннее 100 символов, или что-то кроме букв.\n\n"
             "Пожалуйста, укажите ваше имя, чтобы мы могли с вами связаться:",
        # reply_markup=make_row_keyboard(available_food_names)
    )
@router.message(RegisterMe.choosing_age, lambda message: check_age(message.text))
async def age_chosen(message: Message, state: FSMContext):
    await state.update_data(age=int(message.text.capitalize()))
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, укажите ваш пол:",
        reply_markup=make_row_keyboard(available_gender)
    )
    await state.set_state(RegisterMe.choosing_gender)

@router.message(RegisterMe.choosing_age)
async def age_chosen_incorrectly(message: Message):
    # print('Возраст указан некорректно')
    await message.answer(
        text="Вам должно быть от 4 до 110 лет, пожалуйста, укажите возраст.",
        # reply_markup=make_row_keyboard(available_food_sizes)
    )

@router.message(RegisterMe.choosing_gender, F.text.in_(available_gender))
async def gender_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.update_data(gender=message.text.capitalize())
    await message.answer(
        text=f"Отлично. Теперь пожалуйста укажите ваш вес\n",
        reply_markup=ReplyKeyboardRemove()
    )
    # Сброс состояния и сохранённых данных у пользователя
    await state.set_state(RegisterMe.choosing_weight)

@router.message(RegisterMe.choosing_gender)
async def gender_chosen_incorrectly(message: Message, state: FSMContext):
    # user_data = await state.get_data()
    await message.answer(
        text=f"Пожалуйста, выберете один из двух гендеров",
        reply_markup=make_row_keyboard(available_gender)
    )

@router.message(RegisterMe.choosing_weight,lambda message: check_weight(message.text))
async def weight_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.update_data(weight=message.text.capitalize())
    await message.answer(
        # text=f"Вас зовут {user_data['name']} и вам {user_data['age']} лет. \nВаш пол {user_data['gender']}\n Ваш вес {message.text.capitalize()}\n",
        text="Отлично! Пожалуйста, выберите укажите ваш опыт.",
       reply_markup=make_row_keyboard(available_exp)
    )
    await state.set_state(RegisterMe.choosing_exp)
    # Сброс состояния и сохранённых данных у пользователя
    # await state.clear()

@router.message(RegisterMe.choosing_weight)
async def weight_chosen_incorrectly(message: Message, state: FSMContext):
    # user_data = await state.get_data()
    await message.answer(
        text=f"Пожалуйста, выберете вес от 20 до 130",
        # reply_markup=make_row_keyboard(available_gender)
    )

@router.message(RegisterMe.choosing_exp, F.text.in_(available_exp))
async def exp_chosen(message: Message, state: FSMContext):
    await state.update_data(exp=message.text.capitalize())
    await message.answer(
        text="Спасибо. Теперь, пожалуйста, выбрите, сколько вам нужно сопровождающих:",
        reply_markup=make_row_keyboard(available_esc)
    )
    await state.set_state(RegisterMe.choosing_escort)

@router.message(RegisterMe.choosing_exp)
async def exp_chosen_incorrectly(message: Message):
    # print('Возраст указан некорректно')
    await message.answer(
        text="Пожалуйста, выберите вариант из списка",
        reply_markup=make_row_keyboard(available_exp)
    )

@router.message(RegisterMe.choosing_escort, F.text.in_(available_esc))
async def exp_chosen(message: Message, state: FSMContext):
    await state.update_data(esc=message.text.capitalize())
    await state.update_data(tg_id=message.from_user.id)
    user_data = await state.get_data()
    tg_id = message.from_user.id
    esc = message.text.capitalize()
    await message.answer(
        text=f'''
Вы успешно зарегистрированы!\n
Ваш id: {tg_id}\n
Имя:   {html.bold(user_data['name'])}\n
Возраст:  {html.bold(user_data['age'])}\n
Пол:      {html.bold(user_data['gender'])}\n
Ваш вес:   {html.bold(user_data["weight"])}\n
Опыт:     {html.bold(user_data['exp'])}\n
Сопровождающие:   {html.bold(esc)}\n''',
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove()
    )
    if(user_data['mode'] == 'reg'):
        tpeople.add_person(
            tg_id,
            user_data['name'],
            user_data['age'],
            user_data['gender'],
            user_data['weight'],
            user_data['exp'],
            esc)
    else:
        tpeople.alt_person(
            tg_id,
            user_data['name'],
            user_data['age'],
            user_data['gender'],
            user_data['weight'],
            user_data['exp'],
            esc)
    await state.clear()

@router.message(RegisterMe.choosing_escort)
async def exp_chosen_incorrectly(message: Message):
    # print('Возраст указан некорректно')
    await message.answer(
        text="Пожалуйста, выберите вариант из списка",
        reply_markup=make_row_keyboard(available_esc)
    )