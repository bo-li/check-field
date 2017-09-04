#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

import smtplib
import sys
from email.mime.text import MIMEText

class buch_email:
    '''
    Send the text from the "sender" to "receiver" hard-coded here
    FIXME: extremely insecure! DO NOT use any personal email as the sender
    '''

    def __init__ (self, dates, text, user_email):
        self.dates = dates
        self.text = text
        self.user_email = user_email
        self.sender = 'bo.li.football.muc@gmail.com'
        self.receivers = [self.user_email, 'liber1986@gmail.com']
        self.username = 'bo.li.football.muc@gmail.com'
        self.password = ''

    def send_email (self):
        '''
        Send the text from the "sender" to "receiver" hard-coded here
        FIXME: extremely insecure! DO NOT use any personal email as the sender
        '''
        # message = """From: From Bo Li <liber1986@gmail.com>
        # To: Team members
        # Subject: Soccer field booking information test

        # This is a e-mail test message
        # """ 

        content = "Found the following place(s): \n" + self.text

        msg = MIMEText (content)
        # msg['Subject']= "Soccer field booking information for " + str(sat) + " and " + str(sun)
        title = "Soccer field booking information for "
        for d in self.dates:
            title = title + str(d) + " "
        msg['Subject'] = title
        msg['From'] = "Bo Li" + "<" + self.sender + ">"
        msg['To'] = ";".join(self.receivers)

        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com:587')
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(self.username, self.password)
            smtpObj.sendmail (self.sender, self.receivers, msg.as_string())
            smtpObj.quit()
            print "Sucessfully sent email"
        except smtplib.SMTPException:
            print "Error: unable to send email"

if __name__ == "__main__":
    a = buch_email(['2015-10-21', '2015-10-22'], "hello world",
            "bo.li@tum.de")
    a.send_email()
