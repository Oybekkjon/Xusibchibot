from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.Guruxga_qoshish import inline_uz



from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}bu bot guruxingizga qo'shib admin qilsangiz guruxingizdagi kirdi chiqtini nazort qiladi!",reply_markup=inline_uz)
