class Person:
    def greet(self):
        print('I am person')

class Teacher(Person):
    def greet(self):
        super().greet()
        print('I am teacher')

class Student(Person):
    def greet(self):
        super().greet()
        print('I am Student')

class StudentAssistant(Teacher, Student):
    def greet(self):
        super().greet()
        print('I am student assistant')


sa = StudentAssistant()
sa.greet()
# print(help(StudentAssistant))
s = Student()
s.greet()
print(help(s))