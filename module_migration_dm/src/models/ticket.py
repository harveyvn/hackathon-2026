from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Ticket(Base):
    __tablename__ = "ticket"

    id = Column(Integer, primary_key=True)
    description = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="tickets")