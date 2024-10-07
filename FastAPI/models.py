from sqlalchemy import Column, ForeignKey, Integer, String
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