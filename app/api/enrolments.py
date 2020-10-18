from fastapi import APIRouter

from app.repositories.s3_course_repo import S3CourseRepo
from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from app.requests.enrolment_requests import NewEnrolmentRequest
from app.requests.search_course_request import SearchCourseRequest
from app.use_cases.create_new_enrolment import CreateNewEnrolment
from app.use_cases.search_course import SearchCourse

router = APIRouter()
course_repo = S3CourseRepo()
enrolment_repo = S3EnrolmentRepo()


@router.post("/search_course/{course_filter}")
def search_course(
    inputs: SearchCourseRequest,
):
    """
    Search Courses using filters
    """
    use_case = SearchCourse(course_repo=course_repo)
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
