from pydantic import BaseModel

from app.domain.entities.course_filters import CourseFilters
from app.repositories.course_repo import CourseRepo
from app.responses import ResponseFailure, ResponseSuccess


class FilterCourseByStandards(BaseModel):
    course_repo: CourseRepo

    class Config:
        # Pydantic will complain if something (enrolment_repo) is defined
        # as having a non-BaseModel type (e.g. an ABC). Setting this ensures
        # that it will just check that the value isinstance of this class.
        arbitrary_types_allowed = True

    def execute(self, course_filters: CourseFilters):
        try:
            course = self.course_repo.search_course(course_filters=course_filters)
            message = "Courses with Industry Standards = " + str(
                course_filters.industry_standards
            )
        except Exception as e:
            return ResponseFailure.build_from_resource_error(message=e)

        return ResponseSuccess(value=course, message=message)
