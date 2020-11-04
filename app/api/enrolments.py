from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.repositories.s3_course_repo import S3CourseRepo
from app.repositories.s3_enrolment_repo import S3EnrolmentRepo
from app.requests.enrolment_requests import NewEnrolmentRequest
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


@router.get("/search_course/")
def search_course(
    industry_standards: Optional[List[str]] = Query(None),
    competency: Optional[List[str]] = Query(None),
    location: Optional[str] = None,
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
    availability: Optional[bool] = None,
):
    """
    Search Courses using filters
    """
    inputs = {
        "industry_standards": industry_standards,
        "competency": competency,
        "location": location,
        "from_date": from_date,
        "to_date": to_date,
        "availability": availability,
    }
    use_case = SearchCourse(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_standards/")
def search_course_by_standards(
    industry_standards: Optional[List[str]] = Query(None),
):
    """
    Search Courses using filters
    """
    inputs = {
        "industry_standards": industry_standards,
    }
    use_case = FilterCourseByStandards(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_competency/")
def search_course_by_competency(
    competency: Optional[List[str]] = Query(None),
):
    """
    Search Courses using filters
    """
    inputs = {
        "competency": competency,
    }
    use_case = FilterCourseByCompetency(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_location/")
def search_course_by_location(
    location: Optional[str] = None,
):
    """
    Search Courses using filters
    """
    inputs = {
        "location": location,
    }
    use_case = FilterCourseByLocation(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_date/")
def search_course_by_date(
    from_date: Optional[datetime] = None,
    to_date: Optional[datetime] = None,
):
    """
    Search Courses using filters
    """
    inputs = {
        "from_date": from_date,
        "to_date": to_date,
    }
    use_case = FilterCourseByDate(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response


@router.get("/search_course_by_availability/")
def search_course_by_availability(
    availability: Optional[bool] = None,
):
    """
    Search Courses using filters
    """
    inputs = {
        "availability": availability,
    }
    use_case = FilterCourseByAvailabilty(course_repo=course_repo)
    response = use_case.execute(inputs)
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
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
    if bool(response) is False:  # If request failed
        raise HTTPException(status_code=response.type.value, detail=response.message)
    return response
