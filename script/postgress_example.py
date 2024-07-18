# Example connection string for PostgreSQL
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgres@db/postgres')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Query the user
user = session.query(User).filter_by(name='Alice').first()
print(user.name, user.age)

# Update the user's age
user.age = 31
session.commit()

# Delete the user
# session.delete(user)
# session.commit()
