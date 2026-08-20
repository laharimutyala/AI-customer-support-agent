from sqlalchemy import Column, Integer, String
from database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String, index=True)
    issue = Column(String)
    status = Column(String, default="Open")
    category = Column(String, default="other")
    response = Column(String)