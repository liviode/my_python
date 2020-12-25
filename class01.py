class Person:
    """This class shows the structure of a persons data"""

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printMyName(self):
        print(self.firstName + " " + self.lastName)



livio = Person('Livio', 'de Capitani')
toni = Person('Toni', 'Bünter')


livio.printMyName()

toni.printMyName()
toni.firstName = 'Anton'
toni.printMyName()


toni.yearOfBirth = 1964
print(toni.yearOfBirth)

# print(livio.yearOfBirth)
