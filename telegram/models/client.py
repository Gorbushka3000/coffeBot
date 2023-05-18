from sqlalchemy import Column, Integer, String, Text, Boolean
from telegram.models.vsegdaCoffeDb import Base
from sqlalchemy.orm import relationship
from telegram.models.vsegdaCoffeDb import Session
from sqlalchemy.orm import Session as SqlSession

class client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    clientId = Column(Integer)
    nameClient = Column(String)
    coffeCup = Column(Integer)
    sendNews = Column(Boolean)
    promoCodes = relationship('promoCode', backref='promoCode')

    def __init__(self, client, nameClient, coffeCup, sendNews):
        self.clientId = client
        self.nameClient = nameClient
        self.coffeCup = coffeCup
        self.sendNews = sendNews

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

    def ReturnInfoUser(userId, session: SqlSession = Session()):
        try:
            user = session.query(client).filter(client.clientId == userId).first()
        except:
            session.close()

        if bool(user) == False:
            return bool(user)
        else:
            return user

    def ReturnAllUsers(session: SqlSession = Session()):
        try:
            allusers = session.query(client)
            return allusers
        except:
            return False

    def returnNewsUsers(session: SqlSession = Session()):
        try:
            newsUsers = session.query(client).filter(client.sendNews == True)
        except:
            return False
        return newsUsers

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