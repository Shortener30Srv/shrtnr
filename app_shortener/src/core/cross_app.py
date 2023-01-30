import datetime

from pydantic import BaseModel


class ShortenerInPost(BaseModel):
    long_link: str = ""

    class Config:
        orm_mode = True


class ShortenerCrudResponse(BaseModel):
    long_link: str = ""
    short_link: str = ""
    valid_up_to: datetime.datetime = datetime.datetime.now() + datetime.timedelta(days=30)
    msg_info: str = ""

    class Config:
        orm_mode = True


class SrvEntityException(Exception):
    """Exception для сущности .
    Attributes:
        status_code -- код ошибки
        detail -- описание ошибки
    """
    def __init__(self, status_code, detail=""):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)