from datetime import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource

from app import api

from ..entities.course import Course
from ..schemas.course_schema import CourseSchema
from ..services.course_service import (
    create_course,
    delete_course,
    list_course_by_id,
    list_courses,
    update_course,
)


class CourseList(Resource):
    def get(self):
        courses = list_courses()
        schema = CourseSchema(many=True)
        return make_response(schema.jsonify(courses), 200)

    def post(self):
        schema = CourseSchema()
        validate = schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        else:
            name = request.json.get("name")
            description = request.json.get("description")
            created_at_str = request.json.get("created_at")
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d")

            new_course = Course(
                name=name,
                description=description,
                created_at=created_at,
            )
            result = create_course(new_course)
            return make_response(schema.jsonify(result), 201)


class CourseDetail(Resource):
    def get(self, id):
        course = list_course_by_id(id)

        if course is None:
            return make_response(jsonify("Course not found"), 404)

        schema = CourseSchema()
        return make_response(schema.jsonify(course), 200)

    def put(self, id):
        course_db = list_course_by_id(id)

        if course_db is None:
            return make_response(jsonify("Course not found"), 404)

        schema = CourseSchema()
        validate = schema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)

        else:
            name = request.json.get("name")
            description = request.json.get("description")
            created_at_str = request.json.get("created_at")
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d")

            new_course = Course(
                name=name,
                description=description,
                created_at=created_at,
            )
            update_course(
                old_course=course_db,
                new_course=new_course,
            )
            updated_course = list_course_by_id(id=id)
            return make_response(schema.jsonify(updated_course), 201)

    def delete(self, id):
        course = list_course_by_id(id)

        if course is None:
            return make_response(jsonify("Course not found"), 404)

        delete_course(course=course)
        return make_response(jsonify("Course deleted successfully"), 204)


api.add_resource(CourseList, "/course")
api.add_resource(CourseDetail, "/course/<int:id>")
