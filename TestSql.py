# coding:utf-8
import sqlite3
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

conn = sqlite3.connect(r"C:\ProgramData\Reformer\cloudpark\sqlite_carpark.db")
cur = conn.cursor()
cur.execute("select *from car_in")
print(cur.fetchall())
cur.execute("select *from car_out")
print(cur.fetchall())
cur.close()
conn.close()

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    # 如果有多个类指向同一张表，那么在后边的类需要把extend_existing设为True，表示在已有列基础上进行扩展
    # 或者换句话说，sqlalchemy允许类是表的字集
    # __table_args__ = {'extend_existing': True}
    # 如果表在同一个数据库服务（datebase）的不同数据库中（schema），可使用schema参数进一步指定数据库
    # __table_args__ = {'schema': 'test_database'}

    # 各变量名一定要与表的各字段名一样，因为相同的名字是他们之间的唯一关联关系
    # 从语法上说，各变量类型和表的类型可以不完全一致，如表字段是String(64)，但我就定义成String(32)
    # 但为了避免造成不必要的错误，变量的类型和其对应的表的字段的类型还是要相一致
    # sqlalchemy强制要求必须要有主键字段不然会报错，如果要映射一张已存在且没有主键的表，那么可行的做法是将所有字段都设为primary_key=True
    # 不要看随便将一个非主键字段设为primary_key，然后似乎就没报错就能使用了，sqlalchemy在接收到查询结果后还会自己根据主键进行一次去重  autoincrement=True
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# engine = create_engine("sqlite:///相对或绝对路径")
# 在create_engine中我们多加了两样东西，一个是echo=Ture，一个是check_same_thread=False。
# echo=Ture----echo默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印。
# check_same_thread=False----sqlite默认建立的对象只能让建立该对象的线程使用，而sqlalchemy是多线程的所以我们需要指定check_same_thread=False来让建立的对象任意线程都可使用
# 存储到内存之中  "sqlite:///:memory:"
engine = create_engine("sqlite:///foo.db?check_same_thread=False", echo=True)
# 查看映射对应的表
User.__table__

# 创建数据表。一方面通过engine来连接数据库，另一方面根据哪些类继承了Base来决定创建哪些表
# checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
Base.metadata.create_all(engine, checkfirst=True)

# 上边的写法会在engine对应的数据库中创建所有继承Base的类对应的表，但很多时候很多只是用来则试的或是其他库的
# 此时可以通过tables参数指定方式，指示仅创建哪些表
# Base.metadata.create_all(engine,tables=[Base.metadata.tables['users']],checkfirst=True)
# 在项目中由于model经常在别的文件定义，没主动加载时上边的写法可能写导致报错，可使用下边这种更明确的写法
# User.__table__.create(engine, checkfirst=True)

# 另外我们说这一步的作用是创建表，当我们已经确定表已经在数据库中存在时，我完可以跳过这一步
# 针对已存放有关键数据的表，或大家共用的表，直接不写这创建代码更让人心里踏实

DBSession = sessionmaker(engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 查
user = session.query(User).filter(User.id == '5').one()
print('query type:', type(user))
print('query name:', user.name)
# 更新
session.query(User).filter(User.id == '5').update({"name": "dd"})
session.commit()
user = session.query(User).filter(User.id == '5').one()
print('update type:', type(user))
print('update name:', user.name)
# 删
session.query(User).filter(User.id == '5').delete()
session.commit()
for u in session.query(User):
    print(u)
# 关闭session:
session.close()
