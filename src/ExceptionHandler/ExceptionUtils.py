from fastapi import Request, Response, status
from Dto.ApiResponse import ApiResponseDto

from logger import get_logger

logger = get_logger(__name__)

def handle_exception(func):
    def inner(request: Request, response: Response, query: str, *args, **kwargs):
        try:
            return func(request, response, query, *args, **kwargs)
        except Exception as exc:
            import traceback
            traceback.print_exc()
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            error_msg = f"{type(exc).__name__}: {str(exc)}"
            logger.error(f"Error in service function: {exc}")
            return ApiResponseDto("INTERNAL SERVER ERROR", error_msg)
    return inner