#!/usr/bin/python
from datetime import datetime, timedelta

class weekdays:

    def __init__ (self, d, ws):
        self.d = d
        self.current_time = datetime.now()
        self.weekday = self.current_time.weekday()
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
    
