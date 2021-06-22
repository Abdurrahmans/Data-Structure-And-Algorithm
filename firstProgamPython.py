class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
    def frintname(self):
         print(self.firstName,self.lastName)

class Student(Person):
    def __init__(self ,fname,lname,year):
        super(person,self).__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.firstName , self.lastName,  self.graduationyear)


x = Student('Abdur','Rahman', 2020)
x.welcome()