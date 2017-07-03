from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from Model import Model

class CashAccount(Model):
    __tablename__ = 'cash_account'
    uuid = Column(String(40), nullable=True)
    cash_account_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)    
    
    #reference for User.user_id
    user_id = Column(Integer, ForeignKey('user.user_id'))
    