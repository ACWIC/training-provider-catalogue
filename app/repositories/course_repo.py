import abc

from app.domain.entities.course_filters import CourseFilters


class CourseRepo(abc.ABC):
    @abc.abstractmethod
    def search_course(self, course_filters: CourseFilters) -> dict:
        """"""
