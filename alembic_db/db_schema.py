from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import NUMERIC
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Data(Base):
    __tablename__ = "data_table"
    id = Column(Integer(), primary_key=True, nullable=False)
    data_value = Column(NUMERIC(asdecimal=False))
