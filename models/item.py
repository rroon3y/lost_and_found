from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.setup import Base


class Item(Base):
    """Represents a lost or found item reported by a user at a location."""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False)  # 'lost' or 'found'
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    location = relationship("Location", back_populates="items")
    user = relationship("User", back_populates="items")

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, status={self.status})>"
