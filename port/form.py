from flask_wtf import FlaskForm
from wtforms import StringField, EmailField,PasswordField,SubmitField,TelField,TextAreaField,FileField,DateField, RadioField,DecimalField,IntegerField,SelectField,MultipleFileField,SelectMultipleField
from wtforms.validators import DataRequired,Email,Length,EqualTo,Optional,NumberRange
from flask_wtf.file import FileAllowed,FileRequired


class ContactForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[DataRequired(), Length(max=120)]
    )

    subject = SelectField(
        "Subject",
        choices=[
            ("General Inquiry", "General Inquiry"),
            ("Partnership Proposal", "Partnership Proposal"),
            ("Media/Press", "Media/Press"),
            ("Volunteering", "Volunteering"),
        ],
        validators=[DataRequired()]
    )

    email = StringField(
        "Email Address",
        validators=[DataRequired(), Email()]
    )

    contact_pref = RadioField(
        "Preferred Response",
        choices=[
            ("Email", "Email Response"),
            ("Phone", "Phone Call")
        ],
        default="Email"
    )

    message = TextAreaField(
        "Message",
        validators=[DataRequired(), Length(min=10)]
    )
