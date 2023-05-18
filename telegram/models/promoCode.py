from sqlalchemy import Column, Integer, String, ForeignKey
from telegram.models.vsegdaCoffeDb import Base
from telegram.models.vsegdaCoffeDb import Session
from sqlalchemy.orm import Session as SqlSession


class promoCode(Base):
    __tablename__ = 'promoCode'

    id = Column(Integer, primary_key=True)
    promo = Column(String)
    client = Column(Integer, ForeignKey('client.clientId'))

    def __init__(self, promo, client):
        self.promo = promo
        self.client = int(client)

    def AddPromoCode(userId, code, session: SqlSession = Session()):
        try:
            promo = promoCode(code, userId)
            session.add(promo)
            session.commit()
            session.close()
        except:
            session.close()

    def RemovePromo(promo, session: SqlSession = Session()):
        try:
            promocode = session.query(promoCode).filter(promoCode.promo == promo).first()
            session.delete(promocode)
            session.commit()
            session.close()
            return True
        except:
            return False

    def GetPromo(userId, session: SqlSession = Session()):
        try:
            allpromo = session.query(promoCode).filter(promoCode.client == userId)
        except:
            return False
        return allpromo