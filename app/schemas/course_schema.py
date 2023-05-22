from marshmallow import fields

from app import ma

from ..models import course_model


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_model.Course
        load_instance = True
        fields = ("id", "name", "description", "created_at")

    name = fields.String(required=True)
    description = fields.String(required=True)
    created_at = fields.Date(required=True)
