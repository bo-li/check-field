#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

from datetime import datetime, timedelta

class weekdays:
    '''
    Generate the exact date of the 'n'th day in the 'ws'th week

    n = 0 : Monday
    n = 6 : Sunday

    ws = 0 : current week
    ws = 1 : increment the week by 1
    '''

    def __init__ (self, d, ws):
        self.d = int(d)
        self.current_time = datetime.now()
        self.weekday =self.current_time.weekday()
        self.t = timedelta ((7 + self.d - self.weekday) % 7 + ws * 7)
        self.dt = self.current_time + self.t

    def current_date (self):
        # print self.current_time.strftime('%Y-%m-%d')
        return self.current_time

    def current_weekday (self):
        return self.weekday

    def get_timedelta (self):
        return self.t

    def get_weekday_date (self):
        return self.dt.strftime('%Y-%m-%d')



if __name__ == "__main__":
    a = weekdays(6, 1)
    print a.get_weekday_date()
    
