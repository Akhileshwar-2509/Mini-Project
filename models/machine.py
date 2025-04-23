from decimal import Decimal
from . import db


class Machine(db.Model):
    __tablename__ = "machines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    rate_per_day = db.Column(db.Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    image_url = db.Column(db.String(255), nullable=True)
    is_available = db.Column(db.Boolean, default=True)

    rentals = db.relationship("Rental", back_populates="machine", cascade="all, delete-orphan")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "rate_per_day": str(self.rate_per_day),
            "image_url": self.image_url,
            "is_available": self.is_available,
        }

    def __repr__(self) -> str:
        return f"<Machine {self.name}>"
