#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

import requests
import bs4
import weekdays
import re
import smtplib
import sys
from email.mime.text import MIMEText

# offset for text debug
offset = 1

# week increment, 0 for current week
shift = int(sys.argv[1])

# get the date of Saturday and Sunday
sat = weekdays.weekdays(5, shift).get_weekday_date()
sun = weekdays.weekdays(6, shift).get_weekday_date()

# FIXME: hard-coded text for url. Need to be updated the first time when
# the source website updates
root_url = 'http://kalender.soccarena-olympiapark.de/kalender'
court_url = root_url + '/courts/courts.php?kalenderTag='

# Yes so simple, this would be the url for field information of a given
# date!
sat_url = court_url + str(sat)
sun_url = court_url + str(sun)

def get_frei_url (url):
    # Get the http response from the url
    response = requests.get (url)
    # use bs4 to parse the html text
    soup = bs4.BeautifulSoup (response.text)
    # return the link for "bookable" court
    return [a.attrs.get('href') for a in soup.select('td.buchbar a[href^=../anfrage/anfrage.php]')]


def get_buch_url (url):

    # stripped the head double dot
    s_url = re.sub ("^\.\.", "", url)

    # append the root url
    buch_url = root_url + s_url

    return buch_url

def send_buch_email (text):
    '''
    Send the text from the "sender" to "receiver" hard-coded here
    FIXME: extremely insecure! DO NOT use any personal email as the sender
    '''

    sender = 'bo.li.football.muc@gmail.com'
    receivers = ['tuhonghao@gmail.com', 'liber1986@gmail.com']
    # receivers = ['liber1986@gmail.com']
    username = 'bo.li.football.muc@gmail.com'
    password = 'm6w9kj874'

    # message = """From: From Bo Li <liber1986@gmail.com>
    # To: Team members
    # Subject: Soccer field booking information test

    # This is a e-mail test message
    # """ 

    content = "Found the following place(s): \n" + text

    msg = MIMEText (content)
    msg['Subject']= "Soccer field booking information for " + str(sat) + " and " + str(sun)
    msg['From'] = "Bo Li" + "<" + sender + ">"
    msg['To'] = ";".join(receivers)

    try:
	smtpObj = smtplib.SMTP('smtp.gmail.com:587')
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(username, password)
	smtpObj.sendmail (sender, receivers, msg.as_string())
	smtpObj.quit()
	print "Sucessfully sent email"
    except SMTPException:
	print "Error: unable to send email"

# main function starts
if __name__ == "__main__":

    # get the free url for Satday and Sunday
    frei_url_sat = get_frei_url(sat_url)
    frei_url_sun = get_frei_url(sun_url)

    # Lazy work, combine the two url cells
    zusam_url = frei_url_sat + frei_url_sun

    text = ""

    for url_sat in zusam_url:
	# put all the urls in an string array
        text = text +  get_buch_url (url_sat) + "\n"

    if offset:
        if text != "":
            send_buch_email (text)
    else:
        print text

# print str(frei_url_sat) + str(frei_url_sun)
# print root_url + str(frei_url_sat) + '\n' + root_url + str(frei_url_sun)
