from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


class BookEventForm(FlaskForm):
    # Event Organizer Information:
    event_organizer_fullname = StringField("Full Name of Organizer:", validators=[DataRequired()])
    event_organizer_email = StringField("Email of Organizer:", validators=[DataRequired()])
    event_organizer_phonenumber = StringField("Phone Number of Organizer:", validators=[DataRequired()])
    event_organizer_areaofresidence = StringField("City, State, Zip Code of Organizer:", validators=[DataRequired()])

    # Event General Information
    event_general_name = StringField("Name of Event:", validators=[DataRequired()])
    event_general_type = StringField("Type of Event:", validators=[DataRequired()])
    event_general_location = StringField("Location of Event:", validators=[DataRequired()])
    event_general_date = StringField("Date of Event:", validators=[DataRequired()])
    event_general_starttime = StringField("Event Start Time:", validators=[DataRequired()])
    event_general_endtime = StringField("Event End Time:", validators=[DataRequired()])
    event_general_extracomments = TextAreaField("Extra Comments (Optional):")

    agreed = BooleanField("I agree that the information inputted in the form above is accurate.")

    submit = SubmitField("Submit")

class ContactUsForm(FlaskForm):
    full_name = StringField("Full Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    phone_number = StringField("Phone Number:", validators=[DataRequired()])
    geographical_area = StringField("City, State, Zip Code:", validators=[DataRequired()])
    message = TextAreaField("Comments:")

    agreed = BooleanField("I agree that the information inputted in the form above is accurate.")

    submit = SubmitField("Submit")
