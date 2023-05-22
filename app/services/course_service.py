from app import db

from ..models.course_model import Course
from ..entities.course import Course as CourseEntity


def create_course(course: CourseEntity) -> Course:
    course_db = Course(
        name=course.name,
        description=course.description,
        created_at=course.created_at,
    )
    db.session.add(course_db)
    db.session.commit()
    return course_db


def list_courses() -> Course:
    courses = Course.query.all()
    return courses


def list_course_by_id(id) -> Course:
    course = Course.query.filter_by(id=id).first()
    return course


def update_course(old_course: CourseEntity, new_course: CourseEntity) -> None:
    old_course.name = new_course.name
    old_course.description = new_course.description
    old_course.created_at = new_course.created_at
    db.session.commit()
    return

def delete_course(course: Course) -> None:
    db.session.delete(course)
    db.session.commit()
    return


