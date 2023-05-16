from sqlalchemy import Column, Integer, String, Text, Boolean
from telegram.models.vsegdaCoffeDb import Base
from sqlalchemy.orm import relationship


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
