from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base


class User(Base):
    """Represents a user who can report lost or found items."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationship: one user can report multiple items
    items = relationship("Item", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
