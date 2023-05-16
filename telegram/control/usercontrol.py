import asyncio
import random

import qrcode
from sqlalchemy.orm import Session as SqlSession

from telegram.models.client import client
from telegram.models.promoCode import promoCode
from telegram.models.vsegdaCoffeDb import Session


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


def createUser(userInfo, session: SqlSession = Session()):
    clientId = userInfo[0]
    nameClient = userInfo[1]
    coffeCup = 0
    sendNews = userInfo[2]
    user = client(clientId, nameClient, coffeCup, sendNews)
    try:
        session.add(user)
        session.commit()
        session.close()
    except:
        session.close()


def returnInfoUser(userId, session: SqlSession = Session()):
    try:
        user = session.query(client).filter(client.clientId == userId).first()
    except:
        session.close()

    if bool(user) == False:
        return bool(user)
    else:
        return user


def add_coffee(userId, coffeeCupAdd, session: SqlSession = Session()):
    try:
        user = session.query(client).filter(client.clientId == userId).first()
    except:
        session.close()
    user.coffeCup += coffeeCupAdd
    while user.coffeCup >= 5:
        print(user.coffeCup)
        user.coffeCup -= 5
        generatePromoCode(user.clientId)
        print(user.coffeCup)
    session.commit()


def generatePromoCode(userId, session: SqlSession = Session()):
    from telegram.view.alwaysCoffeBot import getNewPromo
    # user = returnInfoUser(userId)
    Code = f'VSEGDA-{random.randint(1000, 9999)}'
    try:
        promo = promoCode(Code, userId)
        session.add(promo)
        session.commit()
        session.close()
        print('че как')
        asyncio.run(getNewPromo(userId, Code))
    except:
        session.close()


def usePromo(promo, session: SqlSession = Session()):
    promo = 'VSEGDA-' + promo
    try:
        promocode = session.query(promoCode).filter(promoCode.promo == promo).first()
        session.delete(promocode)
        session.commit()
        session.close()
        return True
    except:
        return False


def returnAllUsers(session: SqlSession = Session()):
    try:
        allusers = session.query(client)
        return allusers
    except:
        return False


def getPromo(userId, session: SqlSession = Session()):
    text = 'Ваши промокоды\n'
    try:
        allpromo = session.query(promoCode).filter(promoCode.client == userId)
        for i in allpromo:
            text += f'{i.promo}\n'
    except:
        return False
    return text


def returnNewsUsers(session: SqlSession = Session()):
    try:
        newsUsers = session.query(client).filter(client.sendNews == True)
    except:
        return False
    return  newsUsers