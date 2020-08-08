class Teacher:

    def greet(self):
        print('Teacher!')


class Student:

    def greet(self):
        print('Student!')


class TeacherAssistant(Teacher, Student):
    # greet() from Teacher is printed first as priority is from left->right
    pass
    # def greet(self):
    #    print('TeacherAssistant!')


ta = TeacherAssistant()
ta.greet()
print(TeacherAssistant.__bases__)
