from flask import Blueprint, request
from app.models import Booking
from app import db

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/book", methods=["POST"])
def create_booking():
    data = request.json
    booking = Booking(
        user_id=data.get("user_id"),
        location=data.get("location"),
    )
    db.session.add(booking)
    db.session.commit()
    return {"status": "booked", "booking_id": booking.id}
