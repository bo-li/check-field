#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

import requests
import bs4
import weekdays, user_data, sendmail
import re
import smtplib
import sys
from email.mime.text import MIMEText


def get_frei_url (url):
    # Get the http response from the url
    response = requests.get (url)
    # use bs4 to parse the html text
    soup = bs4.BeautifulSoup (response.text)
    # return the link for "bookable" court
    return [a.attrs.get('href') for a in soup.select('td.buchbar a[href^=../anfrage/anfrage.php]')]


def get_buch_url (root_url, free_url, lower_limit, upper_limit,):
    # stripped the head double dot
    s_url = re.sub ("^\.\.", "", free_url)

    # append the root url
    buch_url = root_url + s_url

    # search the court number
    m = re.search('(?<=court\=)[0-9]', buch_url)

    # search the start time
    t = re.search('(?<=startZeit\=)\d\d', buch_url)

    if t is None:
        buch_url = ""
    else:
        startTime = int(t.group(0))
        # return empty if it is court 5 or not the in a reasonable time
        # range
        if int(m.group(0)) >= 5 or startTime > upper_limit or \
        startTime < lower_limit:
            buch_url=""

    return buch_url


def feed_user (user, week_shift):

    dates = [weekdays.weekdays (int(d), week_shift).get_weekday_date()
            for d in user.date()]
    print dates

    # FIXME: hard-coded text for url. Need to be updated the first time when
    # the source website updates
    root_url = 'http://kalender.soccarena-olympiapark.de/kalender'
    court_url = root_url + '/courts/courts.php?kalenderTag='

    date_url = [court_url + str(d) for d in dates]
    print date_url

    free_court_url = []

    # get_frei_url() returns a list, sticking to 1d list here by
    # combining them
    for durl in date_url:
        free_court_url = free_court_url + get_frei_url (str(durl))
    print free_court_url

    lt = user.time()[0]
    ut = user.time()[1]
    booking_url = [get_buch_url (root_url, str(url), lt, ut) for url in free_court_url]

    print booking_url

    text = ""
    for url in booking_url:
        if url == "":
            continue
        else:
            text = text + url + "\n"

    offset = 1

    if offset:
        if text != "":
            bmail = sendmail.buch_email (dates, text, user.email())
            bmail.send_email()
    else:
        print text

# main function starts
if __name__ == "__main__":

    # User tag:
    # current 0 or 1
    tag = int(sys.argv[1])

    # week increment, 0 for current week, 1 for the next week, etc.
    shift = int(sys.argv[2])

    user = user_data.user_data(tag)
    feed_user (user, shift)

