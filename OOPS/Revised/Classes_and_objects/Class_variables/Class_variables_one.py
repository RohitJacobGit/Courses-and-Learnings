class abc:

    # class variable
    # same name as instance var
    x = 5 

    def __init__(self):
        self.x = 100

    def display(self):
        print(self.x)    
        print(abc.x)

abc_obj = abc()
print(abc_obj.x) # hides the class variable value
print(abc.x)
