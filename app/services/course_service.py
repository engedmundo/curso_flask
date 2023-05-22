from app import db

from ..models.course_model import Course


def create_course(course):
    course_db = Course(
        name=course.name,
        description=course.description,
        created_at=course.created_at,
    )
    db.session.add(course_db)
    db.session.commit()
    return course_db
