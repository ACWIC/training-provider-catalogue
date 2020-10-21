from typing import Optional

from fastapi import APIRouter

from app.repositories.s3_course_repo import S3CourseRepo
from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from app.requests.enrolment_requests import NewEnrolmentRequest
from app.requests.filter_by_availabilty_request import FilterByAvailabilityRequest
from app.requests.filter_by_competency_request import FilterByCompetencyRequest
from app.requests.filter_by_date_request import FilterByDateRequest
from app.requests.filter_by_location_request import FilterByLocationRequest
from app.requests.filter_by_standards_request import FilterByStandardsRequest
from app.requests.search_course_request import SearchCourseRequest
from app.use_cases.create_new_enrolment import CreateNewEnrolment
from app.use_cases.filter_by_availability import FilterCourseByAvailabilty
from app.use_cases.filter_by_competency import FilterCourseByCompetency
from app.use_cases.filter_by_date import FilterCourseByDate
from app.use_cases.filter_by_location import FilterCourseByLocation
from app.use_cases.filter_by_standards import FilterCourseByStandards
from app.use_cases.search_course import SearchCourse

router = APIRouter()
course_repo = S3CourseRepo()
enrolment_repo = S3EnrolmentRepo()


@router.post("/search_course/")
def search_course(inputs: Optional[SearchCourseRequest]):
    """
    Search Courses using filters
    """
    use_case = SearchCourse(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.post("/search_course/by_availability/{course_filter}")
def search_course_by_availability(
    inputs: FilterByAvailabilityRequest,
):
    """
    Search Courses using filters
    """
    use_case = FilterCourseByAvailabilty(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.post("/search_course/by_competency/{course_filter}")
def search_course_by_competency(
    inputs: FilterByCompetencyRequest,
):
    """
    Search Courses using filters
    """
    use_case = FilterCourseByCompetency(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.post("/search_course/by_date/{course_filter}")
def search_course_by_date(
    inputs: FilterByDateRequest,
):
    """
    Search Courses using filters
    """
    use_case = FilterCourseByDate(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.post("/search_course/by_location/{course_filter}")
def search_course_by_location(
    inputs: FilterByLocationRequest,
):
    """
    Search Courses using filters
    """
    use_case = FilterCourseByLocation(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.post("/search_course/by_standards/{course_filter}")
def search_course_by_standards(
    inputs: FilterByStandardsRequest,
):
    """
    Search Courses using filters
    """
    use_case = FilterCourseByStandards(course_repo=course_repo)
    response = use_case.execute(inputs)
    return response


@router.get("/enrolments/{enrolment_id}")
def enrolments(enrolment_id: str):
    """Getting an enrollment by ID will return the current
    state of the enrollment, derived from the enrollment’s journal.
    """
    return {"your_enrolment_id": enrolment_id}


@router.post("/enrolments")
def create_enrolment(inputs: NewEnrolmentRequest):
    """Posting an enrollment authorisation is a synchronous proccess that
    immediately succeeds (or fails) to create an enrollment authorisation,
    and assign it a unique enrollment authorisation id.

    The initial state of the enrollment authorisation is “lodged”.
    """
    use_case = CreateNewEnrolment(enrolment_repo=enrolment_repo)
    response = use_case.execute(inputs)

    return response
