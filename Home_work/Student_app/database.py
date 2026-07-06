# Импортируем стандартные колонки и типы данных из SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
# Импортируем инструмент для создания базового класса моделей и виртуальных связей
from sqlalchemy.orm import DeclarativeBase, relationship



class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="students")
