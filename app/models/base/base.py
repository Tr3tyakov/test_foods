from sqlalchemy.ext.declarative import declarative_base

from app.models.base.mixins import DeclareMixin

Base = declarative_base()


class BaseModel(Base, DeclareMixin):
    __abstract__ = True
