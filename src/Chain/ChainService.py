from fastapi import Request, Response
from Dto.ApiResponse import ApiResponseDto
from ExceptionHandler.ExceptionUtils import handle_exception
from Chain.ChainUtils import answer_query
from VectorDB.chromaRetrieval import query_docs

from logger import get_logger
logger = get_logger(__name__)

@handle_exception
def answer_user_query(request: Request, response: Response, query: str):
    retrieved_content = query_docs(query)
    answer = answer_query(query, retrieved_content)
    logger.debug(f"Processing result: {answer}")
    return ApiResponseDto("SUCCESS", answer)
