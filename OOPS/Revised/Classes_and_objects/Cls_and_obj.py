# %%
class Person:
    def set_details(self, name, age):
        # self.name & self.age are instance variables and can be used anywhere within the class
        # name & age can be used only in this definition
        self.name = name
        self.age = age
    
    # Usually self is used but other keyword can be used as well
    def display(self):
        print('age is: ', self.age)

    # self = current instance of this class
    def greet(self):
        print('Hello', self.name)
        self.display()


p1 = Person()
p1.set_details('anand', 30)

p1.greet()

# %%
