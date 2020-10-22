from enum import Enum

from pydantic import BaseModel


class SuccessType(str, Enum):
    SUCCESS = "200-Success"


class FailureType(str, Enum):
    PARAMETER_ERROR = "400-PARAMETER ERROR"
    UNAUTHORISED_ERROR = "401-UNAUTHORISED ERROR "
    RESOURCE_ERROR = "404-Resource Error"
    VALIDATION_ERROR = "422-VALIDATION ERROR"
    SYSTEM_ERROR = "500-SYSTEM ERROR"


class ResponseFailure(BaseModel):
    type: FailureType
    message: str

    @classmethod
    def _format_message(cls, message):
        if isinstance(message, Exception):
            return f"{message.__class__.__name__}: {message}"
        return message

    def __bool__(self):
        return False

    @classmethod
    def build_from_resource_error(cls, message=None):
        return cls(
            type=FailureType.RESOURCE_ERROR, message=cls._format_message(message)
        )

    @classmethod
    def build_from_system_error(cls, message=None):
        return cls(type=FailureType.SYSTEM_ERROR, message=cls._format_message(message))

    @classmethod
    def validation_error(cls, message=None):
        return cls(
            type=FailureType.VALIDATION_ERROR, message=cls._format_message(message)
        )

    @classmethod
    def build_from_unauthorised_error(cls, message=None):
        return cls(
            type=FailureType.UNAUTHORISED_ERROR, message=cls._format_message(message)
        )


class ResponseSuccess(BaseModel):
    value: dict
    type = SuccessType.SUCCESS
    message: str = "Success"

    def __bool__(self):
        return True
