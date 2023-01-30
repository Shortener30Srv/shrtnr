import datetime
import uuid

from sqlalchemy.orm import Session
import validators
from fastapi import status
from validators import ValidationFailure

from sqlalchemy import select, delete

from src.core.cross_app import (
    ShortenerCrudResponse,
    ShortenerInPost,
    SrvEntityException
)

from src.db.models import ShortLink

TARGET_SEQUENCE = "QWERLTYUIOPyASDFGHJKZXCVBNMx0123456789qwertuiopasdfghjklzcvbnm-._~"
TARGET_BASE = 66
URI_DOMAIN = 'https://const.com/'


class UrlValidation:
    def __init__(self, db_sess: Session, url_in: str):
        self._db_sess = db_sess
        self._url_in = url_in

    def post_validation(self) -> None:
        self._validate_url_syntax()
        self._validate_existence()

    def get_validation(self) -> None:
        self._validate_url_syntax()

    def delete_validation(self) -> None:
        pass

    def _validate_url_syntax(self):
        _if_valid_public_url = validators.url(self._url_in, public=True)
        if isinstance(_if_valid_public_url, ValidationFailure):
            url_is_out_of_scope = SrvEntityException(
                status_code=status.HTTP_412_PRECONDITION_FAILED,
                detail=f"Ссылка либо некорретная либо не доступна",
            )
            raise url_is_out_of_scope

    def _validate_existence(self):
        stmnt = select(ShortLink.short_link).filter_by(usual_link=self._url_in)
        existed_links = self._db_sess.scalars(stmnt).all()
        if len(existed_links) == 0:
            return False
        else:
            _short_link = existed_links[0]
            link_is_exist = SrvEntityException(
                status_code=status.HTTP_412_PRECONDITION_FAILED,
                detail=f"Кратколинк уже создан: {_short_link}",
            )
            raise link_is_exist


class ShortenerEntity:
    def __init__(self, db_sess: Session):
        self._db_sess = db_sess

    def create_record(self, shortener_in: ShortenerInPost) -> ShortenerCrudResponse:
        self._validate_post(shortener_in)
        new_record = self._create_short_link(shortener_in)
        response_out = ShortenerCrudResponse()
        response_out.long_link = new_record.usual_link
        response_out.short_link = new_record.short_link
        response_out.valid_up_to = new_record.valid_up_to
        return response_out

    def delete_record(self, short_link: str) -> ShortenerCrudResponse:
        _db_links = self._read_links_by_short(short_link)
        response_out = ShortenerCrudResponse()
        response_out.long_link = _db_links[0][1]
        response_out.short_link = _db_links[0][0]
        response_out.valid_up_to = _db_links[0][2]
        response_out.msg_info = '...запись удаляется...'
        stmnt = delete(ShortLink).where(ShortLink.short_link == _db_links[0][0])
        self._db_sess.execute(stmnt)
        self._db_sess.commit()
        return response_out

    def read_by_shortlink(self, short_link: str) -> ShortenerCrudResponse:
        _db_links = self._read_links_by_short(short_link)
        response_out = ShortenerCrudResponse()
        response_out.short_link = _db_links[0][0]
        response_out.long_link = _db_links[0][1]
        response_out.valid_up_to = _db_links[0][2]
        return response_out

    def _read_links_by_short(self, short_link: str):
        stmnt = select(ShortLink.short_link,
                       ShortLink.usual_link,
                       ShortLink.valid_up_to
                       ).filter_by(short_link=short_link)
        _db_links = self._db_sess.execute(stmnt).all()
        if len(_db_links) < 1:
            no_such_link = SrvEntityException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Такой кратколинк не выдавался (или удален) {short_link}",
            )
            raise no_such_link
        return _db_links

    def _validate_post(self, shortener_in: ShortenerInPost) -> None:
        url_validation = UrlValidation(db_sess=self._db_sess, url_in=shortener_in.long_link)
        url_validation.post_validation()

    def _create_short_link(self, shortener_in: ShortenerInPost) -> ShortLink:
        _new_short_link = ShortLink()
        _new_short_link.id = str(uuid.uuid4())
        _new_short_link.usual_link = shortener_in.long_link
        _new_short_link.short_link = URI_DOMAIN + ShortLinkGenerator().sh()
        _new_short_link.modified_on = datetime.datetime.now()
        _new_short_link.valid_up_to = datetime.datetime.now() + datetime.timedelta(days=30)
        self._db_sess.add(_new_short_link)
        self._db_sess.commit()
        return _new_short_link


class ShortLinkGenerator:
    def __init__(self):
        pass

    def sh(self) -> str:
        return self._generate_short_link_key()

    def _generate_short_link_key(self):
        _num1_base10 = int(datetime.datetime.now().strftime("%y%m%d%H%M"))
        _num2_base10 = int(datetime.datetime.now().strftime("%S%f"))
        _num1_base66 = self._frombase10to64(_num1_base10) + self._frombase10to64(_num2_base10)
        return _num1_base66

    def _frombase10to64(self, int10: int) -> str:
        _base66 = ''
        int_div = int10
        while int_div > 0:
            int_div = int_div // TARGET_BASE
            div_remainder = int_div % TARGET_BASE
            _base66 = str(_base66) + str(TARGET_SEQUENCE[div_remainder])
        return _base66

