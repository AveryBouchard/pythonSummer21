"""
Nathan Goldrick

Python Fall 2021

10/31/2021

File: company.py
Defines two separate classes named employee and customer that inherit another classes attributes and methods
"""

from person import Person


class Customer(Person):
    """Customer object"""
    def __init__(self, name, address, phone, credit_score):
        """Constructor that creates an object with the credit score added"""
        Person.__init__(self, name, address, phone)
        self.credit_score = credit_score

    def get_credit_score(self):
        """Returns the credit score of the customer"""
        return self.credit_score

    def set_credit_score(self, credit_score):
        """Sets credit_score to the new value entered instead of the old one"""
        self.credit_score = credit_score

    def __str__(self):
        """Returns the customer string"""
        return "name: " + str(self.get_name()) + "\n" + \
           "address: " + str(self.get_address()) + "\n" + \
           "phone: " + str(self.get_phone()) + "\n" + \
           "credit_score: " + str(self.get_credit_score())


class Employee(Person):
    """Employee object"""
    def __init__(self, name, address, phone, badge, salary):
        """Constructor that creates an object with the badge and salary added"""
        Person.__init__(self, name, address, phone)
        self.badge = badge
        self.salary = salary

    def get_badge(self):
        """Returns badge"""
        return self.badge

    def set_badge(self, badge):
        """Replaces old badge value with new badge value"""
        self.badge = badge

    def get_salary(self):
        """Returns salary"""
        return self.salary

    def set_salary(self, salary):
        """Replaces old salary value with new salary value"""
        self.salary = salary

    def __str__(self):
        return "name: " + str(self.get_name()) + "\n" + \
               "address: " + str(self.get_address()) + "\n" + \
               "phone: " + str(self.get_phone()) + "\n" + \
               "badge: " + str(self.get_badge())

    def __eq__(self, other):
        """Method that compares to make sure the name and the badge number are associated"""
        if self is other:
            return True
        else:
            return self.badge == other
