from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from src.models import Base, Ticket, TicketAction, TicketStatusEnum
from src.config import SQLALCHEMY_DATABASE_URL
import random

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

Base.metadata.create_all(engine)

ticket_names = [f"Ticket {i+1}" for i in range(20)]
ticket_types = ["bug", "feature", "task"]

statuses = list(TicketStatusEnum)

action_names = ["searching order", "propose email", "cancel order", "confirm payment", "update inventory"]

session = Session(engine)

for i in range(20):
    ticket = Ticket(
        name=ticket_names[i],
        type=random.choice(ticket_types),
        status=random.choice(statuses)
    )

    actions = []
    for _ in range(3):
        action = TicketAction(
            action=random.choice(action_names),
            success=random.choice([True, False])
        )
        actions.append(action)

    ticket.actions = actions
    session.add(ticket)

session.commit()
print("Inserted 20 dummy tickets with actions.")
session.close()
