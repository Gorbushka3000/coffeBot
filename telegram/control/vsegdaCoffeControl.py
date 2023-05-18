from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import random
import qrcode
from telegram.models.promoCode import promoCode

bot = Bot(token='6288334700:AAHpfIPLIkDlYwCGGxCJGJMMUIPDK2j50Jc')
dp = Dispatcher(bot, storage=MemoryStorage())


def show_info_qr(name, coffeCup):
    return f'Здравствуйте {name}! Это ваш QR код. Предъявите его при оплате\nУ вас насчитано {coffeCup} кружек кофе'


def generateQR(UserId):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f'http://192.168.1.54:5002/{UserId}')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'D:/Programming/Python/MyProject/telegram/view/QrCode/{UserId}.jpg')


def generatePromoCode(userId):
    from telegram.view.alwaysCoffeBot import getNewPromo
    code = f'VSEGDA-{random.randint(1000, 9999)}'
    promoCode.addPromoCode(userId, code)
    asyncio.run(getNewPromo(userId, code))
