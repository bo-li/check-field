#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

import smtplib

def send_buch_email (sub):
    '''
    This is the test to send email with python
    TODO: A class would be better
    '''

    sender = 'bo.li.football.muc@gmail.com'
    receivers = ['liber1986@gmail.com']
    username = 'bo.li.football.muc@gmail.com'
    password = 'm6w9kj874'

    message = """From: From Bo Li(Football)
    To: To Bo Li(Gmail)
    Subject: SMTP e-mail test

    This is a e-mail test message
    """ + sub

    try:
	smtpObj = smtplib.SMTP('smtp.gmail.com:587')
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(username, password)
	smtpObj.sendmail (sender, receivers, message)
	smtpObj.quit()
	print "Sucessfully sent email"
    except SMTPException:
	print "Error: unable to send email"

if __name__ == "__main__":
    send_buch_email ("hello world")
