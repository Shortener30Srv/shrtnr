from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

import psycopg
from psycopg import AsyncConnection

from src.core.settings import settings

connection_string = {"dbname": settings.DB_NAME,
                     "user": settings.DB_USER,
                     "password": settings.DB_PSWD,
                     "host": settings.DB_HOST,
                     "port": settings.DB_PORT,
                     }
# db_conn = AsyncConnection.connect(**connection_string)
# db_conn.autocommit = False

SQLALCHEMY_DATABASE_URL = settings.DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


# async def close_db_connection():
#     db_conn.close()
#
#
# async def get_db_connection() -> psycopg.connection:
#     return db_conn
