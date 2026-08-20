from pydantic import BaseModel


class TicketCreate(BaseModel):
    customer: str
    issue: str