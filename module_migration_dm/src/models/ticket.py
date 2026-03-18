import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class TicketStatusEnum(enum.Enum):
    open = "open"
    running = "running"
    failed = "failed"
    success = "success"
    needs_review = "needs_review"

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    status = Column(Enum(TicketStatusEnum), default=TicketStatusEnum.open, nullable=False)

    actions = relationship("TicketAction", back_populates="ticket", cascade="all, delete-orphan")

class TicketAction(Base):
    __tablename__ = "ticket_action"

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey("ticket.id", ondelete="CASCADE"), nullable=False)
    action = Column(String(255), nullable=False)
    success = Column(Boolean, nullable=False, default=False)

    ticket = relationship("Ticket", back_populates="actions")
