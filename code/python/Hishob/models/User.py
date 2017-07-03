from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class User(Model):
    __tablename__ = 'user'
    uuid = Column(String(40), nullable=True)
    user_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    middle_name = Column(String(50), nullable=True)
    user_name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False)
    mobile_number = Column(Integer, nullable=True)
    password = Column(String(40), nullable=True)
    cash_accounts = relationship('CashAccount')

    def serialize(self):
        return {
            "uuid" : self.uuid,
            "user_id" : self.user_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "middle_name" : self.middle_name,
            "user_name" : self.user_name,
            "email" : self.email,
            "mobile_number" : self.mobile_number
        }
        