from flask import Blueprint, request
from app.models import User
from app import db

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = User(
        full_name=data.get("full_name"),
        email=data.get("email"),
        phone=data.get("phone"),
        national_id=data.get("national_id"),
        password=data.get("password"),
    )
    db.session.add(user)
    db.session.commit()
    return {"status": "created", "user_id": user.id}


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    user = User.query.filter_by(email=email, password=password).first()
    if user:
        return {"status": "ok"}
    return {"status": "invalid"}, 401
