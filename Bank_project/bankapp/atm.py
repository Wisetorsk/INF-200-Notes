# -*- coding: utf-8 -*-
from bankapp.printer import Printer
"""

"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class ATM(object):

    users = {"marius": 1234}
    accounts = {"marius": 5000}

    def __init__(self, user):
        self.current_user = user
        self.balance = None
        self.actions = []

    def authenticate(self):
        """
        returns true if authentication is successful
        :return:
        """
        if self.current_user in self.users:
            pin = int(raw_input('Please enter pin for user "{}":'.format(self.current_user.capitalize())))
            if self.users[self.current_user] != pin:
                raise ValueError('Invalid PIN')
            else:
                print "User authentication successful"
                self.balance = self.users[self.current_user]
                return True

    def withdraw(self, amount):
        self.actions.append(["withdraw", amount])
        self.balance -= amount

    def deposit(self, amount):
        self.actions.append(["deposit", amount])
        self.balance += amount

    def printout(self):
        inst = Printer(self.actions, self.balance)
        inst.receipt()

    def selector(self):
        selection = raw_input("Please select action: ")
        return selection

    def atm(self):
        if self.authenticate():
            self.balance = self.accounts[self.current_user]
            print "Welcome {}!".format(self.current_user.capitalize())
            selected = self.selector()
            amount = raw_input('amount: ')
            if selected[:2].strip().lower() == "wi":
                self.withdraw(amount)
            elif selected[:2].strip().lower() == "de":
                self.deposit(amount)
            Printer(self.actions).receipt()
