from . import mail, db
from flask import render_template, current_app
from threading import Thread
from flask_mail import Message


def async_send_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, recipient, template, **kwargs):
    msg = Message(subject, sender=current_app.config['MAIL_DEFAULT_SENDER'], recipients=[recipient])
    msg.html = render_template(template, **kwargs)
    thr = Thread(target=async_send_mail, args=[current_app._get_current_object(), msg])
    thr.start()
    return thr