#!/usr/bin/python

import requests
import bs4
import weekdays
import re
import smtplib
from email.mime.text import MIMEText

sat = weekdays.weekdays(5, 0).get_weekday_date()
sun = weekdays.weekdays(6, 0).get_weekday_date()

root_url = 'http://kalender.soccarena-olympiapark.de/kalender'
court_url = root_url + '/courts/courts.php?kalenderTag='

sat_url = court_url + str(sat)
sun_url = court_url + str(sun)


offset = 0

def get_frei_url (url):
    response = requests.get (url)
    soup = bs4.BeautifulSoup (response.text)
    return [a.attrs.get('href') for a in soup.select('td.buchbar a[href^=../anfrage/anfrage.php]')]


def get_buch_url (url):

    # stripped the head double dot
    s_url = re.sub ("^\.\.", "", url)

    # append the root url
    buch_url = root_url + s_url

    return buch_url

def send_buch_email (text):

    sender = 'bo.li.football.muc@gmail.com'
    receivers = ['tuhonghao@gmail.com', 'liber1986@gmail.com']
    # receivers = ['liber1986@gmail.com']
    username = 'bo.li.football.muc@gmail.com'
    password = '1982528lB!'

    # message = """From: From Bo Li <liber1986@gmail.com>
    # To: Team members
    # Subject: Soccer field booking information test

    # This is a e-mail test message
    # """ 

    content = "Found the following place(s): \n" + text

    msg = MIMEText (content)
    msg['Subject']= "Soccer field booking information test"
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

if __name__ == "__main__":

    frei_url_sat = get_frei_url(sat_url)
    frei_url_sun = get_frei_url(sun_url)

    zusam_url = frei_url_sat + frei_url_sun

    text = ""

    for url_sat in zusam_url:
        text = text +  get_buch_url (url_sat) + "\n"

    if offset:
        if text != "":
            send_buch_email (text)
    else:
        print text

# print str(frei_url_sat) + str(frei_url_sun)
# print root_url + str(frei_url_sat) + '\n' + root_url + str(frei_url_sun)
