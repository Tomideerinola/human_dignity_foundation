from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)

    # Name of the service (Mental Health, Abuse Protection, etc.)
    name = db.Column(db.String(100), nullable=False, unique=True)

    # Used in URLs like /get-help/mental-health
    slug = db.Column(db.String(100), nullable=False, unique=True)

    # Short explanation shown on the UI
    description = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class HelpRequest(db.Model):
    __tablename__ = "help_requests"

    id = db.Column(db.Integer, primary_key=True)

    # Optional — allows anonymous help requests
    full_name = db.Column(db.String(255), nullable=True)

    email = db.Column(db.String(255), nullable=False)

    phone = db.Column(db.String(30), nullable=True)

    location = db.Column(db.String(255), nullable=True)

    # Foreign key to the service requested
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)

    # Main message from the user
    message = db.Column(db.Text, nullable=False)

    # User consent for data handling
    consent = db.Column(db.Boolean, default=False)

    # Internal case status
    status = db.Column(
        db.String(50),
        default="pending"
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship back to Service
    service = db.relationship("Service", backref="help_requests")



class MentalHealthDetail(db.Model):
    __tablename__ = "mental_health_details"

    id = db.Column(db.Integer, primary_key=True)

    help_request_id = db.Column(
        db.Integer,
        db.ForeignKey("help_requests.id"),
        nullable=False,
        unique=True
    )

    # Anxiety, depression, stress, etc.
    concern_type = db.Column(db.String(255), nullable=True)

    # How long the user has felt this way
    duration = db.Column(db.String(100), nullable=True)

    # Email / call / chat
    preferred_contact = db.Column(db.String(50), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    help_request = db.relationship("HelpRequest", backref="mental_health_detail")


class AbuseReport(db.Model):
    __tablename__ = "abuse_reports"

    id = db.Column(db.Integer, primary_key=True)

    help_request_id = db.Column(
        db.Integer,
        db.ForeignKey("help_requests.id"),
        nullable=False,
        unique=True
    )

    # Domestic, emotional, workplace, etc.
    abuse_type = db.Column(db.String(255), nullable=True)

    # Is the situation still happening?
    ongoing = db.Column(db.Boolean, default=False)

    # Safety check (non-graphic, yes/no)
    immediate_danger = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    help_request = db.relationship("HelpRequest", backref="abuse_report")


class HumanRightsReport(db.Model):
    __tablename__ = "human_rights_reports"

    id = db.Column(db.Integer, primary_key=True)

    help_request_id = db.Column(
        db.Integer,
        db.ForeignKey("help_requests.id"),
        nullable=False,
        unique=True
    )

    # Type of violation
    violation_type = db.Column(db.String(255), nullable=True)

    # When the incident occurred
    incident_date = db.Column(db.Date, nullable=True)

    # Organization or person involved
    reported_party = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    help_request = db.relationship("HelpRequest", backref="human_rights_report")



class WellnessDetail(db.Model):
    __tablename__ = "wellness_details"

    id = db.Column(db.Integer, primary_key=True)

    help_request_id = db.Column(
        db.Integer,
        db.ForeignKey("help_requests.id"),
        nullable=False,
        unique=True
    )

    focus_area = db.Column(db.String(255), nullable=True)

    preferred_guidance = db.Column(db.String(100), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    help_request = db.relationship("HelpRequest", backref="wellness_detail")



class Volunteer(db.Model):
    __tablename__ = "volunteers"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(255), nullable=False)

    skills = db.Column(db.Text, nullable=True)

    availability = db.Column(db.String(100), nullable=True)

    motivation = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
