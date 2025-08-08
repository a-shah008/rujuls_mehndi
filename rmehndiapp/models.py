from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    geo_area = db.Column(db.String, nullable=False)
    message = db.Column(db.Text, nullable=False)

    time_created = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"\n\n{self.fullname}: {self.message}\n\n"
    
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Organizer Contact Information:
    organizer_name = db.Column(db.String, nullable=False)
    organizer_email = db.Column(db.String, nullable=False)
    organizer_phone_number = db.Column(db.String, nullable=False)

    # Event General Information:
    event_name = db.Column(db.String(25), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    event_location = db.Column(db.String, nullable=False)
    event_date = db.Column(db.String, nullable=False)
    event_start_time = db.Column(db.String, nullable=False)
    event_end_time = db.Column(db.String, nullable=False)
    event_extra_comments = db.Column(db.String(150), nullable=False)

    # Admin Side Information:
    admin_time_created = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"\n\n{self.organizer_name}: {self.event_name} - {self.event_date}\n\n"
