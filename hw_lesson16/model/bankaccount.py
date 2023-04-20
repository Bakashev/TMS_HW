from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
import hw_lesson16.db as db
import hw_lesson16.model.schet as schet
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


from hw_lesson16.model import Base

#Base = declarative_base()
class Bankaccount(Base):
    __tablename__ = 'bankaccount'

    id= Column(Integer, primary_key=True)
    name_account = Column(String)
    schet = relationship('Schet',back_populates='account')


    def __repr__(self):
        return f'{self.id} ----- {self.name_account} --'

#создаем аккаунты
def create_account():
    with Session(autoflush=False, bind=db.engine) as session:
        acc_one = Bankaccount(name_account='Sergey')
        acc_two = Bankaccount(name_account='Vadim')
        print()
        #schet_ = schet.Schet(balance=number, id_account=row.id)
        #Bankaccount.name_account = name
        #print(row.name_account)
        #print(row.id, 2)
        session.add(acc_one)
        session.add(acc_two)
        #session.query('bankaccount').filter(row.name_account)
        session.commit()


