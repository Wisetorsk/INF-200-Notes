# -*- coding: utf-8 -*-
import time
import shelve

"""

"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Printer(object):
    """
    Class Printer takes input in the from of a dictionary containing actions taken and transaction values.
    Returns a printable string

    """
    number = shelve.open("reciept_no.dat")
    if len(number) < 1:
        number["no"] = 0

    def __init__(self, actions, balance, field_width=50, padding=5):
        """

        :param actions: list containing transaction details
        :return:
        """
        self.actions = actions
        self.field_width = field_width
        self.padding = padding
        self.balance = balance

    def contents(self):
        printable = ""
        sums = 0
        for action in self.actions:
            printable += (self.padding * " ") + "{}".format(action[0]) + \
                         ("{:32}".format(action[1]) if action[0] == "withdraw" else "{:33}".format(action[1])
                          )
            printable += "\n"
            if action[0] == "withdraw":
                sums -= action[1]
            else:
                sums += action[1]
        printable += (self.padding * " ") + ((self.field_width - 10) * "=") + "\n" + \
                     (self.padding * " ") + "Balance change" + "{:26}".format(sums) + "\n"
        printable += (self.padding * " ") + "New balance" + " {:28}".format(self.balance)
        return printable

    def header(self):
        """
        Adds the top header to the reciept printout string
        :return:
        """
        return ((self.field_width / 2 - 2) * "-") + "BANK" + ((self.field_width / 2 - 2) * "-")

    def footer(self):
        """
        Adds footer with receipt number and timestamp
        :return:
        """
        self.number["no"] += 1
        self.number = shelve.open("reciept_no.dat")
        return (self.field_width * "-") + "\n" + self.time_date() + "\n" + (self.padding * " ") + "Reciept number: {}"\
            .format(self.number["no"]) + "\n" + (self.field_width * "-")

    def time_date(self):
        values = time.localtime()
        values = values[:7]
        stamp = []
        for value in values:
            if len(str(value)) == 1:
                value = "0" + str(value)
                stamp.append(value)
            else:
                stamp.append(str(value))
        return (self.padding * " ") + "{}.{}.{}".format(stamp[2], stamp[1], stamp[0]) + \
               (" " * (self.field_width - 2 * self.padding - 18)) + "{}:{}:{}".format(stamp[3], stamp[4], stamp[5]) + \
               (self.padding * " ")

    def receipt(self):
        printable = self.header() + "\n" + self.contents() + "\n" + self.footer()
        print printable
