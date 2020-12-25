class Person:
    """This class shows the structure of a persons data"""

    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l
        self.yearOfBirth = None

    def printMyName(self):
        print(self.firstName + " " + self.lastName)



livio = Person('Livio', 'de Capitani')
toni = Person('Toni', 'Bünter')

print(type(livio))


livio.printMyName()

toni.printMyName()
toni.firstName = 'Anton'
toni.printMyName()


toni.yearOfBirth = 1964
print(toni.yearOfBirth)

print(livio.yearOfBirth)
