import os
from datetime import datetime
from flask_mail import Message
from flask import render_template,redirect,request,url_for,make_response,session,flash,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from port import app,csrf,mail
from port.models import db, ContactMessage
from port.form import ContactForm


@app.get('/')
def home():
    return render_template('index.html')


@app.get('/get/help')
def get_help():
    return render_template('get_help.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        new_message = ContactMessage(
            full_name=form.full_name.data,
            subject=form.subject.data,
            email=form.email.data,
            contact_pref=form.contact_pref.data,
            message=form.message.data
        )

        db.session.add(new_message)
        db.session.commit()

        flash("Your message has been sent successfully.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html", form=form)

@app.get('/about')
def about():
    return render_template('about.html')

@app.route('/donate',methods=['GET','POST'])
def donate():
    return render_template('donate.html')

@app.route('/volunteer',methods=['GET','POST'])
def volunteer():
    return render_template('volunteer.html')

@app.route('/services',methods=['GET','POST'])
def services():
    return render_template('services.html')

@app.route('/formy',methods=['GET','POST'])
def formy():
    return render_template('formy.html')
