class Teacher:
    def greet(self):
        print('I am teacher')

    def __str__(self):
        return 'Class: Teacher'

class Student:
    def greet(self):
        print('I am Student')

    def __str__(self):
        return 'Class: Student'

# class StudentAssistant(Teacher, Student):
#     def greet(self):
#         print('I am student assistant')

# sa = StudentAssistant()
# sa.greet()


# class StudentAssistant(Teacher, Student):
#     pass

# sa = StudentAssistant()
# sa.greet()

class StudentAssistant(Student, Teacher):
    def greet(self):
        Teacher.greet(self)
        Student.greet(self)
        print('I am student assistant')


sa = StudentAssistant()
sa.greet()
# print(StudentAssistant.__bases__) # Base classes
# print(help(StudentAssistant))
print(StudentAssistant.__mro__)
print(StudentAssistant.mro())
print(sa.__class__.__mro__)
