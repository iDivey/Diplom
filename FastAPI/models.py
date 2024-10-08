from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Book(Base):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(30), nullable=False)
    name_father_Author = Column(String(5), nullable=False)
    title = Column(String, nullable=False)
    publisher = Column(String(20), nullable=False)
    city = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    pages = Column(Integer, nullable=False)


class Conf(Base):
    __tablename__ = 'conference'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(30), nullable=False)
    name_father_Author = Column(String(5), nullable=False)
    title = Column(String, nullable=False)
    publisher = Column(String(20), nullable=False)
    place = Column(String(20), nullable=False)
    date = Column(DateTime, nullable=False)
    city = Column(String(20), nullable=False)
    year = Column(Integer, nullable=False)
    page_start = Column(Integer, nullable=False)
    page_end = Column(Integer, nullable=False)


class Jour(Base):
    __tablename__ = 'journal'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(30), nullable=False)
    name_father_Author = Column(String(5), nullable=False)
    title = Column(String, nullable=False)
    publisher = Column(String(20), nullable=False)
    number_tom = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    page_start = Column(Integer, nullable=False)
    page_end = Column(Integer, nullable=False)