import os
from sqlalchemy import and_, or_, not_, desc, func, distinct, text

from models.database import DATABASE_NAME, Session
import create_database as db_creator
from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    # print(session.query(Lesson).all())
    # print('*' * 200)

    # for it in session.query(Lesson):
    #     # print(it)
    #     print(it.lesson_title)
    # print('*' * 200)

    # print(session.query(Lesson).count())
    # print('*' * 200)
    #
    # print(session.query(Lesson).first())
    # print('*' * 200)
    #
    # print(session.query(Lesson).get(3))
    # print('*' * 200)

    # for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('%м%')):
    #     print(it)
    # print('*' * 200)
    #
    # for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('%м%'))):
    #     print(it)
    # print('*' * 200)
    #
    # for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('%о%'))):
    #     print(it)
    # print('*' * 200)

    # for it, gr in session.query(Lesson.lesson_title, Group.group_name).filter(and_(Group.group_name == "RPO-9",
    #                             Group.id == association_table.c.group_id, association_table.c.lesson_id == Lesson.id)):
    #     print(it, gr)
    # print('*' * 200)
    #
    # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    # print('*' * 200)

    # print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
    # print('*' * 200)

    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(["Физика", "Дизайн"])).all())
    # print('*' * 200)

    # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(["Физика", "Дизайн"])).all())
    # print('*' * 200)

    # print(session.query(Student).filter(Student.age.between(16, 17)).all())
    # print('*' * 200)

    # print(session.query(Student).filter(not_(Student.age.between(16, 24))).all())
    # print('*' * 200)

    # print(session.query(Student).filter(Student.age.like("1%")).all())
    # print('*' * 200)

    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(Student).join(Group).filter(Group.group_name == "RPO-7"):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(func.count(Student.surname),
    #     Group.group_name).join(Group).group_by(Group.group_name).having(func.count(Student.surname)):
    #     print(it)
    # print('*' * 200)

    # for it in session.query(distinct(Student.age)):
    #     print(it)
    # print('*' * 200)

    for it in session.query(Student.age).filter(Student.age < 20).distinct():
        print(it)
    print('*' * 200)




