from pydantic import BaseModel

from app.domain.entities.course_filters import CourseFilters
from app.repositories.course_repo import CourseRepo
from app.responses import ResponseFailure, ResponseSuccess


class FilterCourseByAvailability(BaseModel):
    course_repo: CourseRepo

    class Config:
        # Pydantic will complain if something (enrolment_repo) is defined
        # as having a non-BaseModel type (e.g. an ABC). Setting this ensures
        # that it will just check that the value isinstance of this class.
        arbitrary_types_allowed = True

    def execute(self, course_filters: dict):
        try:
            course_filters = CourseFilters(**course_filters)
            course = self.course_repo.search_course(course_filters=course_filters)
            message = "Courses with Availability = " + str(course_filters.availability)
        except Exception as e:
            return ResponseFailure.build_from_resource_error(message=e)

        return ResponseSuccess(value=course, message=message)
