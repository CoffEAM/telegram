import sqlite3
from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bd import get_profiles
router = Router()


class ClassState(StatesGroup):
    class_selection = State()
    profile_selection = State()
    day_selection = State()
    symbol_selection = State()
    symbol_selection_56 = State()


@router.message(Command("start"))
async def process_command_1(message: types.Message):
    await message.reply("Привет! Для того, чтобы узнать своё расписание, выполни следующие действия:")
    inline_kb1 = InlineKeyboardBuilder()
    text_btn = 4
    btn_callback = 4
    for index in range(5, 12):
        text_btn += 1
        btn_callback += 1
        if index == 11:
            inline_kb1.button(text=f"{text_btn}-й класс💤", callback_data=f"{btn_callback}")
        else:
            inline_kb1.button(text=f"{text_btn}-й класс", callback_data=f"{btn_callback}")
    inline_kb1.adjust(2, 2)
    await message.answer("Выбери класс, в котором ты учишься", reply_markup=inline_kb1.as_markup())


@router.callback_query()
async def process_callback_1(query: types.CallbackQuery, state: FSMContext):
    clicked_button = query.data

    if clicked_button == '10':
        await query.message.edit_text('Выбери профиль, в котором ты обучаешься')
        await state.set_state(ClassState.profile_selection.state)
        await updated_inline_keyboard_1(query, 10, state)
    elif clicked_button in ['7', '8', '9']:
        await query.message.edit_text('Выбери букву класса')
        await state.set_state(ClassState.symbol_selection.state)
        await select_symbol_of_class(query, state)
    elif clicked_button in ['5', '6']:
        await query.message.edit_text('Выбери букву класса')
        await state.set_state(ClassState.symbol_selection_56.state)
        await select_symbol_of_class_e(query, state)
    elif clicked_button in ['a', 'b', 'v', 'g', 'd', 'e', 'Физ/мат', 'Инфо/тех', 'Хим/био', 'Соц/гум', 'Соц/эко']:
        await query.message.edit_text('Выбери день недели🗓')
        await state.set_state(ClassState.day_selection.state)
        await select_day_of_week(query, state)
    print(clicked_button)

    if clicked_button == 'back':
        await updated_inline_keyboard(query, state)


async def updated_inline_keyboard(callback: types.CallbackQuery, state: FSMContext):
    inline_kb1 = InlineKeyboardBuilder()
    text_btn, btn_callback = 4, 4
    for index in range(5, 12):
        text_btn += 1
        btn_callback += 1
        if index == 11:
            inline_kb1.button(text=f"{text_btn}-й класс💤", callback_data=f"{btn_callback}")
        else:
            inline_kb1.button(text=f"{text_btn}-й класс", callback_data=f"{btn_callback}")
    inline_kb1.adjust(2, 2)

    await callback.message.edit_text("Выбери класс, в котором ты учишься")
    await callback.message.edit_reply_markup(reply_markup=inline_kb1.as_markup())
    await state.set_state(ClassState.class_selection.state)


async def updated_inline_keyboard_1(callback: types.CallbackQuery, class_name: int, state: FSMContext):
    inline_kb2 = InlineKeyboardBuilder()
    profiles = get_profiles(class_name)
    s = ['👨‍🏭', '🧑‍💻', '👩‍🔬', '👩‍🏫', '👨‍🎤']
    for i in range(5):
        inline_kb2.button(text=f"{profiles[i] + s[i]}", callback_data=f"{profiles[i]}")
    inline_kb2.button(text=f"Назад◀️", callback_data=f"back")
    inline_kb2.adjust(3, 2)

    await callback.message.edit_reply_markup(reply_markup=inline_kb2.as_markup())
    await state.set_state(ClassState.profile_selection.state)


async def select_symbol_of_class(callback: types.CallbackQuery, state: FSMContext):
    inline_kb = InlineKeyboardBuilder()
    s1 = ['А', 'Б', 'В', 'Г', 'Д']
    s2 = ['a', 'b', 'v', 'g', 'd']
    for i in range(5):
        inline_kb.button(text=s1[i], callback_data=s2[i])
    inline_kb.button(text=f"Назад◀️", callback_data=f"back")
    inline_kb.adjust(5, 1)

    await callback.message.edit_reply_markup(reply_markup=inline_kb.as_markup())
    await state.set_state(ClassState.symbol_selection.state)


async def select_symbol_of_class_e(callback: types.CallbackQuery, state: FSMContext):
    inline_kb = InlineKeyboardBuilder()
    s1 = ['А', 'Б', 'В', 'Г', 'Д', 'Е']
    s2 = ['a', 'b', 'v', 'g', 'd', 'e']
    for i in range(6):
        inline_kb.button(text=s1[i], callback_data=s2[i])
    inline_kb.button(text=f"Назад◀️", callback_data=f"back")
    inline_kb.adjust(6, 1)

    await callback.message.edit_reply_markup(reply_markup=inline_kb.as_markup())
    await state.set_state(ClassState.symbol_selection_56)


async def select_day_of_week(callback: types.CallbackQuery, state: FSMContext):
    inline_kb = InlineKeyboardBuilder()
    inline_kb.button(text="Понедельник", callback_data="monday")
    inline_kb.button(text="Вторник", callback_data="tuesday")
    inline_kb.button(text="Среда", callback_data="wednesday")
    inline_kb.button(text="Четверг", callback_data="thursday")
    inline_kb.button(text="Пятница", callback_data="friday")
    inline_kb.button(text="Суббота", callback_data="saturday")
    inline_kb.button(text=f"Назад◀️", callback_data=f"back")
    inline_kb.adjust(3, 3, 1)

    await callback.message.edit_reply_markup(reply_markup=inline_kb.as_markup())
    await state.set_state(ClassState.day_selection.state)









