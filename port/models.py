from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), nullable=False)
    contact_pref = db.Column(db.String(20))

    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    status = db.Column(db.String(20), default="new")

    def __repr__(self):
        return f"<ContactMessage {self.full_name}>"