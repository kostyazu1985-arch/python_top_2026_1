from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, Department, Student


engine = create_engine("sqlite:///university.db", echo=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


with Session() as session:

    if session.query(Student).count() == 0:

        dep1 = Department(name="Кафедра Информатики")
        dep2 = Department(name="Кафедра Математики")
        dep3 = Department(name="Кафедра Физики")


        students_list = [
            Student(name="Иванов Иван", age=19, department=dep1),
            Student(name="Петров Петр", age=20, department=dep1),
            Student(name="Сидоров Сидор", age=18, department=dep1),
            Student(name="Васильева Ольга", age=21, department=dep2),
            Student(name="Шутов Анатолий", age=19, department=dep2),
            Student(name="Кузнецов Алексей", age=22, department=dep2),
            Student(name="Павлов Павел", age=20, department=dep2),
            Student(name="Смирнова Анна", age=19, department=dep3),
            Student(name="Попов Дмитрий", age=18, department=dep3),
            Student(name="Тихонов Игорь", age=21, department=dep3),
        ]

        session.add_all([dep1, dep2, dep3])

        session.add_all(students_list)

        session.flush()

        session.commit()

    all_students = session.query(Student).all()
    print("Список студентов и их кафедр:")

    for student in all_students:
        print(f"Студент: {student.name} | Возраст: {student.age} | {student.department.name}")
