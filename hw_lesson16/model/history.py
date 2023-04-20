from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import hw_lesson16.db as db
import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


from hw_lesson16.model import Base

#Base = declarative_base()
class History(Base):
    __tablename__ = 'history'

    id= Column(Integer, primary_key=True)
    sum_operation = Column(Integer)
    date_operation = Column(DateTime)
    operation_id = Column(Integer, ForeignKey('operation.id'))
    history_op = relationship('Operation', back_populates='operations')
    schet_id = Column(Integer, ForeignKey('schet.id'))
    history_sc = relationship('Schet', back_populates='schet')



    def __repr__(self):
        return f'{self.id} -----'

def create_history():
    db.configurate_engine()
    with db.Session(autoflush=False, bind=db.engine) as session:
        history_add_S = History(
            sum_operation=10,
            date_operation=datetime.datetime.now(),
            operation_id=1,
            schet_id=2
        )

        history_add_S_1 = History(
            sum_operation=20,
            date_operation=datetime.datetime.now(),
            operation_id=1,
            schet_id=2
        )

        history_add_S_2 = History(
            sum_operation=15,
            date_operation=datetime.datetime.now(),
            operation_id=2,
            schet_id=2
        )

        history_add_V = History(
            sum_operation=100,
            date_operation=datetime.datetime.now(),
            operation_id=2,
            schet_id=5
        )

        session.add(history_add_S)
        session.add(history_add_S_1)
        session.add(history_add_S_2)
        session.add(history_add_V)
        session.commit()
