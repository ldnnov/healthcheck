from .base import Base
from sqlalchemy import Column, Integer, String, DateTime


class Url(Base):

    __tablename__ = "url"

    id = Column(Integer, unique=True, primary_key=True)
    url = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)

    def __init__(self, url, date, duration, status):
        self.url = url
        self.date = date
        self.duration = duration
        self.status = status

    def __repr__(self):
        return f"<Url: {self.url}, Date: {self.date}, Duration: {self.duration}, Status: {self.status}>"
