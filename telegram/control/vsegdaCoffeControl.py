from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='6288334700:AAHpfIPLIkDlYwCGGxCJGJMMUIPDK2j50Jc')
dp = Dispatcher(bot, storage=MemoryStorage())

def show_info_qr(name, coffeCup):
    return f'Здравствуйте {name}! Это ваш QR код. Предъявите его при оплате\nУ вас насчитано {coffeCup} кружек кофе'
