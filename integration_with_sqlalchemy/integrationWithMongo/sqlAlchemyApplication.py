import sqlalchemy

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}), fullname={self.fullname}"
    

class Address(Base):    
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship(
        "User", back_populates ="address"
    )

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__table__)

# database connection
engine = create_engine("sqlite://")

# creating the classes as a table in the database
Base.metadata.create_all(engine)

# inspect database
insp = inspect(engine)


print(insp.get_table_names())
print(insp.has_table("user_account"))

with Session(engine) as session:
    mayk = User(
        name='mayk',
        fullname='Mayk johnson',
        address=[Address(email_address='mayk@email.com')]
    )

    sandy = User(
        name='sandy',
        fullname='Sandy Allen',
        address=[Address(email_address='sandy@email.com'), Address(email_address='sandy@exemplo.com')]
    )

    patrick = User(
        name='patrick',
        fullname='Patrick Allen'
        )
    
    # sending to the database (data persistence)
    session.add_all([mayk,sandy,patrick])

    session.commit()

statement = select(User).where(User.name.in_(['sandy', 'mayk']))
print('\nRetrieving users from filtering condition\n')
for user in session.scalars(statement):
    print(user)

statement_address = select(Address).where(Address.user_id.in_([2]))
print('\nRetrieving addresses from sandy\n')
for address in session.scalars(statement_address):
    print(address)

# order_by

order_stmt = select(User).order_by(User.fullname.desc())
print('\nRetrieving info in descending order\n')
for result in session.scalars(order_stmt):
    print(result)

# join

join_stmt = select(User.fullname, Address.email_address).join_from(Address, User)
print('\nRetrieving info using join\n')
for result in session.scalars(join_stmt):
    print(result)

# with connectio and fetchall

connection = engine.connect()

results = connection.execute(join_stmt).fetchall()
print('\nExecuting statement from connection\n')
for result in results:
    print(result)

# Count
stmt_count = select(func.count('*')).select_from(User)
print('\nTotal instances in user\n')
for result in session.scalars(stmt_count):
    print(result)