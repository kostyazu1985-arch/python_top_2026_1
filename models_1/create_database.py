from faker import Faker

from models.database import create_db, Session
from models.group import Group
from models.lesson import Lesson
from models.student import Student


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons_name = ['Математика', 'Программирование', 'Культура речи', 'Дизайн', 'Статистика',
                    'Алгоритмы и структуры данных', 'Философия', 'Физика']

    group1 = Group(group_name='RPO-7')
    group2 = Group(group_name='RPO-9')

    session.add(group1)
    session.add(group2)

    for key, it in enumerate(lessons_name):
        lesson = Lesson(lesson_title=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    faker = Faker("ru-RU")
    group_list = [group1, group2]
    session.commit()

    for _ in range(100):
        full_name = faker.name().split()
        age = faker.random.randint(16, 26)
        group = faker.random.choice(group_list)
        student = Student(full_name, age, group.id)
        session.add(student)

    session.commit()
    session.close()
