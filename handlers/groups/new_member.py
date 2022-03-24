from aiogram import types
from aiogram.types import ContentTypes

from filters import Guruh

# Echo bot
from loader import dp


@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism =message.new_chat_members[0].first_name
    await message.answer(text=f"Assalom alaykum {ism} guruxga xush kelibsiz ")
    await message.delete()

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.username
    user_id = message.left_chat_member.id
    message_id =message.message_id
    await message.answer(text=f"{ism} Guruxni tark etdi")
    await message.delete()
