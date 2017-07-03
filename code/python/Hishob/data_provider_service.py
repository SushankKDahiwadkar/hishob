from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime

from models import User
from models import CashAccount
from models import init_database

class DataProviderService:
    def __init__(self, engine):
        if not engine:
            raise ValueError('The Values specified in engine parameter has to supported by SQlAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()
    
    def init_database(self):
        init_database(self.engine)
    
    def add_user(self, first_name, last_name, middle_name, user_name, email, mobile_number):
        new_user = User(first_name=first_name,
                        last_name=last_name,
                        middle_name=middle_name,
                        user_name=user_name,
                        email=email,
                        mobile_number=mobile_number)
    
        self.session.add(new_user)
        self.session.commit()
        return new_user.user_id

    def get_user(self, id=None, serialize=False):
        all_candidates = []
        if id is None:
            all_users = self.session.query(User).order_by(User.first_name).all()
        else:
            all_users = self.session.query(User).filter(User.user_id == id).all()
        
        if serialize:
            return [user.serialize() for user in all_users]
        else:
            return all_users
    
    def fill_database(self):
        user1 = User(first_name="first_name",
                        last_name="last_name",
                        middle_name="middle_name",
                        user_name="user_name",
                        email="email",
                        mobile_number=1212121212)
        
        user2 = User(first_name="first_name1",
                    last_name="last_name1",
                    middle_name="middle_name1",
                    user_name="user_name1",
                    email="email1",
                    mobile_number=1212121212)

        self.session.add(user1)
        self.session.add(user1)
        self.session.commit()