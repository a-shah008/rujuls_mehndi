from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.models import Message, Event
from app.scripts import validate_phone_number, validate_email_address, validate_each_input, validate_date, validate_time
from datetime import datetime
from app.forms import BookEventForm, ContactUsForm


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():

    return render_template("home.html")

@app.route("/about", methods=["GET", "POST"])
def about():

    return render_template("about.html")

@app.route("/my_work", methods=["GET", "POST"])
def my_work():

    return render_template("my_work.html")

@app.route("/services", methods=["GET", "POST"])
def services():

    return render_template("services.html")

@app.route("/booking", methods=["GET", "POST"])
def booking():
    form = BookEventForm()

    if request.method == "POST":
        if form.validate_on_submit():
            inputs_all_exist = False
            user_agrees = False
            valid_email = False
            valid_phonenumber = False
            valid_date = False
            valid_times = False
            valid_extracomments = False

            inputs = []

            o_fullname = form.event_organizer_fullname.data
            o_email = form.event_organizer_email.data
            o_phonenumber = form.event_organizer_phonenumber.data
            o_areaofresidence = form.event_organizer_areaofresidence.data

            e_name = form.event_general_name.data
            e_type = form.event_general_type.data
            e_location = form.event_general_location.data
            e_date = form.event_general_date.data
            e_starttime = form.event_general_starttime.data
            e_endtime = form.event_general_endtime.data
            e_extracomments = form.event_general_extracomments.data

            inputs = [o_fullname, o_email, o_phonenumber, o_areaofresidence, e_name, e_type, e_location, e_date, e_starttime, e_endtime]

            error_in_input = False
            while error_in_input == False:
                if validate_each_input(inputs) == True:
                    inputs_all_exist = True
                    if form.agreed.data == True:
                        user_agrees = True
                        if validate_email_address(o_email) == False:
                            error_in_input = True
                            flash("The email inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_email = True
                        if validate_phone_number(o_phonenumber) == False:
                            error_in_input = True
                            flash("The phone number inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_phonenumber = True
                        if validate_date(e_date) == False:
                            error_in_input = True
                            flash("The date inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_date = True
                        if validate_time(e_starttime) == False or validate_time(e_endtime) == False:
                            error_in_input = True
                            flash("The time(s) inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_times = True
                        if e_extracomments != "" or e_extracomments != None:
                            if len(e_extracomments) <= 150:
                                valid_extracomments = True
                            else:
                                error_in_input = True
                                flash("Your extra comments exceeded the character limit of 150. Please try again.", "warning")
                                break
                        else:
                            e_extracomments = None
                            valid_extracomments = True
                    else:
                        error_in_input = True
                        flash("You must confirm that the information inputted in the form is accurate.", "warning")
                        break
                else:
                    error_in_input = True
                    flash("You have an empty input(s) in a required field. Please try again.", "warning")
                    break
                
                if inputs_all_exist and user_agrees and valid_email and valid_phonenumber and valid_date and valid_times and valid_extracomments:
                    time_created = datetime.now()
                    formatted_time_created = time_created.strftime("%m/%d/%Y, %H:%M:%S")
                    new_order = Event(organizer_name=o_fullname, organizer_email=o_email, organizer_phone_number=o_phonenumber, event_name=e_name, event_type=e_type, event_location=e_location, event_date=e_date, event_start_time=e_starttime, event_end_time=e_endtime, event_extra_comments=e_extracomments, admin_time_created=formatted_time_created)
                    db.session.add(new_order)
                    db.session.commit()
                    flash("Your event has been successfully sent to our database. We will reach out shortly to the contact information provided!", "success")
                    return redirect("home")
                else:
                    error_in_input = True
                    flash("There was an error with your inputs that we weren't able to catch. Please try again later.", "danger")
                    return redirect(url_for("booking"))

    return render_template("booking.html", form=form)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactUsForm()

    if request.method == "POST":
        if form.validate_on_submit():
            inputs_all_exist = False
            user_agrees = False
            valid_email = False
            valid_phonenumber = False
            valid_message = False

            inputs = []

            full_name = form.full_name.data
            email = form.email.data
            phone_number = form.phone_number.data
            geo_area = form.geographical_area.data
            message = form.message.data
            agreed = form.agreed.data

            inputs = [full_name, email, phone_number, geo_area, message, agreed]

            error_in_input = False
            while error_in_input == False:
                if validate_each_input(inputs) == True:
                    inputs_all_exist = True
                    if form.agreed.data == True:
                        user_agrees = True
                        if validate_email_address(email) == False:
                            error_in_input = True
                            flash("The email inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_email = True
                        if validate_phone_number(phone_number) == False:
                            error_in_input = True
                            flash("The phone number inputted is invalid. Please try again.", "warning")
                            break
                        else:
                            valid_phonenumber = True
                        if len(message) <= 150:
                            valid_message = True
                        else:
                            error_in_input = True
                            flash("Your extra comments exceeded the character limit of 150. Please try again.", "warning")
                            break
                    else:
                        error_in_input = True
                        flash("You must agree that the information inputted in the form is accurate.", "warning")
                        break
                else:
                    error_in_input = True
                    flash("You have an empty input(s) in a required field. Please try again.", "warning")
                    break

                if inputs_all_exist and user_agrees and valid_email and valid_phonenumber and valid_message:
                    time_created = datetime.now()
                    formatted_time_created = time_created.strftime("%m/%d/%Y, %H:%M:%S")
                    new_message = Message(fullname=full_name, email=email, phone_number=phone_number, geo_area=geo_area, message=message, time_created=formatted_time_created)
                    db.session.add(new_message)
                    db.session.commit()
                    flash("Your message has been successfully sent to our database. Thank you!", "success")
                    return redirect("home")
                else:
                    error_in_input = True
                    flash("There was an error with your inputs that we weren't able to catch. Please try again later.", "danger")
                    return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

