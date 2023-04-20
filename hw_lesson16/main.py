import  db
from hw_lesson16.model import Base
from hw_lesson16.model.bankaccount import Bankaccount
from hw_lesson16.model.operation import create_operation_db
from hw_lesson16.model.bankaccount import create_account
from hw_lesson16.model.schet import create_schet
from hw_lesson16.model.history import create_history

db.configurate_engine()
# создаем таблицы
Base.metadata.drop_all(bind=db.engine)
Base.metadata.create_all(bind=db.engine)

create_operation_db()
create_account()
create_schet()
create_history()
#acc = Bankaccount()
#first = create_account(acc, 'Ann')









# # создаем сессию подключения к бд
# with Session(autoflush=False, bind=db.engine) as db:
#     # создаем объект Person для добавления в бд
#     tom = Person(name="Tom", age=38)
#     sam = Person(name="SAM", age=39)
#     db.add(tom)
#     db.add(sam)# добавляем в бд
#     db.commit()  # сохраняем изменения
#     print(tom.id, tom.name, tom.age)  # можно получить установленный id
#     people = db.query(Person).all()
#     for p in people:
#         print(p.name)
# ----------------------
# db.configurate_engine()
# print(db.engine)
# #Base.metadata.drop_all(db.engine)
# Base.metadata.create_all(bind=db.engine)
#
# session = db.Session()
# first_row = Operation(name_operation='Add')
# session.add(first_row)
# session.commit()
#
# print(1)
# first_query = session.query(Operation)
# print(first_query)
# # print(first_query.)
# ---------------------