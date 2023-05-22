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


def list_courses():
    courses = Course.query.all()
    return courses


def list_course_by_id(id):
    course = Course.query.filter_by(id=id).first()
    return course


def update_course(old_course, new_course):
    old_course.name = new_course.name
    old_course.description = new_course.description
    old_course.created_at = new_course.created_at
    db.session.commit()
    return
