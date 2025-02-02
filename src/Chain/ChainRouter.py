from fastapi import Request, Response, APIRouter, status
from Chain import ChainService
from Dto.requestDto import QueryRequestDto
from Chain.ChainService import answer_user_query

chain_router = APIRouter(prefix="/bot")

@chain_router.post("/answer", status_code=status.HTTP_200_OK)
async def answer_query(request: Request, response: Response, query_request_dto: QueryRequestDto):
    query = query_request_dto.query
    return answer_user_query(request, response, query)