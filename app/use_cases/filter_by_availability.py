from pydantic import BaseModel

from app.repositories.course_repo import CourseRepo
from app.requests.filter_by_availabilty_request import FilterByAvailabilityRequest
from app.responses import ResponseFailure, ResponseSuccess


class FilterCourseByAvailabilty(BaseModel):
    course_repo: CourseRepo

    class Config:
        # Pydantic will complain if something (enrolment_repo) is defined
        # as having a non-BaseModel type (e.g. an ABC). Setting this ensures
        # that it will just check that the value isinstance of this class.
        arbitrary_types_allowed = True

    def execute(self, search_course_request: FilterByAvailabilityRequest):
        try:
            course_filters = vars(search_course_request)
            course_id = self.course_repo.search_course(course_filters=course_filters)
        except Exception as e:
            return ResponseFailure.build_from_resource_error(message=e)

        return ResponseSuccess(value=course_id)
