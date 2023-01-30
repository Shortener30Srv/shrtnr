from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException
from src.core.cross_app import (
    ShortenerCrudResponse,
    ShortenerInPost,
    SrvEntityException
)

from src.srv.shortener_srv import ShortenerEntity
from src.db.pg_conn import get_db_session

router = APIRouter()


@router.post(
    "/",
    response_model=ShortenerCrudResponse,
    summary="Создание кратколинка (короткой ссылки)",
    description="Создание короткой ссылки (короткой ссылки) на основе длинный ссылки",
)
async def post_shortener(shortener_in: ShortenerInPost,
                         db_session: Session = Depends(get_db_session)) -> ShortenerCrudResponse:
    try:
        shortener_entity = ShortenerEntity(db_session)
        return shortener_entity.create_record(shortener_in)
    except SrvEntityException as exc_srv:
        raise HTTPException(status_code=exc_srv.status_code, detail=exc_srv.detail)


@router.delete(
    "/<string:short_url>",
    response_model=ShortenerCrudResponse,
    summary="Удаление кратколинка (короткой ссылки)",
    description="Удаление данных о кратколинке (короткой ссылки)",
)
async def delete_shortener(short_url: str,
                           db_session: Session = Depends(get_db_session)) -> ShortenerCrudResponse:
    try:
        shortener_entity = ShortenerEntity(db_session)
        return shortener_entity.delete_record(short_url)
    except SrvEntityException as exc_srv:
        raise HTTPException(status_code=exc_srv.status_code, detail=exc_srv.detail)


@router.get(
    "/short2usual/<string:short_url>",
    response_model=ShortenerCrudResponse,
    summary="По кратколинку возвращаем обычную ссылку",
    description="По кратколинку возвращаем обычную ссылку",
)
async def get_usual_lin_by_short(short_url: str,
                                 db_session: Session = Depends(get_db_session)) -> ShortenerCrudResponse:
    try:
        shortener_entity = ShortenerEntity(db_session)
        return shortener_entity.read_by_shortlink(short_url)
    except SrvEntityException as exc_srv:
        raise HTTPException(status_code=exc_srv.status_code, detail=exc_srv.detail)
