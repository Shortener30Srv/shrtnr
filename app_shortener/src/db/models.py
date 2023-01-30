from sqlalchemy import Column, String, DateTime

from src.db.pg_conn import Base, engine

Base.metadata.create_all(bind=engine)


class ShortLink(Base):
    __tablename__ = "shortlink"
    __table_args__ = {"schema": "shortner_srv"}
    id = Column(String(40), primary_key=True, index=True)
    short_link = Column(String(30), unique=True, index=True)
    usual_link = Column(String)
    modified_on = Column(DateTime(timezone=True))
    valid_up_to = Column(DateTime(timezone=True))
