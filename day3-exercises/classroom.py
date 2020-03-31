#!/bin/python

class Person:

    """
    This class takes firstname and lastname as arguments and returns them as a combined string.
    """
    
    def __init__(self, firstname, lastname):
        """
        Create firstname and lastname for a given person
        """
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return("The name of this person is: {} {} ".format(self.firstname, self.lastname))




class Student(Person):
    """
    This class inherits from the Person class, takes subject as argument as well and returns them as a combined string.
    """

    def __init__(self, firstname, lastname, subject):
        super().__init__(firstname, lastname)
        """
        Create firstname and lastname for a given person
        """
        self.subject = subject

    def __str__(self):
        return("The name and subject are: {} {}, {} ".format(self.firstname, self.lastname, self.subject))

    def printNameSubject(self):
        self.printNameSubject = print("{} {}, {}".format(self.firstname, self.lastname, self.subject))
        

class Teacher(Person):
    """
    This class inherits from the Person class, takes course as argument as well and returns them as a combined string.
    """

    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        """
        Create firstname and lastname for a given person
        """
        self.course = course

    def __str__(self):
        return("The teacher {} {} is teaching the {} course".format(self.firstname, self.lastname, self.course))

    def printNameSubject(self):
        self.printNameSubject = print("{} {}, {}".format(self.firstname, self.lastname, self.course))
