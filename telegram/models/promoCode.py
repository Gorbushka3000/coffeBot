from sqlalchemy import Column, Integer, String, ForeignKey
from telegram.models.vsegdaCoffeDb import Base


class promoCode(Base):
    __tablename__ = 'promoCode'

    id = Column(Integer, primary_key=True)
    promo = Column(String)
    client = Column(Integer, ForeignKey('client.clientId'))

    def __init__(self, promo, client):
        self.promo = promo
        self.client = int(client)
