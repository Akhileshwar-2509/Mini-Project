from datetime import date
from decimal import Decimal
from . import db


class Rental(db.Model):
    __tablename__ = "rentals"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    machine_id = db.Column(db.Integer, db.ForeignKey("machines.id"), nullable=False)

    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    total_cost = db.Column(db.Numeric(10, 2), nullable=False)

    # ---- Relationships
    user = db.relationship("User", back_populates="rentals")
    machine = db.relationship("Machine", back_populates="rentals")

    # ---- Helpers
    @classmethod
    def calculate_cost(cls, daily_rate: Decimal, start: date, end: date) -> Decimal:
        days = (end - start).days + 1
        return daily_rate * days

    def __repr__(self) -> str:
        return f"<Rental U:{self.user_id} M:{self.machine_id} {self.start_date}→{self.end_date}>"
