from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
import hw_lesson16.db as db
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


from hw_lesson16.model import Base

#Base = declarative_base()
class Schet(Base):
    __tablename__ = 'schet'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)
    id_account = Column(Integer, ForeignKey('bankaccount.id'))
    account = relationship('Bankaccount', back_populates='schet')
    schet = relationship('History', back_populates='history_sc')


    def __repr__(self):
        return f'{self.id} ----- {self.balance} --'

def create_schet():
    db.configurate_engine()
    with Session(autoflush=False, bind=db.engine) as session:
        schet_Sergey_R = Schet(name='RUB', balance=120, id_account=1)
        schet_Sergey_E = Schet(name='EUR', balance=320, id_account=1)
        schet_Vadim_R = Schet(name='RUB', balance=100, id_account=2)
        schet_Vadim_E = Schet(name='EUR', balance=400, id_account=2)
        schet_Vadim_U = Schet(name='USD', balance=500, id_account=2)
        session.add(schet_Sergey_R)
        session.add(schet_Sergey_E)
        session.add(schet_Vadim_R)
        session.add(schet_Vadim_E)
        session.add(schet_Vadim_U)
        session.commit()