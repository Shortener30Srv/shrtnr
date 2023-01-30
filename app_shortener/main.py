
import uvicorn, logging
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse
from src.core.logger import LOGGING
from src.api.v1 import shortener_crud

app = FastAPI()

load_dotenv()

app = FastAPI(
    title="Сервис кратколинков",
    description="...укороченный сервис кратколинков...",
    version="1.0.1",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


app.include_router(
    shortener_crud.router,
    prefix="/api/v1/shortener",
    tags=[
        "shortener/кратколинки",
    ],
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=LOGGING,
        log_level=logging.DEBUG,
    )