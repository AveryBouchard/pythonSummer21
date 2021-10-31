"""
File: company.py
Creates Employee and Customer classes to manage customers and employees
"""

# import pre established Person class for the parent class
from person import Person


class Customer(Person):
    """Represents a Customer object"""
    def __init__(self, name, address, phone, credit_score):
        """Constructor to create a Customer object with the credit score added to
            the given name, address and phone from the parent class Person"""
        Person.__init__(self, name, address, phone)  # instantiates name address and phone to class
        self.credit_score = credit_score

    def set_credit_score(self, credit_score):
        """overwrite credit_score with new credit_score number given"""
        self.credit_score = credit_score

    def get_credit_score(self):
        """returns the Customer credit score"""
        return self.credit_score

    def __str__(self):
        """Returns the string representation of the Customer"""
        return "Name: " + str(self.get_name()) + "\n" + \
            "Address: " + str(self.get_address()) + "\n" + \
            "Phone: " + str(self.get_phone()) + "\n" + \
            "Credit Score: " + str(self.get_credit_score())


class Employee(Person):
    """Represents an Employee object"""
    def __init__(self, name, address, phone, badge, salary):
        """Constructor to create an Employee object with the badge and salary added to
                    the given name, address and phone from the parent class Person"""
        Person.__init__(self, name, address, phone)
        self.badge = badge
        self.salary = salary

    def set_badge(self, badge):
        """overwrite badge with new badge number given"""
        self.badge = badge

    def get_badge(self):
        """returns badge number"""
        return self.badge

    def set_salary(self, salary):
        """overwrite salary with new salary number given"""
        self.salary = salary

    def get_salary(self):
        """returns salary"""
        return self.salary

    def __str__(self):
        return "Name: " + str(self.get_name()) + "\n" + \
               "Address: " + str(self.get_address()) + "\n" + \
               "Phone: " + str(self.get_phone()) + "\n" + \
               "Badge: " + str(self.get_badge())

    def __eq__(self, other):
        if self is other:
            return True
        else:
            return self.name == other or self.badge == other

