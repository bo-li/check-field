#!/usr/bin/python
# -*- mode: python; c-basic-offset: 4 -*- vim: set sw=4 tw=70 et sta ai:

class user_data:
    '''
    The users are expecting differencet dates for the field, thus sort
    out their requirement in a class
    '''
    
    def __init__ (self, tag):
        self.tag = tag
        self.dates = [[2, 3], [5, 6]]
        self.emails = ['Lu2003de@hotmail.com', 'tuhonghao@gmail.com']
        self.times = [[17, 21], [10, 20]]

        # make sure tags provided are in a valid range
        assert tag >= 0 and tag < len (self.dates)

    def date (self):
        return self.dates [self.tag]

    def email (self):
        return self.emails [self.tag]

    def time (self):
        return self.times [self.tag]


if __name__ == "__main__":
    a = user_data (0)
    print a.date(), a.email()
    b = user_data (1)
    print b.date(), b.email()

