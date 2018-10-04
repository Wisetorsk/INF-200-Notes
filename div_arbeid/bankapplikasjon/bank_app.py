# -*- coding: utf-8 -*-
import shelve
import time

"""

"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Banking(object):

    def __init__(self, user_database, field=40):
        """

        :param user_database:
        :param field: with default value 40 chr
        :return:
        """
        self._title = '<TEST>'
        self._fieldwidth = field
        self._users = user_database
        self._current = None

    def set_field(self, field):
        """
        If fieldwidth needs to be altered during operation

        :param field:
        :return:
        """
        self._fieldwidth = field

    def open_account(self, acc_no):
        """

        :param acc_no:
        :return:
        """
        self._acc_no = str(acc_no)
        if acc_no not in self._users:
            print 'User not registered, register new?: \n\n'
            choice = raw_input('Y/N: ')
            if choice[0].lower() == 'y':
                username = raw_input('Name: ')
                surname = raw_input('Surname: ')
                while True:
                    try:
                        pin_1 = int(raw_input('PIN: '))
                        pin_2 = int(raw_input('Re-enter for verification: '))
                        if pin_1 == pin_2:
                            break
                        else:
                            print 'PINs do not match'
                    except ValueError:
                        print 'Input is invalid!'
                self._users[acc_no] = {'name': username, 'surname': surname,
                                       'pin': pin_1, 'balance': 0}
                self._current = self._users[acc_no]
        else:
            self._current = self._users[self._acc_no]
            print 'Welcome, {} {}'.format(self._current['name'],
                                          self._current['surname'])

    def end_operation(self):
        """

        :return:
        """
        self._users[self._acc_no] = self._current

    def head(self):
        print '-'*((self._fieldwidth - len(self._title) )/2) + \
              self._title + '-'*((self._fieldwidth - len(self._title))/2)
        print
        print '{}, {}'.format(self._current['surname'].capitalize(),
                             self._current['name'].capitalize())
        print 'Account number: ' + ' '*(self._fieldwidth-21) + \
              '{}'.format(self._acc_no)
        print '.'*self._fieldwidth + '\n'

    def footer(self):
        print '='*self._fieldwidth
        print self.timestamp() + ' '*(self._fieldwidth-20) + self.datestamp()
        print '='*self._fieldwidth

    def withdraw(self, amount):
        """

        :param amount:
        :return:
        """
        self.head()
        string_a = '\'Original balance: {:' + str(self._fieldwidth-19) + \
                   '}\'.format(self._current[\'balance\'])'
        print eval(string_a)
        self._current['balance'] -= amount
        action = '\'Withdraw: {:' + str(self._fieldwidth-11) + \
                 '}\'.format(amount)'
        print '-'*self._fieldwidth
        print eval(action)
        string_b = '\'New balance: {:' + str(self._fieldwidth-14) + \
                   '}\'.format(self._current[\'balance\'])'
        print eval(string_b)
        self.footer()

    def deposit(self, amount):
        """

        :param amount:
        :return:
        """
        self.head()
        string_a = '\'Original balance: {:' + str(self._fieldwidth-19) + \
                   '}\'.format(self._current[\'balance\'])'
        print eval(string_a)
        self._current['balance'] += amount
        print '-'*self._fieldwidth
        action = '\'Deposit: {:' + str(self._fieldwidth-10) + \
                 '}\'.format(amount)'
        print eval(action)
        string_b = '\'New balance: {:' + str(self._fieldwidth-14) + \
                   '}\'.format(self._current[\'balance\'])'
        print eval(string_b)
        self.footer()

    def dump(self):
        """

        :return:
        """
        try:
            print '='*self._fieldwidth
            strings = '\'Current balance: {:' + str(self._fieldwidth-18) + \
                      '}\'.format(self._current[\'balance\'])'
            print eval(strings)
            print '='*self._fieldwidth
        except TypeError:
            print 'User not logged inn, please run' \
                  ' "USERNAME".open_account("account number")'

    def datestamp(self):
        """

        :return:
        """
        mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
               'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        stamp = time.localtime()
        if len(str(stamp[2])) == 1:
            day = '0' + str(stamp[2])
        else:
            day = str(stamp[2])
        return '{}/{}/{}'.format(day, mon[stamp[1]], stamp[0])

    def timestamp(self):
        """

        :return:
        """
        stamp = time.localtime()
        timeprint = []
        for denom in range(3, 6):
            if len(str(stamp[denom])) == 1:
                timeprint.append('0' + str(stamp[denom]))
            else:
                timeprint.append(str(stamp[denom]))
        return '{}:{}:{}'.format(timeprint[0], timeprint[1], timeprint[2])

    def change_balance(self, amount):
        self._current['balance'] = amount
        self.end_operation()


class ATM(object):

    def __init__(self, db, field=40):
        self._field = field
        self._db = db

    def account(self):
        user = Banking(self._db, self._field)
        user.open_account(int(raw_input('Account number: ')))
        user.dump()

if __name__ == '__main__':
    db = shelve.open('Banking.dat')
    instance = Banking(db)
    instance.open_account(raw_input('Account number: '))
    instance.dump()
    instance.deposit(1500)
    instance.withdraw(1600)
    instance.dump()