from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.setup import Base


class Location(Base):
    """Represents a physical location where items can be lost or found."""
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    # Relationship: one location can have multiple items
    items = relationship("Item", back_populates="location")

    def __repr__(self):
        return f"<Location(id={self.id}, name='{self.name}')>"
