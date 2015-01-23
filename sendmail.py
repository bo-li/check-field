#!/usr/bin/python

import smtplib

def send_buch_email (sub):

    sender = 'bo.li.football.muc@gmail.com'
    receivers = ['liber1986@gmail.com']
    username = 'bo.li.football.muc@gmail.com'
    password = '1982528lB!'

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
