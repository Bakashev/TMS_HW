from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
import hw_lesson16.db as db
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped



from hw_lesson16.model import Base

#Base = declarative_base()
class Operation(Base):
    __tablename__ = "operation"

    id = Column(Integer, primary_key=True)
    name_operation = Column(String)
    operations = relationship('History', back_populates='history_op')

    def __repr__(self):
        return f'{self.id} ----- {self.name_operation} --'


def create_operation_db():
    db.configurate_engine()
    with Session(autoflush=False, bind=db.engine) as session:
        #session = db.Session()
        first_row = Operation(name_operation='Пополнение')
        second_row = Operation(name_operation='Снятие')
        session.add(first_row)
        session.add(second_row)
        session.commit()
