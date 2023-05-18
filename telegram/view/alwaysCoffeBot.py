import os

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from telegram.control import vsegdaCoffeControl
from telegram.control.vsegdaCoffeControl import bot, dp
from aiogram import types
from telegram.models.client import client
from telegram.models.promoCode import promoCode


keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Да", "Нет"]
keyboard1.add(*buttons)

keyboard2 = types.InlineKeyboardMarkup
class Wait(StatesGroup):
    userId = State()
    name = State()
    info_for_user = State()
    choose_name = State()
    choose_info_for_user = State()
    register_user = State()
    getQr = State()


@dp.message_handler(commands=['start'], state="*")
async def start(message: types.Message, state: FSMContext):
    if message.chat.type == 'private':
        if not bool(client.ReturnInfoUser(message.from_user.id)):
            await state.update_data(userId=message.from_user.id)
            await bot.send_message(message.from_user.id, "Добро пожаловать! Желаете учавствовать в акции 5 + 1?",
                                   reply_markup=keyboard1)
            await Wait.name.set()
        else:
            await bot.send_message(message.from_user.id, "Добро пожаловать!")


@dp.message_handler(state=Wait.name)
async def choose_name(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await message.answer("Ваше имя?", reply_markup=types.ReplyKeyboardRemove())
        await Wait.choose_info_for_user.set()
    elif message.text != "Да" or "Нет":
        await message.answer("не понял 🤨")
        return
    else:
        pass


@dp.message_handler(state=Wait.choose_info_for_user)
async def choose_info_user(message: types.Message, state: FSMContext):
    if len(message.text) < 60:
        await state.update_data(name=message.text)
    else:
        await message.answer("Слишком длинное имя")
        return
    await message.answer("Желаете получать новости?", reply_markup=keyboard1)
    await Wait.register_user.set()


@dp.message_handler(state=Wait.register_user)
async def register_user(message: types.Message, state: FSMContext):
    if message.text == "Да":
        await state.update_data(info_for_user=True)
    elif message.text == "Нет":
        await state.update_data(info_for_user=False)
    data = await state.get_data()
    if not bool(client.ReturnInfoUser(message.from_user.id)):
        userInfo = list(data.values())
        userInfo = userInfo[0], userInfo[1], userInfo[2]
        client.createUser(userInfo)
        await getMyQrCode(message)


@dp.message_handler(commands=['myqr'])
async def getMyQrCode(message: types.Message):
    caption = client.ReturnInfoUser(message.from_user.id)
    caption = vsegdaCoffeControl.show_info_qr(caption.nameClient, caption.coffeCup)
    vsegdaCoffeControl.generateQR(message.from_user.id)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=open(f'D:/Programming/Python/MyProject/telegram/view/QrCode/{message.from_user.id}.jpg',
                                    'rb'), caption=caption, reply_markup=types.ReplyKeyboardRemove())
    os.remove(f'D:/Programming/Python/MyProject/telegram/view/QrCode/{message.from_user.id}.jpg')


async def getNewPromo(userId, code):
    await bot.send_message(chat_id=userId, text=f'Ваш промокод на кофе {code}')


@dp.message_handler(commands=['usepromo'])
async def usePromoCode(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 650690754:
            text = 'VSEGDA' + message.text[10:]
            if promoCode.RemovePromo(text) == True:
                await bot.send_message(chat_id=message.from_user.id, text='Промокод использован')
            else:
                await bot.send_message(chat_id=message.from_user.id, text='Промокода не существует')


@dp.message_handler(commands=['sendall'])
async def sendallMessage(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 650690754:
            text = message.text[9:]
            users = client.ReturnAllUsers()
            for u in users:
                await bot.send_message(chat_id=u.clientId, text=text)
            await bot.send_message(chat_id=message.from_user.id, text="Рассылка успешна!")


@dp.message_handler(commands=['sendnews'])
async def sendNewsMessage(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 650690754:
            text = message.text[10:]
            users = client.ReturnNewsUsers()
            for u in users:
                await bot.send_message(chat_id=u.clientId, text=text)
            await bot.send_message(chat_id=message.from_user.id, text='рассылка новостей успешна')

'''
@dp.message_handler(commands=['mypromo'])
async def getmypromo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=usercontrol.getPromo(message.from_user.id))
'''