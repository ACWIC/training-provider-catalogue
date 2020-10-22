import abc


class CourseRepo(abc.ABC):
    @abc.abstractmethod
    def search_course(self, course_filters: dict) -> dict:
        pass
