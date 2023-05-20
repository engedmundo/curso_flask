from flask_restful import Resource

from app import api


class CourseList(Resource):
    def get(self):
        return "Hello"


api.add_resource(CourseList, "/course")
