from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.repositories.s3_course_repo import S3CourseRepo
from app.use_cases.filter_by_availability import FilterCourseByAvailabilty
from app.use_cases.filter_by_competency import FilterCourseByCompetency
from app.use_cases.filter_by_date import FilterCourseByDate
from app.use_cases.filter_by_location import FilterCourseByLocation
from app.use_cases.filter_by_standards import FilterCourseByStandards
from app.use_cases.search_course import SearchCourse

router = APIRouter()
course_repo = S3CourseRepo()


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
    Search Courses using filters\n
    <b>course_name</b> is required.
    <b>industry_standards</b> is a list of industry standard versions
    this course confirms to.\n
    <b>competency</b> is a list of competencies.\n
    <b>location</b> is the location where course is conducted.
    It is required.\n
    <b>start_date</b> is in format ISO 8601 (YYYY-MM-DDTHH:mm:ss.sssZ).
    It is the starting date of the course.
    It is required.\n
    <b>availability</b> is a boolean which is True or False depending
    upon the availability of the course. It is required.\n
    <b>hours_per_week</b> is the number of hours per week the course
    demands from the students. It is a float value. It is required.\n
    <b>duration</b> is the total duration of course in string.
    It is required.\n
    <b>fees_from</b> is the minimum fee of the course.
    It is a float value. It is required\n
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
