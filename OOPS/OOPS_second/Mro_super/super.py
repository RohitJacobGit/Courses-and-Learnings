class Teacher:
    def greet(self):
        Person.greet(self)
        print('I am teacher')

class Person:
    def greet(self):
        print('I am person')

class Student:
    def greet(self):
        Person.greet(self)
        print('I am Student')

class StudentAssistant(Teacher, Student):
    def greet(self):
        Teacher.greet(self)
        Student.greet(self)
        print('I am student assistant')


sa = StudentAssistant()
sa.greet()
# print(StudentAssistant.__bases__) # Base classes
# print(help(StudentAssistant))
# print(StudentAssistant.__mro__)
