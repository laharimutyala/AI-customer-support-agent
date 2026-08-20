from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models import Ticket
from schemas import TicketCreate

from services.classifier import classify_ticket
from services.ai_responder import generate_ai_response
from services.escalator import should_escalate

# Create FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Home API
@app.get("/")
def home():
    return {
        "message": "Customer Support Agent Running"
    }


# Create Ticket API
@app.post("/tickets")
def create_ticket(
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    # Check if ticket should be escalated
    escalate = should_escalate(ticket.issue)

    # Classify issue
    category = classify_ticket(ticket.issue)

    # Generate AI response
    response = generate_ai_response(ticket.issue)

    # Set status
    status = "Escalated" if escalate else "Closed"

    # Create ticket object
    new_ticket = Ticket(
        customer=ticket.customer,
        issue=ticket.issue,
        category=category,
        response=response,
        status=status
    )

    # Save to database
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return {
        "message": "Ticket created successfully",
        "ticket_id": new_ticket.id,
        "category": category,
        "status": new_ticket.status,
        "response": response
    }


# Get all tickets API
@app.get("/tickets")
def get_tickets(
    db: Session = Depends(get_db)
):
    tickets = db.query(Ticket).all()
    return tickets