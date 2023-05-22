from flask_restful import Resource
from ..schemas.course_schema import CourseSchema
from flask import request, make_response, jsonify
from app import api
from ..entities.course import Course
from ..services.course_service import create_course
from datetime import datetime


class CourseList(Resource):
    def get(self):
        return "Hello"

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


api.add_resource(CourseList, "/course")
