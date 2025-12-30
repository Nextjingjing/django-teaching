from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        # Unexpected error (500)
        logger.exception("Unhandled exception", exc_info=exc)
        return Response(
            {
                "error": True,
                "status_code": 500,
                "message": "Internal server error",
            },
            status=500,
        )

    if isinstance(exc, ValidationError):
        return Response(
            {
                "error": True,
                "status_code": response.status_code,
                "errors": response.data,
            },
            status=response.status_code,
        )

    if isinstance(exc, APIException):
        return Response(
            {
                "error": True,
                "status_code": response.status_code,
                "message": response.data.get("detail"),
                "code": exc.default_code,
            },
            status=response.status_code,
        )

    return response