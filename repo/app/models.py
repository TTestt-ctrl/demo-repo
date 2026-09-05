from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    national_id = db.Column(db.String(20))
    payment_info = db.Column(db.String(200))
    password = db.Column(db.String(200))


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime)
