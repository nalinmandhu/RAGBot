import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI, Request
from Chain.ChainRouter import chain_router
from logger import get_logger



load_dotenv()
from VectorDB import chromaRetrieval
from Chain import ChainUtils

app = FastAPI()
logger = get_logger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello"}

# logging.basicConfig(level=logging.INFO,
#                     format="%(asctime)s - %(levelname)s - %(message)s",
#                     handlers=[
#                         logging.FileHandler("app.log"),
#                         logging.StreamHandler()
#                     ])
# logger = logging.getLogger(__name__)

app.include_router(chain_router, prefix = "/abinbev")

@app.get("/health")
async def home(request: Request):
    return {"message": "Online"}


if __name__ == "__main__":
    uvicorn.run(app)

